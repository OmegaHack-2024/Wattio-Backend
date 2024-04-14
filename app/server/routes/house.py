from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from server.database.house import (
    add_house,
    delete_house,
    retrieve_house,
    retrieve_houses,
    update_house,
)

from server.models.house import (
    ErrorResponseModel,
    ResponseModel,
    HouseSchema,
    UpdateHouseModel,
)
from server.dependencies import get_current_user

router = APIRouter()


@router.post("/", response_description="House data added into the database")
async def add_house_data(house: HouseSchema = Body(...), current_user: dict = Depends(get_current_user)):
    house = jsonable_encoder(house)
    new_house = await add_house(house)
    return ResponseModel(new_house, "House added successfully.")


@router.get("/", response_description="Houses retrieved")
async def get_houses(current_user: dict = Depends(get_current_user)):
    # You can access the current_user if needed, or just keep it in Depends() for protection
    houses = await retrieve_houses()
    if houses:
        return ResponseModel(houses, "Houses data retrieved successfully")
    return ResponseModel(houses, "Empty list returned")


@router.get("/{id}", response_description="House data retrieved")
async def get_house_data(id: str, current_user: dict = Depends(get_current_user)):
    house = await retrieve_house(id)
    if house:
        return ResponseModel(house, "House data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "House doesn't exist.")


@router.put("/{id}", response_description="House data updated in the database")
async def update_house_data(id: str, req: UpdateHouseModel = Body(...), current_user: dict = Depends(get_current_user)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_house = await update_house(id, req)
    if updated_house:
        return ResponseModel(
            "House with ID: {} update is successful".format(id),
            "House data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the house data.",
    )


@router.delete("/{id}", response_description="House data deleted from the database")
async def delete_house_data(id: str, current_user: dict = Depends(get_current_user)):
    deleted_house = await delete_house(id)
    if deleted_house:
        return ResponseModel(
            "House with ID: {} removed".format(id),
            "House deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "House with id {0} doesn't exist".format(
            id)
    )
