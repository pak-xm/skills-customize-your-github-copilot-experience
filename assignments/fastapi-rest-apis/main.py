"""
FastAPI Task Management API - Starter Code

This is a template for building a REST API with FastAPI. 
Students will implement the routes and business logic.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# TODO: Define a Task model using Pydantic
# This should have: id (int), title (str), description (str), completed (bool)


# TODO: Create an in-memory list to store tasks
# tasks = []


@app.get("/")
def read_root():
    """
    TODO: Implement the root route
    Should return a welcome message for the API
    """
    pass


@app.get("/tasks")
def get_tasks(completed: Optional[bool] = None):
    """
    TODO: Implement the get tasks route
    Should return all tasks, or filter by completed status if provided
    """
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """
    TODO: Implement the get single task route
    Should return a specific task by its ID
    If task not found, raise an HTTPException with status 404
    """
    pass


@app.post("/tasks", status_code=201)
def create_task(task: "Task"):
    """
    TODO: Implement the create task route
    Should accept a Task object and add it to the list
    Return the newly created task with its assigned ID
    """
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: "Task"):
    """
    TODO: Implement the update task route
    Should update an existing task by its ID
    If task not found, raise an HTTPException with status 404
    """
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    TODO: Implement the delete task route
    Should remove a task by its ID
    If task not found, raise an HTTPException with status 404
    Return a confirmation message
    """
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
