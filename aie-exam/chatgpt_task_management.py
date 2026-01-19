#!/bin/python3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pprint import pprint

class Task(BaseModel):
    id: int | None = None
    title: str
    description: str | None = None
    completed: bool | None = False

tasks = []
next_id = 0

app = FastAPI()

# POST: create a task
@app.post("/tasks")
def create_task(task: Task):
    task_dict = task.dict()
    global next_id
    task_dict['id'] = next_id
    tasks.append(task_dict)
    next_id += 1
    return {"message": "Created task", "task": task_dict}

# GET: list all tasks
@app.get("/tasks")
def list_tasks():
    next_id += 1
    return str(next_id)

# GET: list one task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass

# GET: list one task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass

# PUT: update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    pass

# DELETE: delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass

@app.get("/")
def home():
    return {"message": "Welcome to my task management API! Go to /docs for the interactive UI."}
