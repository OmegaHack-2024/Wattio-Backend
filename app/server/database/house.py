from bson.objectid import ObjectId
from .config import database

house_collection = database.get_collection("houses_collection")


def house_helper(house) -> dict:
    return {
        "id": str(house["_id"]),
        "address": house["address"],
        "house_type": house["house_type"],
        "number_of_rooms": house["number_of_rooms"],
    }


async def retrieve_houses():
    houses = []
    async for house in house_collection.find():
        houses.append(house_helper(house))
    return houses


async def add_house(house_data: dict) -> dict:
    house = await house_collection.insert_one(house_data)
    new_house = await house_collection.find_one({"_id": house.inserted_id})
    return house_helper(new_house)


async def retrieve_house(id: str) -> dict:
    house = await house_collection.find_one({"_id": ObjectId(id)})
    if house:
        return house_helper(house)


async def update_house(id: str, data: dict):
    if len(data) < 1:
        return False
    house = await house_collection.find_one({"_id": ObjectId(id)})
    if house:
        updated_house = await house_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_house:
            return True
        return False


async def delete_house(id: str):
    house = await house_collection.find_one({"_id": ObjectId(id)})
    if house:
        await house_collection.delete_one({"_id": ObjectId(id)})
        return True
    

