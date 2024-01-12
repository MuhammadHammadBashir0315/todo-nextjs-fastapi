from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class TaskSchema(BaseModel):
    id : Optional[int] = None
    title : Optional[str] = None
    description : Optional[str] = None

    class db:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestTask(BaseModel):
    parameter: TaskSchema = Field(...)
    
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]