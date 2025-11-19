from fastapi import APIRouter

router = APIRouter(
    prefix="/calendar",
    tags=["calendar"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_calendar():
    return {"events": []}
