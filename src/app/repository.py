import logging

from src.logicinit import config
from src.app.db.core import connect_db

from .dependencies import queries_db

from .models import IncidentRespModel, IncidentBaseModel


settings = config.get_settings()
logger = logging.getLogger(__name__)


class IncidentRepo:

    async def get_incident_by_status(self, status) -> IncidentRespModel:
        """ Получение инцидентов по статусу"""

        async with connect_db.connection() as conn:
            incidents = await queries_db.select_incident_by_status(conn, status=status)
            return incidents

    async def create_incident(self, incident_data: IncidentBaseModel) -> IncidentRespModel:
        """ Создание инцидента"""
        async with connect_db.connection() as conn:
            incidents = await queries_db.insert_incident(
                conn,
                description=incident_data.description,
                status=incident_data.status,
                source=incident_data.source,
                create_dt=incident_data.create_dt
            )
            return incidents

    async def update_incident(self, incident_id: int, status: str) -> IncidentRespModel:
        """ Изменение статуса инцидента"""
        async with connect_db.connection() as conn:
            incidents = await queries_db.update_incident(
                conn,
                incident_id=incident_id,
                status=status,
            )
            return incidents
