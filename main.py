from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Landing page
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request, lang: str = "en"):
    return templates.TemplateResponse(request, "index.html", {"lang": lang})#return templates.TemplateResponse(name="index.html", context={"request": request, "lang": lang})

@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request, lang: str = "en"):
    return templates.TemplateResponse(
        name="index.html", 
        context={"request": request, "lang": lang}
    )

# Reporting Form 
@app.get("/report", response_class=HTMLResponse)
async def report_form(request: Request):
    return templates.TemplateResponse("report_form.html", {"request": request})

# Community Map 
@app.get("/map", response_class=HTMLResponse)
async def community_map(request: Request):
    return templates.TemplateResponse("community_map.html", {"request": request})
