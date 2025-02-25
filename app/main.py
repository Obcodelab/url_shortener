from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.url import Base
from app.core.config import engine
from app.api.routes import router

app = FastAPI(title="URL Shortener API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to URL Shortener API"}
