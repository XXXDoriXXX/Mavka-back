from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from sqlalchemy.orm import Session

from app.models import User
from app.schemas.user import UserSignup
from app.utils.jwt import create_access_token
from app.utils.security import verify_password, hash_password
from app.dependencies import get_current_user, require_role
from app.db.session import get_db


ACCESS_TOKEN_EXPIRE_MINUTES = 600

router = APIRouter(prefix="/auth", tags=["auth"])
"""users = {
    "admin": {
        "username": "admin",
        "full_name": "Admin User",
        "hashed_password": "$2b$12$s.4NKCQHLFn4DkiM43ZyHOGSLvVAb5nff9fHO8udNT2UIroLX9Vyq",  # adminpass
        "role": "admin",
    },
    "user": {
        "username": "user",
        "full_name": "Regular User",
        "hashed_password": "$2b$12$WHlf0zuqgLVsBsiY.Sjk6u4s6p/aIbpL6HA6fLua9oLn3F5JCkndK",  # userpass
        "role": "user",
    }
}"""

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter_by(username=username).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(
        {"id": user.id, "sub": user.username, "role": str(user.role)},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": token, "token_type": "bearer"}

@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        password_hash=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        group_id=user.group_id,
        role=user.role,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully", "username": new_user.username}

@router.get("/me")
def read_me(current_user = Depends(get_current_user)):
    return {"user": current_user}

@router.get("/admin")
def admin_only(current_user = Depends(require_role("ADMIN"))):
    return {"message": "Welcome admin!"}
