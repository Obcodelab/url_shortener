from fastapi import FastAPI
from app.models.url import Base
from app.core.config import engine
from app.api.routes import router

app = FastAPI(title="URL Shortener API", version="1.0")

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to URL Shortener API"}
