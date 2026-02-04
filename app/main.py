from fastapi import FastAPI
from contextlib import asynccontextmanager
from app import auth, models
from app.db import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    models.Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
