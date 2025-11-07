
import asyncpg
from contextlib import asynccontextmanager
from pathlib import Path

import aiosql

from .models import IncidentRespModel
from src.logicinit import config

settings = config.get_settings()


queries_db = aiosql.from_path(
    sql_path=Path(__file__).parent / "db.sql",
    driver_adapter="asyncpg",
    record_classes={
        "IncidentRespModel": IncidentRespModel,
    },
)


@asynccontextmanager
async def pool_conn_db():
    pool = await asyncpg.create_pool(
        database=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        min_size=5,
        max_size=10
    )
    try:
        yield pool
    finally:
        await pool.close()

