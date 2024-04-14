from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    house_id: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jane.doe@wattio.com",
                "password": "securepassword",
                "house_id": "123"
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    house_id: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Jane M. Doe",
                "email": "jane.doe@wattio.com",
                "password": "newpassword",
                "house_id": "123"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
