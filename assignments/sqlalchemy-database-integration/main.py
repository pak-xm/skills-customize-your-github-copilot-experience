"""
FastAPI Task Management API with SQLAlchemy - Starter Code

This assignment builds on the previous FastAPI assignment by adding
persistent database storage using SQLAlchemy ORM and SQLite.
"""

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# TODO: Configure SQLAlchemy
# Create engine for SQLite database (use "tasks.db")
# engine = create_engine(...)

# TODO: Create session factory
# SessionLocal = sessionmaker(...)

# TODO: Create declarative base for models
# Base = declarative_base()

app = FastAPI()


# TODO: Define the Task SQLAlchemy model
# This should map to a database table with columns:
# - id (primary key)
# - title (string)
# - description (string, nullable)
# - completed (boolean, default False)
# - created_at (datetime)
class TaskModel:
    """Database model for tasks"""
    pass


# Pydantic models for request/response
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True


# TODO: Create database tables on startup
@app.on_event("startup")
def startup():
    """Initialize the database"""
    pass


# TODO: Dependency to get database session
def get_db():
    """Get database session for request"""
    pass


@app.get("/")
def read_root():
    """Welcome message for the API"""
    return {"message": "Task Management API with Database"}


@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks(db: Session, completed: Optional[bool] = None):
    """
    TODO: Fetch tasks from database
    
    - Query all tasks or filter by completed status if provided
    - Return list of tasks
    """
    pass


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session):
    """
    TODO: Fetch a specific task from database
    
    - Query task by ID
    - Raise HTTPException 404 if not found
    """
    pass


@app.post("/tasks", status_code=201, response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session):
    """
    TODO: Create and save a new task to database
    
    - Create TaskModel instance from request data
    - Add to session and commit
    - Return created task with ID
    """
    pass


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session):
    """
    TODO: Update an existing task in database
    
    - Query task by ID
    - Update fields only if provided
    - Commit changes
    - Raise HTTPException 404 if not found
    """
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session):
    """
    TODO: Delete a task from database
    
    - Query task by ID
    - Delete from session and commit
    - Return confirmation message
    - Raise HTTPException 404 if not found
    """
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
