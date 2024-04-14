from bson.objectid import ObjectId
from .config import database

house_log_collection = database.get_collection("house_logs_collection")


def house_log_helper(house_log) -> dict:
    return {
        "id": str(house_log["_id"]),
        "house_id": house_log["house_id"],
        "timestamp": house_log["timestamp"],
        "powerConsumption": house_log["powerConsumption"],
    }


async def retrieve_house_logs():
    house_logs = []
    async for house_log in house_log_collection.find():
        house_logs.append(house_log_helper(house_log))
    return house_logs


async def add_house_log(house_log_data: dict) -> dict:
    house_log = await house_log_collection.insert_one(house_log_data)
    new_house_log = await house_log_collection.find_one({"_id": house_log.inserted_id})
    return house_log_helper(new_house_log)


async def retrieve_house_log(id: str) -> dict:
    house_log = await house_log_collection.find_one({"_id": ObjectId(id)})
    if house_log:
        return house_log_helper(house_log)


async def update_house_log(id: str, data: dict):
    if len(data) < 1:
        return False
    house_log = await house_log_collection.find_one({"_id": ObjectId(id)})
    if house_log:
        updated_house_log = await house_log_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_house_log:
            return True
        return False


async def delete_house_log(id: str):
    house_log = await house_log_collection.find_one({"_id": ObjectId(id)})
    if house_log:
        await house_log_collection.delete_one({"_id": ObjectId(id)})
        return True
