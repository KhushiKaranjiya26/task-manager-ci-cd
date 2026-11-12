
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task Manager API",
    description="A CI/CD practice project",
    version="1.0.0"
)

# Temporary in-memory storage
tasks = {}

# Request data validation
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Task Manager API"}


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# Create a task
@app.post("/tasks", status_code=201)
def create_task(task: Task):

    task_id = len(tasks) + 1

    tasks[task_id] = task.model_dump()

    return {
        "message": "Task created successfully",
        "task_id": task_id,
        "task": tasks[task_id]
    }


# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Get a specific task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


# Update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    tasks[task_id] = task.model_dump()

    return {
        "message": "Task updated successfully",
        "task": tasks[task_id]
    }


# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[task_id]

    return {"message": "Task deleted successfully"}
