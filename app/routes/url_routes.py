from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from .. import models, schema as schemas, utlis as utils
from ..database import get_db

router = APIRouter()

@router.post("/shorten", response_model=schemas.URLInfo)
def create_short_url(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    # Step 1: Save original URL first (to get ID)
    db_url = models.URL(original_url=url_data.original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    # Step 2: Generate short code using ID
    short_code = utils.generate_short_code(db_url.id)
    db_url.short_code = short_code
    db.commit()
    db.refresh(db_url)

    short_url = f"http://localhost:8000/{short_code}"
    return {"original_url": db_url.original_url, "short_url": short_url}

@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    # Step 3: Retrieve original URL
    url_entry = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if not url_entry:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=url_entry.original_url)
