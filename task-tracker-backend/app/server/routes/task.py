from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import *
from app.server.models.taskschema import (
    ErrorResponseModel,
    ResponseModel,
    TaskSchema,
    UpdateTask,
)

router = APIRouter()


@router.post("/", response_description="Task data added into DB")
async def create_task(task: TaskSchema = Body(...)):
    task = jsonable_encoder(task)
    new_task = await add_task(task)
    return ResponseModel(new_task, "Task created successfully")


@router.get("/", response_description="Get all tasks")
async def get_all_tasks():
    tasks = await retrieve_tasks()
    if tasks:
        return ResponseModel(tasks, "Tasks data retrieved successfully")
    return ResponseModel(tasks, "Tasks list is empty")


@router.get("/{id}", response_description="Get task by id")
async def get_task_by_id(id: str):
    task = await retrieve_task(id)
    if task:
        return ResponseModel(task, "Task data retrieved successfully")
    return ErrorResponseModel("An Error occurred", 404, "Task does not exist")


@router.put("/{id}")
async def update_task_by_id(id: str, req: UpdateTask = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_task = await update_task(id, req)
    if updated_task:
        return ResponseModel(
            updated_task, "Task updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the task data"
    )


@router.delete("/{id}", response_description="Delete task from Database")
async def remove_task(id: str):
    deleted_task = await delete_task(id)
    if deleted_task:
        return ResponseModel(f"Task with Id {id} is removed", "Task Deleted Successfully")
    return ErrorResponseModel(
        "An error occurred",
        404,
        f"Task with id {id} does not exist"
    )

