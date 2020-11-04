from fastapi import APIRouter
from datetime import datetime

from ..models.pydantic.user import User, UserCreateIn, UserUpdateIn
router = APIRouter()

@router.get("/users/{id}", tags=["Users"], response_model=User)
async def retrieve_user(id: int):
    return {
        "status" : "success",
        "id": 1,
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "name": "something",
        "email": "hello@email.com",
        "phone_number": "01234232122",
        "country_code": 123
    }
