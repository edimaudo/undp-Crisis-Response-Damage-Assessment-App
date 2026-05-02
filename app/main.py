from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import public, auth, reports, dashboard, export, rewards

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(public.router)
app.include_router(auth.router, prefix="/auth")
app.include_router(reports.router, prefix="/reports")
app.include_router(dashboard.router, prefix="/dashboard")
app.include_router(export.router, prefix="/export")
app.include_router(rewards.router, prefix="/rewards")
