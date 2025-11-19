from fastapi import APIRouter

router = APIRouter(
    prefix="/meals",
    tags=["meals"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_meals():
    return {"meals": []}
