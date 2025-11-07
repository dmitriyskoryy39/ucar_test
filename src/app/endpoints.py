from fastapi import APIRouter, Query


from .models import IncidentModel, IncidentStatus

router = APIRouter()


@router.get(
    path="/incident/",
    summary="Получить список инцидентов (с фильтром по статусу)",
    # response_model=IncidentModel
)
async def get_incident(
    status: IncidentStatus = Query(description="Статус инцидента")
):
    return {"ok": status}


