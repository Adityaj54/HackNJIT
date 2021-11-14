from fastapi import FastAPI
from . import models
from .database import engine
from .routes import jobs,users,auth
import azure.functions as func
from .http_asgi import AsgiMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"HELLO": "Welcome"}

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)