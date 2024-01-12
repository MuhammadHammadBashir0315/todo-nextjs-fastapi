from fastapi import APIRouter, HTTPException, Path
from fastapi import FastAPI
from fastapi import Depends
from db import SessionLocal
from sqlalchemy.orm import Session
from schemas import TaskSchema, Request, Response, RequestTask
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/todos")
async def create_task_service(request: RequestTask, db: Session = Depends(get_db)):
    crud.create_task(db, task=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="task created successfully").dict(exclude_none=True)

@router.get("/api/todos")
async def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _tasks = crud.get_task(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_tasks)

@router.patch("/api/todos/{todo_id}")
async def update_task(request: RequestTask, db: Session = Depends(get_db)):
    _task = crud.update_task(db, task_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_task)

@router.delete("/api/todos/{todo_id}")
async def delete_task(request: RequestTask,  db: Session = Depends(get_db)):
    crud.remove_task(db, task_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)