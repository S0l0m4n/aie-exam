#!/bin/python3
# A simple FastAPI server for returning health information

from enum import Enum
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

ERROR_NOT_FOUND = "Health record not found"

class Sex(Enum):
    MALE = 'male'
    FEMALE = 'female'

# health model
class Health(BaseModel):
    id: int
    name: str
    age: int | None = None
    sex: Sex | None = None
    heart_rate: int | None = None
    vo2_max: int | None = None

db = {
        1: Health(id=1, name='John Smith', age=23, sex=Sex.MALE, heart_rate=80, vo2_max=50),
        2: Health(id=2, name='Frank Carr', age=37, sex=Sex.MALE, heart_rate=101, vo2_max=34),
        3: Health(id=3, name='Susan Maye', age=30, sex=Sex.FEMALE, heart_rate=78, vo2_max=39),
}

app = FastAPI()

# GET: retrieve health information
@app.get("/health/{id}")
def get_health(id: int):
    result = db.get(id)
    if result is None:
        raise HTTPException(status_code=404, detail=ERROR_NOT_FOUND)

# POST: update all health stats
@app.post("/health/{id}")
def update_health(health: Health, id: int):
    if id in db:
        # exclude_unset to ignore empty values
        # excluding "id" ignores whatever value it might be set to, preserving
        # the object's id value
        health_fields = health.model_dump(exclude_unset=True, exclude={"id"})
        for k,v in health_fields.items():
            # health object is not a dict, so we need to use setattr
            setattr(db[id], k, v)
        return {"message": "Updated info successfully", "health": db[id]}
    else:
        raise HTTPException(status_code=404, detail=ERROR_NOT_FOUND)

# POST: update heart rate
@app.post("/heart_rate/{id}")
def update_heart_rate(id: int, heart_rate: int = Body()):
    try:
        db[id].heart_rate = heart_rate
        return db[id]
    except KeyError:
        raise HTTPException(status_code=404, detail=ERROR_NOT_FOUND)
