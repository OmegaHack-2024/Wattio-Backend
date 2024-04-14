from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from server.database.house_log import (
    add_house_log,
    delete_house_log,
    retrieve_house_log,
    retrieve_house_logs,
    update_house_log,
    get_logs_by_house_id
)

from server.models.house_log import (
    ErrorResponseModel,
    ResponseModel,
    HouseLogSchema,
    UpdateHouseLogModel,
)
from server.dependencies import get_current_user

router = APIRouter()


@router.post("/", response_description="HouseLog data added into the database")
async def add_house_log_data(
    house_log: HouseLogSchema = Body(...),
    current_user: dict = Depends(get_current_user),
):
    house_log = jsonable_encoder(house_log)
    new_house_log = await add_house_log(house_log)
    return ResponseModel(new_house_log, "HouseLog added successfully.")


@router.get("/", response_description="HouseLogs retrieved")
async def get_house_logs(current_user: dict = Depends(get_current_user)):
    # You can access the current_user if needed, or just keep it in Depends() for protection
    house_logs = await retrieve_house_logs()
    if house_logs:
        return ResponseModel(house_logs, "HouseLogs data retrieved successfully")
    return ResponseModel(house_logs, "Empty list returned")


@router.get("/{id}", response_description="HouseLog data retrieved")
async def get_house_log_data(id: str, current_user: dict = Depends(get_current_user)):
    house_log = await retrieve_house_log(id)
    if house_log:
        return ResponseModel(house_log, "HouseLog data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "HouseLog doesn't exist.")


@router.put("/{id}", response_description="HouseLog data updated in the database")
async def update_house_log_data(
    id: str,
    req: UpdateHouseLogModel = Body(...),
    current_user: dict = Depends(get_current_user),
):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_house_log = await update_house_log(id, req)
    if updated_house_log:
        return ResponseModel(
            "HouseLog with ID: {} update is successful".format(id),
            "HouseLog data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the house_log data.",
    )


@router.delete("/{id}", response_description="HouseLog data deleted from the database")
async def delete_house_log_data(
    id: str, current_user: dict = Depends(get_current_user)
):
    deleted_house_log = await delete_house_log(id)
    if deleted_house_log:
        return ResponseModel(
            "HouseLog with ID: {} removed".format(id), "HouseLog deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "HouseLog with id {0} doesn't exist".format(id)
    )

@router.get("/logs/{house_id}", response_description="Get all logs from a house")
async def get_logs(house_id: str):
    logs = await get_logs_by_house_id(house_id)
    if not logs:
        return ResponseModel([], "No logs found for the provided house_id.")

    return ResponseModel(logs, "Logs retrieved successfully.")