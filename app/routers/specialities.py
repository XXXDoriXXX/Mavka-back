# app/api/speciality.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies import require_role
from app.models import Speciality
from app.schemas.speciality import SpecialityCreate, SpecialityResponse

router = APIRouter(prefix="/specialities", tags=["specialities"])


@router.post("/", response_model=SpecialityResponse)
def create_speciality(speciality: SpecialityCreate,
                      db: Session = Depends(get_db),
                      current_user=Depends(require_role("admin"))):
    db_speciality = Speciality(name=speciality.name)
    db.add(db_speciality)
    db.commit()
    db.refresh(db_speciality)
    return db_speciality


@router.get("/", response_model=list[SpecialityResponse])
def get_specialities(skip: int = 0,
                     limit: int = 100,
                     db: Session = Depends(get_db)):
    db_specialities = db.query(Speciality).offset(skip).limit(limit).all()
    return db_specialities


@router.get("/{speciality_id}", response_model=SpecialityResponse)
def get_speciality(speciality_id: int, db: Session = Depends(get_db)):
    db_speciality = db.query(Speciality).filter(Speciality.id == speciality_id).first()
    if db_speciality is None:
        raise HTTPException(status_code=404, detail="Speciality not found")
    return db_speciality


@router.put("/{speciality_id}", response_model=SpecialityResponse)
def update_speciality(speciality_id: int,
                      speciality: SpecialityCreate,
                      db: Session = Depends(get_db),
                      current_user=Depends(require_role("admin"))):
    db_speciality = db.query(Speciality).filter(Speciality.id == speciality_id).first()
    if db_speciality is None:
        raise HTTPException(status_code=404, detail="Speciality not found")

    db_speciality.name = speciality.name
    db.commit()
    db.refresh(db_speciality)
    return db_speciality


@router.delete("/{speciality_id}", response_model=SpecialityResponse)
def delete_speciality(speciality_id: int,
                      db: Session = Depends(get_db),
                      current_user=Depends(require_role("admin"))):
    db_speciality = db.query(Speciality).filter(Speciality.id == speciality_id).first()
    if db_speciality is None:
        raise HTTPException(status_code=404, detail="Speciality not found")

    db.delete(db_speciality)
    db.commit()
    return db_speciality
