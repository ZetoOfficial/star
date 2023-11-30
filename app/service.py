import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import api_router
from settings import load_settings

app = FastAPI()

settings = load_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.app.endpoint)

if not os.path.exists(settings.app.static_dir):
    os.makedirs(settings.app.static_dir)

app.mount(
    "/static",
    StaticFiles(directory=settings.app.static_dir),
    name=settings.app.static_dir,
)
