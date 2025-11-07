import logging
from fastapi import APIRouter, Query, Body, Path, Depends


from .models import IncidentRespModel, StatusModel, IncidentBaseModel
from .repository import IncidentRepo

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    path="/incident/",
    summary="Получить список инцидентов (с фильтром по статусу)",
    response_model=list[IncidentRespModel]
)
async def get_incident(
    status: StatusModel = Query(description="Статус инцидента"),
    repo: IncidentRepo = Depends(IncidentRepo)
):
    try:
        incidents = await repo.get_incident_by_status(status=status.status)
        return incidents
    except Exception as e:
        logger.error(e)
        raise


@router.post(
    path="/incident/",
    summary="Создать инцидент",
    response_model=IncidentRespModel,
    status_code=201
)
async def get_incident(
    incident_data: IncidentBaseModel = Body(...),
    repo: IncidentRepo = Depends(IncidentRepo)
):
    try:
        incident = await repo.create_incident(incident_data=incident_data)
        return incident
    except Exception as e:
        logger.error(e)


@router.patch(
    path="/incident/{incident_id}",
    summary="Обновить статус инцидента",
    response_model=IncidentRespModel,
    status_code=201
)
async def get_incident(
    incident_id: int = Path(description="Идентификатор инцидента"),
    status: StatusModel = Query(description="Статус инцидента"),
    repo: IncidentRepo = Depends(IncidentRepo)
):
    try:
        incident = await repo.update_incident(incident_id=incident_id, status=status.status)
        return incident
    except Exception as e:
        logger.error(e)
