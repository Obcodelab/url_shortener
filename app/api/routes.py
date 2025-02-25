import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.schemas.url import URLCreate, URLResponse, StatResponse
from app.models.url import URL
from app.core.config import SessionLocal
from app.services.shortener import generate_short_code

from dotenv import load_dotenv

load_dotenv()


router = APIRouter()

backend_url = os.getenv("backend_url")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/shorten", response_model=URLResponse)
def shorten_url(url_data: URLCreate, db: Session = Depends(get_db)):
    """Shorten a given url and store it in the database."""
    short_code = url_data.short_code or generate_short_code()
    existing_url = db.query(URL).filter(URL.short_code == short_code).first()
    if existing_url:
        raise HTTPException(
            status_code=409, detail="Short code already exists. Choose another."
        )

    new_url = URL(original_url=str(url_data.original_url), short_code=short_code)

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "original_url": new_url.original_url,
        "short_code": new_url.short_code,
        "new_url": f"{backend_url}/{new_url.short_code}",
    }


@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    """Redirect to the original url using the short code."""
    url_entry = db.query(URL).filter(URL.short_code == short_code).first()
    if not url_entry:
        raise HTTPException(status_code=404, detail="URL not found")

    url_entry.click_count += 1
    db.commit()

    return RedirectResponse(url_entry.original_url)


@router.get("/stats/{short_code}", response_model=StatResponse)
def get_url_stat(short_code: str, db: Session = Depends(get_db)):
    """Retrieve stats for a short url"""
    url_entry = db.query(URL).filter(URL.short_code == short_code).first()
    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return {
        "original_url": url_entry.original_url,
        "short_code": url_entry.short_code,
        "new_url": f"{backend_url}/{url_entry.short_code}",
        "click_count": url_entry.click_count,
        "created_at": url_entry.created_at,
    }
