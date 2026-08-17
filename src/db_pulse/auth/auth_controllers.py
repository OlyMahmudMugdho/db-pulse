from fastapi import APIRouter

from db_pulse.auth.register_request import RegisterRequest

router = APIRouter()


@router.post("/register")
async def register(request: RegisterRequest):
    print(request)
    return request
