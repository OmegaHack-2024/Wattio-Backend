from fastapi import APIRouter, Body, Depends, HTTPException
from server.database.redeemable import (
    add_redeemable,
    retrieve_redeemables,
    retrieve_redeemable,
    update_redeemable,
    delete_redeemable,
)
from server.models.redeemable import RedeemableSchema, ResponseModel, ErrorResponseModel
from server.dependencies import get_current_user

router = APIRouter()


@router.post("/", response_description="Redeemable data added into the database")
async def add_redeemable_data(redeemable: RedeemableSchema = Body(...), current_user: dict = Depends(get_current_user)):
    redeemable = await add_redeemable(redeemable.dict())
    return ResponseModel(redeemable, "Redeemable added successfully.")


@router.get("/", response_description="Redeemables retrieved")
async def get_redeemables(current_user: dict = Depends(get_current_user)):
    redeemables = await retrieve_redeemables()
    if redeemables:
        return ResponseModel(redeemables, "Redeemables retrieved successfully.")
    return ResponseModel(redeemables, "No redeemables found.")


@router.get("/{id}", response_description="Redeemable data retrieved")
async def get_redeemable_data(id: str, current_user: dict = Depends(get_current_user)):
    redeemable = await retrieve_redeemable(id)
    if redeemable:
        return ResponseModel(redeemable, "Redeemable retrieved successfully.")
    return ErrorResponseModel("An error occurred.", 404, "Redeemable doesn't exist.")


@router.put("/{id}", response_description="Redeemable data updated in the database")
async def update_redeemable_data(id: str, redeemable: RedeemableSchema = Body(...), current_user: dict = Depends(get_current_user)):
    updated_redeemable = await update_redeemable(id, redeemable.dict())
    if updated_redeemable:
        return ResponseModel(updated_redeemable, "Redeemable updated successfully.")
    return ErrorResponseModel("An error occurred", 404, "Updating redeemable failed.")


@router.delete("/{id}", response_description="Redeemable data deleted from the database")
async def delete_redeemable_data(id: str, current_user: dict = Depends(get_current_user)):
    deleted_redeemable = await delete_redeemable(id)
    if deleted_redeemable:
        return ResponseModel(str(id), "Redeemable deleted successfully.")
    return ErrorResponseModel("An error occurred", 404, "Redeemable not found.")
