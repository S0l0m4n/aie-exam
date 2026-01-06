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
    age: Optional[int]
    sex: Optional[Sex]
    heart_rate: Optional[int]
    vo2_max: Optional[int]

MY_HEALTH = Health(name='John Smith', age=23, sex=Sex.MALE, heart_rate=80,
        vo2_max=50)

# GET: retrieve health information
@app.get("/health")
def get_health():
    return MY_HEALTH

# POST: update all health stats
@app.post("/health")
def update_health(health: Health):
    # name is required
    MY_HEALTH.name = health.name
    if health.age is not None:
        MY_HEALTH.age = health.age
    if health.sex is not None:
        MY_HEALTH.sex = health.sex
    if health.heart_rate is not None:
        MY_HEALTH.heart_rate = health.heart_rate
    if health.vo2_max is not None:
        MY_HEALTH.vo2_max = health.vo2_max
    return {"message": "Updated info successfully", "health": MY_HEALTH}

# POST: update heart rate
@app.post("/heart_rate")
def update_heart_rate(heart_rate: int):
    MY_HEALTH.heart_rate = heart_rate
