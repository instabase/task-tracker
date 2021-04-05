from typing import Optional

from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    id: Optional[str]
    text: str = Field(...)
    day: str
    reminder: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "text": "Grocery Shopping",
                "day": "March 4th",
                "reminder": True,
            }
        }


class UpdateTask(BaseModel):
    id: Optional[str]
    text: Optional[str]
    day: Optional[str]
    reminder: Optional[bool]


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
