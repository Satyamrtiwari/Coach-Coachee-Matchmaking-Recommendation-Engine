from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as api_router
from app.models.database import db
from app.services.matcher import matcher_service

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    # Load JSON file of coaches
    db.load_data()
    # Initialize the TF-IDF embeddings on the loaded data
    matcher_service.initialize()
    print(f"Loaded {len(db.get_all_coaches())} coaches into the matcher service.")

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API. Visit /docs for the swagger playground."}
