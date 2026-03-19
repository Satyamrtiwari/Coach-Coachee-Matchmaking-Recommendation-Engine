from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from app.core.config import settings
from app.api.routes import router as api_router
from app.models.database import db
from app.services.matcher import matcher_service

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    db.load_data()    # Load JSON file of coaches
    matcher_service.initialize()    # Initialize the TF-IDF embeddings on the loaded data
    print(f"Loaded {len(db.get_all_coaches())} coaches into the matcher service.")

app.include_router(api_router, prefix=settings.API_V1_STR)

# inntegrated the static folder to serve assets/HTML
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_root():
    html_path = os.path.join(static_dir, "index.html")      # Attempt to return the beautiful frontend index.html
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"message": f"Welcome to {settings.PROJECT_NAME} API. Visit /docs for the swagger playground."}
