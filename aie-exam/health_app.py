#!/bin/python3
# A simple FastAPI server for returning health information

from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Sex(Enum):
    MALE = 'male'
    FEMALE = 'female'

# health model
class Health(BaseModel):
    name: str
    age: int | None = None
    sex: Sex | None = None
    heart_rate: int | None = None
    vo2_max: int | None = None

MY_HEALTH = Health(name='John Smith', age=23, sex=Sex.MALE, heart_rate=80,
        vo2_max=50)

# GET: retrieve health information
@app.get("/health")
def get_health():
    return MY_HEALTH

# POST: update all health stats
@app.post("/health")
def update_health(health: Health):
    health_fields = health.model_dump()
    for k,v in health_fields.items():
        # health object is not a dict, so we need to use setattr
        setattr(MY_HEALTH, k, v)
    return {"message": "Updated info successfully", "health": MY_HEALTH}

# POST: update heart rate
@app.post("/heart_rate")
def update_heart_rate(heart_rate: int):
    MY_HEALTH.heart_rate = heart_rate
