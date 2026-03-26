from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# The Custom 404 Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    # If the URL starts with /admin, give them the technical 404
    if request.url.path.startswith("/admin"):
        return templates.TemplateResponse("404_admin.html", {
            "request": request
        }, status_code=404)
    
    # Otherwise, give the public the reassurance 404
    return templates.TemplateResponse("404_user.html", {
        "request": request
    }, status_code=404)

# Landing page
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request, lang: str = "en"):
    return templates.TemplateResponse("landing.html", {"request": request, "lang": lang})

# Reporting Form 
@app.get("/report", response_class=HTMLResponse)
async def report_form(request: Request):
    return templates.TemplateResponse("report_form.html", {"request": request})

# Community Map 
@app.get("/map", response_class=HTMLResponse)
async def community_map(request: Request):
    return templates.TemplateResponse("community_map.html", {"request": request})
