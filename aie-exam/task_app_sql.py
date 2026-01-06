#!/bin/python3
# A task app using a real SQLite DB 

from enum import Enum
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import Optional

DB_FILE = "task_data.db"

ERROR_NOT_FOUND = "Record not found"

class Task(BaseModel):
    id: int
    name: str
    latency: int | None = None

# connect to the database file (creates it if it doesn't exist)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# create the table with raw SQL
cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            latency INTEGER
        )
""")
conn.commit()

# dummy database using a list
db = {
        1: Task(id=1, name="Task 1"),
        2: Task(id=2, name="Task 2"),
}

# FastAPI server
app = FastAPI()

# POST: post task data
@app.post("/assist")
def post_task(task: Task):
    db[task.id] = task
    return db[task.id]

# GET: return tasks
@app.get("/runs")
def get_tasks():
    return [ db[i].name for i in db ]
