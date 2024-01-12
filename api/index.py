

from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import models
from db import engine
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")
app.include_router(router)


# @app.get("/api/healthchecker")
# def healthchecker():
#     return {"status": "success", "message": "Integrate FastAPI Framework with Next.js"}

# app.add_middleware(CORSMiddleware, 
#                     allow_origins=["*"],
#                     allow_credentials=True,
#                     allow_methods=["*"],
#                     allow_headers=["*"] )


# class TodoCreate(BaseModel):
#     title:str

# class TodoUpdate(BaseModel):
#     title: Union[str , None] = None
#     completed : Union[bool , None] = None

# class TodoItem(BaseModel):
#     id : str
#     title : str
#     completed : bool

# class TodoItem(BaseModel):
#     id : str
#     title : str
#     completed : bool

# todos = []

# @app.post("/api/todos")
# async def create_todo_item(todo: TodoCreate):
#     new_todo = TodoItem(id=len(todos)+1, title=todo.title, completed=False)
#     todos.append(new_todo)
#     return new_todo

# @app.get("/api/todos")
# async def get_all_todo():
#     return todos

# @app.get("/api/todos/{todo_id}")
# async def get_todo_item(todo_id : int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return todo
#     return {"error":"todo item is not found"}

# @app.patch("/api/todos/{todo_id}")
# def update_todo_item(todo_id :int , todo: TodoUpdate):
#     for todo_item in todos:
#         if todo.id == todo_id:
#             todo_item.title = todo.title if todo.title is not None else todo_item.title
#             todo_item.completed = todo.completed if todo.completed is not None else todo_item.completed
#             return todo_item
#     return {"error":"todo item is not found "}

# @app.delete("/api/todos/{todo_id}")
# def delete_todo_item(todo_id: int ):
    # for i, todo_item in enumerate(todos):
    #     if todo_item.id == todo_id:
    #         del todos[i]
    #         return {"message":"todo item is deleted"}
    # return {"error":"Todo item is not found "}