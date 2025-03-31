from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, groups, specialities, nets, schedules, reports

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(groups.router)
app.include_router(specialities.router)
app.include_router(nets.router)
app.include_router(schedules.router)
app.include_router(reports.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
