from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies import require_role
from app.models import Net
from app.schemas.net import NetCreate, NetResponseFull
from app.schemas.net_pallete import NetPalleteResponse

router = APIRouter(prefix="/nets", tags=["nets"])


@router.post("/", response_model=NetResponseFull)
def create_net(net: NetCreate,
               db: Session = Depends(get_db),
               current_user = Depends(require_role("teacher"))):
    db_net = Net(**net.dict())
    db.add(db_net)
    db.commit()
    db.refresh(db_net)
    return NetResponseFull.from_orm(db_net)


@router.get("/", response_model=list[NetResponseFull])
def get_nets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_nets = db.query(Net).offset(skip).limit(limit).all()
    return [NetResponseFull.from_orm(net) for net in db_nets]


@router.get("/{net_id}", response_model=NetResponseFull)
def get_net(net_id: int, db: Session = Depends(get_db)):
    db_net = db.query(Net).filter(Net.id == net_id).first()
    if db_net is None:
        raise HTTPException(status_code=404, detail="Net not found")
    return NetResponseFull.from_orm(db_net)


@router.put("/{net_id}", response_model=NetResponseFull)
def update_net(net_id: int,
               net: NetCreate,
               db: Session = Depends(get_db),
               current_user = Depends(require_role("teacher"))):
    db_net = db.query(Net).filter(Net.id == net_id).first()
    if db_net is None:
        raise HTTPException(status_code=404, detail="Net not found")

    for key, value in net.dict(exclude_unset=True).items():
        setattr(db_net, key, value)
    db.commit()
    db.refresh(db_net)
    return NetResponseFull.from_orm(db_net)


@router.delete("/{net_id}", response_model=NetResponseFull)
def delete_net(net_id: int,
               db: Session = Depends(get_db),
               current_user = Depends(require_role("teacher"))):
    db_net = db.query(Net).filter(Net.id == net_id).first()
    if db_net is None:
        raise HTTPException(status_code=404, detail="Net not found")
    db.delete(db_net)
    db.commit()
    return NetResponseFull.from_orm(db_net)
