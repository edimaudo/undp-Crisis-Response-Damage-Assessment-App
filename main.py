from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
