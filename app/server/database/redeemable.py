from bson.objectid import ObjectId
from .config import database

redeemable_collection = database.get_collection("redeemables_collection")


def redeemable_helper(redeemable) -> dict:
    return {
        "id": str(redeemable["_id"]),
        "title": redeemable["title"],
        "points_required": redeemable["points_required"],
        "availability": redeemable["availability"],
        "expiry_date": redeemable.get("expiry_date"),
        "category": redeemable.get("category"),
        "image_url": redeemable.get("image_url"),
    }


async def retrieve_redeemables():
    redeemables = []
    async for redeemable in redeemable_collection.find():
        redeemables.append(redeemable_helper(redeemable))
    return redeemables


async def add_redeemable(redeemable_data: dict) -> dict:
    redeemable = await redeemable_collection.insert_one(redeemable_data)
    new_redeemable = await redeemable_collection.find_one({"_id": redeemable.inserted_id})
    return redeemable_helper(new_redeemable)


async def retrieve_redeemable(id: str) -> dict:
    redeemable = await redeemable_collection.find_one({"_id": ObjectId(id)})
    if redeemable:
        return redeemable_helper(redeemable)


async def update_redeemable(id: str, data: dict):
    redeemable = await redeemable_collection.find_one({"_id": ObjectId(id)})
    if redeemable:
        updated_redeemable = await redeemable_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_redeemable:
            return redeemable_helper(await redeemable_collection.find_one({"_id": ObjectId(id)}))


async def delete_redeemable(id: str):
    redeemable = await redeemable_collection.find_one({"_id": ObjectId(id)})
    if redeemable:
        await redeemable_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
