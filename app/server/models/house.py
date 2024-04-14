from pydantic import BaseModel, Field
from typing import Optional

class HouseSchema(BaseModel):
    owner_id: Optional[int] = Field(None, description="The user ID of the house owner")
    address: str = Field(..., description="The full address of the house")
    house_type: str = Field(..., description="Type of house (e.g., apartment, detached)")
    number_of_rooms: int = Field(..., description="Number of rooms in the house")

    class Config:
        schema_extra = {
            "example": {
                "owner_id": 1,
                "address": "1234 Main St, Anytown, AT 12345",
                "house_type": "Detached",
                "number_of_rooms": 5,
            }
        }

class UpdateHouseModel(BaseModel):
    address: Optional[str] = Field(None, description="The full address of the house")
    house_type: Optional[str] = Field(None, description="Type of house (e.g., apartment, detached)")
    number_of_rooms: Optional[int] = Field(None, description="Number of rooms in the house")

    class Config:
        schema_extra = {
            "example": {
                "address": "1234 Main St, Anytown, AT 12345",
                "house_type": "Detached",
                "number_of_rooms": 6,
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
