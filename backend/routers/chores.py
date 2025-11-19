from fastapi import APIRouter

router = APIRouter(
    prefix="/chores",
    tags=["chores"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_chores():
    return {"chores": []}
