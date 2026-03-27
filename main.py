from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

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
    return templates.TemplateResponse(request, "community_map.html.html", {"lang": lang})
