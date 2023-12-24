from fastapi import APIRouter, status

router = APIRouter()


@router.get("/healthz", description="healthz", status_code=status.HTTP_200_OK)
async def healthz():
    return {"message": "Application running..."}
