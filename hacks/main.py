from fastapi import FastAPI
from . import models
from .database import engine
from .routes import jobs,users,auth
from fastapi.middleware.cors import CORSMiddleware



models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(jobs.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"HELLO": "Welcome"}

