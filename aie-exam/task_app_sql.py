#!/bin/python3
# A task assistant app using a real SQLite DB. Assistant can execute a number of
# simple commands. Input and output are stored as a JSON object, along with
# execution latency. APIs are made available to run tasks and fetch the history
# of calls.
#
# Possible tasks:
#   - uppercase: Convert string to uppercase
#   - reverse: Reverse the string
#   - word_count: Count the number of words in the string

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import time

DB_FILE = "task_data.db"

app = FastAPI(title="Task assistant API")

# --- DATABASE SETUP ---
def init_db():
    # connect to the database file (creates it if it doesn't exist)
    with sqlite3.connect(DB_FILE) as conn:
        # create the table with raw SQL
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                input TEXT NOT NULL,
                output TEXT NOT NULL,
                latency_ms INTEGER NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

init_db()

# --- SCHEMAS ---
class AssistRequest(BaseModel):
    task: str
    input: str

class AssistResponse(BaseModel):
    task: str
    output: str
    latency_ms: int

# --- TASK LOGIC ---
def run_task(task: str, input_text: str) -> str:
    if task == "uppercase":
        return input_text.upper()
    elif task == "reverse":
        return "".join(reversed(input_text))
    elif task == "word_count":
        # convert result to string as schema expects it
        return str(len(input_text.split()))
    else:
        raise ValueError("Unsupported task")

# --- ROUTES ---
@app.post("/assist", response_model=AssistResponse)
def assist(req: AssistRequest):
    start = time.perf_counter()

    try:
        output = run_task(req.task, req.input)
    except ValueError as e:
        # bad input
        raise HTTPException(status_code=400, detail=str(e))

    latency_ms = int((time.perf_counter() - start) * 1000)

    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "INSERT INTO tasks (task, input, output, latency_ms) \
                    VALUES (?, ?, ?, ?)",
            (req.task, req.input, output, latency_ms)
        )
    return { "task": req.task, "output": output, "latency_ms": latency_ms }
# NOTE: the response model ensures the returned output is conforming

@app.get("/runs")
def get_runs():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    return [ dict(row) for row in rows ]
