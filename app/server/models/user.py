from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    house_id: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@wattio.com",
                "password": "securepassword",
                "house_id": "661bc0d2cdf7b602ac9902cc",
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    house_id: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "john M. Doe",
                "email": "john.doe@wattio.com",
                "password": "newpassword",
                "house_id": "661bc0d2cdf7b602ac9902cc",
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
