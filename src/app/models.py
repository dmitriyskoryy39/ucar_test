
from datetime import datetime
from pydantic import BaseModel, Field
from fastapi import Query
from enum import Enum


class IncidentStatus(str, Enum):
    active = "active"
    processing = "processing"
    completed = "completed"


class Sources(str, Enum):
    operator = "operator"
    monitoring = "monitoring"
    partner = "partner"


class StatusModel(BaseModel):
    status: IncidentStatus = Field(Query(description="Статус инцидента"))


class IncidentBaseModel(BaseModel):
    description: str = Field(description="Описание инцидента")
    status: IncidentStatus = Field(description="Статус инцидента")
    source: Sources = Field(description="Источники инцидентов")
    create_dt: datetime = Field(description="Дата и время создания инцидента", default=datetime.now())


class IncidentRespModel(IncidentBaseModel):
    id: int = Field(description="Идентификатор инцидента")

