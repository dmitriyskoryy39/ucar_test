from fastapi import APIRouter


router = APIRouter()


@router.get(
    path="/incident/",
    summary="Получить список инцидентов (с фильтром по статусу)",
)
async def get_incident(
):
    return {"ok": "ok"}
