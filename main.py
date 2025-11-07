
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.logicinit import config
from src.app import endpoints
from src.app.db.core import connect_db

settings = config.get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await connect_db.connect()
        print('start app')
        yield
    finally:
        await connect_db.disconnect()
        print("stop app")

app = FastAPI(lifespan=lifespan)
app.include_router(endpoints.router)

