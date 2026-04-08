from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
import shutil
import os
import json
import uuid

# Correct Architecture Imports
#from .database import get_db
#from . import crud, schemas
from services.translation import TranslationService
#from .services.anonymization import PrivacyService
#from .services.anonymization import AnonymizationService

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Landing page
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request, lang: str = "en"):
    labels = TranslationService.get_ui_labels(lang)
    return templates.TemplateResponse(
        request=request,       
        name="index.html", 
        context={
            "lang": lang, 
            "labels": labels
        }
    )

# Reporting Form 

# Create a local directory for reports if it doesn't exist
REPORTS_DIR = "local_reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

# Serve the Report Form
@app.get("/report", response_class=HTMLResponse)
async def get_report_form(request: Request, lang: str = "en"):
    labels = TranslationService.get_ui_labels(lang)
    
    return templates.TemplateResponse(
        request=request,
        name="report_form.html",
        context={
            "lang": lang,
            "labels": labels
        }
    )
# Handle Form Submission (Local Storage) --> will link to DB in future
@app.post("/report")
async def post_report_form(
    request: Request,
    lang: str = "en",
    lat: str = Form(...),
    lng: str = Form(...),
    level: str = Form(...),
    notes: str = Form(None),
    damage_photo: UploadFile = File(None)
):
    report_id = str(uuid.uuid4())
    
    # Generate a dynamic UTC timestamp in ISO format
    # Example: "2026-04-08T14:30:00Z"
    current_time = datetime.now(timezone.utc).isoformat()

    report_data = {
        "report_id": report_id,
        "language": lang,
        "location": {"lat": lat, "lng": lng},
        "severity": level,
        "notes": notes,
        "timestamp": current_time  # Dynamic timestamp
    }

    # Save JSON data
    file_path = os.path.join(REPORTS_DIR, f"{report_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4)

    # Save Photo if provided
    if damage_photo and damage_photo.filename:
        photo_path = os.path.join(REPORTS_DIR, f"{report_id}_photo.jpg")
        with open(photo_path, "wb") as buffer:
            buffer.write(await damage_photo.read())

    return RedirectResponse(url=f"/?lang={lang}", status_code=303)
# @app.get("/report")
# async def report_form_get(request: Request):
#     # Detect browser language (e.g., "es-MX,es;q=0.9")
#     browser_lang = request.headers.get("accept-language", "en")
#     target_lang = "en"
#     for lang_code in ["ar", "fr", "es", "sw", "pt"]:
#         if lang_code in browser_lang.lower():
#             target_lang = lang_code
#             break
#     # Fetch the correct UI strings
#     labels = TranslationService.get_ui_labels(target_lang)
#     return templates.TemplateResponse(
#             "report_form.html", 
#             {
#                 "request": request, 
#                 "lang": target_lang, 
#                 "labels": labels
#             }
#         )

# @app.post("/report")
# async def submit_report(
#     request: Request,
#     lat: float = Form(...),
#     lng: float = Form(...),
#     level: str = Form(...),
#     damage_photo: UploadFile = File(None),
#     notes: str = Form(None),
#     db: AsyncSession = Depends(get_db)
# ):
#     """
#     Receives the emergency data, sanitizes it, and saves it.
#     """
#     # 1. Image Storage (Placeholder for actual bucket logic)
#     image_url = None
#     if damage_photo:
#         file_location = f"uploads/{damage_photo.filename}"
#         with open(file_location, "wb+") as file_object:
#             shutil.copyfileobj(damage_photo.file, file_object)
#         image_url = f"/{file_location}"

#     # 2. Service Layer: Privacy & Safety
#     public_lat, public_lng = AnonymizationService.blur_location(lat, lng)
#     safe_notes = AnonymizationService.strip_pii_from_text(notes)

#     # 3. Validation via Pydantic Schema
#     report_data = schemas.DamageReportCreate(
#         latitude=lat,
#         longitude=lng,
#         damage_level=level,
#         notes=safe_notes
#     )

#     # 4. Database execution
#     # await crud.create_report(db, report_data, public_lat, public_lng, image_url)

#     return {"status": "success", "message": "Report secured and filed."}

# Community Map 
# @app.get("/map", response_class=HTMLResponse)
# async def community_map(request: Request, lang: str = "en"):
#     return templates.TemplateResponse(request, "community_map.html", {"lang": lang})

# 404 
# @app.exception_handler(404)
# async def custom_404_handler(request: Request, __):
#     lang = "en"     # Default language for error pages
#     if request.url.path.startswith("/admin"):
#         return templates.TemplateResponse(request, "404_admin.html", context={"lang": lang}, status_code=404)
#     return templates.TemplateResponse(request, "404_user.html", context={"lang": lang}, status_code=404)


@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    lang = request.query_params.get("lang", "en")
    labels = TranslationService.get_ui_labels(lang)
    template = "404_admin.html" if request.url.path.startswith("/admin") else "404_user.html"

    return templates.TemplateResponse(
        request=request,
        name=template,
        context={
            "lang": lang,
            "labels": labels 
        },
        status_code=404
    )
