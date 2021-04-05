import motor.motor_asyncio
from bson.objectid import ObjectId
from pymongo import ReturnDocument

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.tasks
task_collection = database.get_collection("task_collection")


def task_parser(task) -> dict:
    return {
        "id": str(task["_id"]),
        "text": task["text"],
        "day": task["day"],
        "reminder": bool(task["reminder"])
    }


async def retrieve_tasks():
    tasks = []
    async for task in task_collection.find():
        tasks.append(task_parser(task))
    return tasks


async def retrieve_task(id: str) -> dict:
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        return task_parser(task)


async def add_task(task_data: dict) -> dict:
    task = await task_collection.insert_one(task_data)
    new_task = await task_collection.find_one({"_id": task.inserted_id})
    return task_parser(new_task)


async def update_task(id: str, data: dict):
    if len(data) < 1:
        return None
    updated_task = await task_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": data}, return_document=ReturnDocument.AFTER
    )
    return task_parser(updated_task)


async def delete_task(id: str):
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        await task_collection.delete_one({"_id": ObjectId(id)})
        return True
