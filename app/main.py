from fastapi import FastAPI
from app.pikparser.router import router

app = FastAPI()

app.include_router(router)