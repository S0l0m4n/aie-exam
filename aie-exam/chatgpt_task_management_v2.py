from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()
tasks: List[Task] = []
next_id = 1

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None

class Task(TaskCreate):
    id: int
    completed: bool = False

# Create a task
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task( id=next_id, title=task.title, description=task.description, completed=False)
    tasks.append(new_task)
    next_id += 1
    return new_task

# List all tasks
@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks

# Get a single task
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Update a task (full update)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated: TaskCreate):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            new_task = Task( id=task_id, title=updated.title, description=updated.description, completed=task.completed)
            tasks[i] = new_task
            return new_task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return

    raise HTTPException(status_code=404, detail="Task not found")

# Home
@app.get("/")
def home():
    return {"message": "Welcome to my task management API! Go to /docs for the interactive UI."}
