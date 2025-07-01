from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, Field


#pydantic schemas and validation

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of the dodo')
    todo_description: str = Field(..., description="Description of todo")


class TodoCreate(TodoBase):
    pass 


class Todo(TodoBase):
    todo_id: int = Field(..., description=" unique id of todo") 


class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='Name of the dodo')
    todo_description : Optional[str] = Field(None, description="Description of todo")