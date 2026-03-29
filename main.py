from fastapi import FastAPI, Request, status, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from . import crud, schemas
from .services.anonymization import PrivacyService
from .services.translation import TranslationService

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Landing page
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request, lang: str = "en"):
    return templates.TemplateResponse(request, "index.html", {"lang": lang})

# Reporting Form 
@app.get("/report", response_class=HTMLResponse)
async def report_form(request: Request, lang: str = "en"):
    return templates.TemplateResponse(request, "report_form.html", {"lang": lang})

@app.post("/report")
async def handle_report(
    request: Request,
    lat: float = Form(...),
    lng: float = Form(...),
    damage_level: str = Form(...),
    reporter_name: str = Form(None),
    db: AsyncSession = Depends(get_db)
):
    # 1. Use Privacy Service to protect the reporter
    safe_name = PrivacyService.anonymize_reporter(reporter_name)
    
    # 2. Prepare the data using our Schema
    report_in = schemas.DamageReportCreate(
        latitude=lat,
        longitude=lng,
        damage_level=damage_level,
        reporter_name=safe_name
    )
    
    # 3. Save via CRUD
    await crud.create_damage_report(db, report_in)
    
    return {"status": "success", "message": "Report secured and filed."}

# Community Map 
@app.get("/map", response_class=HTMLResponse)
async def community_map(request: Request, lang: str = "en"):
    return templates.TemplateResponse(request, "community_map.html", {"lang": lang})

# 404 
@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    lang = "en"     # Default language for error pages
    if request.url.path.startswith("/admin"):
        return templates.TemplateResponse(request, "404_admin.html", context={"lang": lang}, status_code=404)
    return templates.TemplateResponse(request, "404_user.html", context={"lang": lang}, status_code=404)
