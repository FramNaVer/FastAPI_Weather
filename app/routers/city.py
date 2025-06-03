from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.city import City
from app.schemas.city import CityOut
from typing import List

router = APIRouter(prefix="/cities", tags=["Cities"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CityOut])
def get_cities(db: Session = Depends(get_db)):
    return db.query(City).all()
