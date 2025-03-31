from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.utils.jwt import create_access_token
from app.utils.security import verify_password
from app.dependencies import get_current_user, require_role

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/auth", tags=["auth"])

users = {
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
}

def authenticate_user(username: str, password: str):
    user = users.get(username)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(
        {"sub": user["username"], "role": user["role"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def read_me(current_user = Depends(get_current_user)):
    return {"user": current_user}

@router.get("/admin")
def admin_only(current_user = Depends(require_role("admin"))):
    return {"message": "Welcome admin!"}
