from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies import require_role
from app.models import Group
from app.schemas.group import GroupCreate, GroupResponse

router = APIRouter(prefix="/groups", tags=["groups"])

@router.post("/", response_model=GroupResponse)
def create_group(group: GroupCreate,
                 db: Session = Depends(get_db),
                 current_user = Depends(require_role("admin"))):
    db_group = Group(name=group.name, speciality_id=group.speciality_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@router.get("/", response_model=list[GroupResponse])
def get_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_groups = db.query(Group).offset(skip).limit(limit).all()
    return db_groups

@router.get("/{group_id}", response_model=GroupResponse)
def get_group(group_id: int, db: Session = Depends(get_db)):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@router.put("/{group_id}", response_model=GroupResponse)
def update_group(group_id: int,
                 group: GroupCreate,
                 db: Session = Depends(get_db),
                 current_user = Depends(require_role("admin"))):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    db_group.name = group.name
    db_group.speciality_id = group.speciality_id
    db.commit()
    db.refresh(db_group)
    return db_group

@router.delete("/{group_id}", response_model=GroupResponse)
def delete_group(group_id: int,
                 db: Session = Depends(get_db),
                 current_user = Depends(require_role("admin"))):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    db.delete(db_group)
    db.commit()
    return db_group
