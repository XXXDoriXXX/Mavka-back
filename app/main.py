from fastapi import FastAPI

from app.routers import auth, groups, specialities

app = FastAPI()

app.include_router(auth.router)
app.include_router(groups.router)
app.include_router(specialities.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
