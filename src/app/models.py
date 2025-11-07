
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class IncidentStatus(Enum):
    ACTIVE = "active"
    PROCESSING = "processing"
    COMPLETED = "completed"


class Sources(Enum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"


class IncidentModel(BaseModel):
    id: int = Field(description="Идентификатор инцидента")
    description: str = Field(description="Описание инцидента")
    status: IncidentStatus = Field(description="Статус инцидента")
    source: Sources = Field(description="Источники инцидентов")
    create_dt: datetime = Field(description="Дата и время создания инцидента", default=datetime.now())
