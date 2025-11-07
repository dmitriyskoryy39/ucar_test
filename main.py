from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.logicinit import config
from src.app import endpoints

settings = config.get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('start app')
    yield
    print("stop app")


app = FastAPI(lifespan=lifespan)
app.include_router(endpoints.router)

