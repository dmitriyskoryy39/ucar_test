
import asyncpg
from contextlib import asynccontextmanager


from src.logicinit import config

settings = config.get_settings()


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
