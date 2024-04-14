from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class HouseLogSchema(BaseModel):
    house_id: int = Field(..., description="The ID of the house this log belongs to")
    timestamp: datetime = Field(..., description="The exact time the data was recorded")
    powerConsumption: float = Field(..., description="The amount of wattage used at the recorded time")

    class Config:
        schema_extra = {
            "example": {
                "house_id": 1,
                "timestamp": "2023-04-04T14:00:00",
                "powerConsumption": 350.5,
            }
        }

class UpdateHouseLogModel(BaseModel):
    powerConsumption: Optional[float] = Field(None, description="The amount of wattage used at the recorded time")

    class Config:
        schema_extra = {
            "example": {
                "powerConsumption": 345.2,
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
