
from pathlib import Path

import aiosql

from .models import IncidentRespModel
from src.logicinit import config

settings = config.get_settings()


queries_db = aiosql.from_path(
    sql_path=Path(__file__).parent / "db" / "db.sql",
    driver_adapter="asyncpg",
    record_classes={
        "IncidentRespModel": IncidentRespModel,
    },
)