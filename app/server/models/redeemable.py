from pydantic import BaseModel, Field
from typing import Optional


class RedeemableSchema(BaseModel):
    title: str = Field(...)
    points_required: int = Field(...)
    availability: bool = Field(default=True)
    expiry_date: Optional[str] = Field(
        None, regex="^\d{2}-\d{2}-\d{4}$")  # Enforcing a DD-MM-YYYY format
    category: Optional[str]
    image_url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Bono 10.000 Frisby",
                "points_required": 100,
                "availability": True,
                "expiry_date": "31-12-2023",
                "category": "Food",
                "image_url": "http://localhost:8000/static/redeemables/bono-frisby.jpg"
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
