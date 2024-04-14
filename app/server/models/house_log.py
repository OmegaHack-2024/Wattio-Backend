from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class HouseLogSchema(BaseModel):
    house_id: int = Field(..., description="The ID of the house this log belongs to")
    start_time: datetime = Field(..., description="The start time of the aggregation period")
    end_time: datetime = Field(..., description="The end time of the aggregation period")
    average_wattage: float = Field(..., description="The average wattage used during the period")
    total_wattage: float = Field(..., description="The total wattage consumed during the period")

    class Config:
        schema_extra = {
            "example": {
                "house_id": 1,
                "start_time": "2023-04-04T00:00:00",
                "end_time": "2023-04-04T23:59:59",
                "average_wattage": 320.5,
                "total_wattage": 5000.0,
            }
        }

class UpdateHouseLogModel(BaseModel):
    average_wattage: Optional[float] = Field(None, description="The average wattage used during the period")
    total_wattage: Optional[float] = Field(None, description="The total wattage consumed during the period")

    class Config:
        schema_extra = {
            "example": {
                "average_wattage": 325.0,
                "total_wattage": 5100.0,
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
