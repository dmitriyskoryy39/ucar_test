
import asyncpg
from contextlib import asynccontextmanager


from src.logicinit import config

settings = config.get_settings()


class ConnectDatabase:
    def __init__(self):
        self.pool = None

    async def connect(self):
        if not self.pool:
            self.pool = await asyncpg.create_pool(
                database=settings.POSTGRES_DB,
                user=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
                host=settings.POSTGRES_HOST,
                port=settings.POSTGRES_PORT,
                min_size=5,
                max_size=10
            )

    async def disconnect(self):
        if self.pool is not None:
            await self.pool.close()

    @asynccontextmanager
    async def connection(self):
        conn = await self.pool.acquire()
        try:
            yield conn
        finally:
            await self.pool.release(conn)


connect_db = ConnectDatabase()

