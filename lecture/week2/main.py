# =============================================================================
# HogwartsMember
# =============================================================================
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to the Hogwarts School of Witchcraft and Wizardry of class 2023"}

class HogwartsMember(BaseModel):
    name: str
    house: Optional[str] = None
    year: Optional[int] = None

members = [
    {"name": "Harry Potter", "house": "Gryffindor", "year": 5},
    {"name": "Hermione Granger", "house": "Gryffindor", "year": 5},
]

@app.get("/hogwarts/members/{member_id}")
def get_member(member_id: int):
    if 0 <= member_id < len(members):
        return members[member_id]
    return {"error": "Member not found"}

@app.post("/hogwarts/members")
def add_member(member: HogwartsMember):
    members.append(member.dict())
    return {"success": True, "member_id": len(members) - 1}

# =============================================================================
# HogwartsClass
# =============================================================================

class HogwartsClass(BaseModel):
    id: int
    name: str
    professor: str
    description: str

# In-memory storage for Hogwarts classes
classes = {}

@app.get("/welcome")
async def hello_world():
    return {"message": "Welcome to Hogwarts School of Witchcraft and Wizardry"}

@app.get("/classes/{class_id}")
async def get_class(class_id: int):
    return classes.get(class_id, {"message": "Class not found"})

@app.post("/classes/")
async def create_class(hogwarts_class: HogwartsClass):
    classes[hogwarts_class.id] = hogwarts_class
    return {"message": "Class created successfully"}

@app.put("/classes/{class_id}")
async def update_class(class_id: int, hogwarts_class: HogwartsClass):
    if class_id in classes:
        classes[class_id] = hogwarts_class
        return {"message": "Class updated successfully"}
    else:
        return {"message": "Class not found"}

@app.delete("/classes/{class_id}")
async def delete_class(class_id: int):
    if class_id in classes:
        del classes[class_id]
        return {"message": "Class deleted successfully"}
    else:
        return {"message": "Class not found"}

@app.patch("/classes/{class_id}")
async def partial_update_class(class_id: int, name: str = None, professor: str = None, description: str = None):
    if class_id in classes:
        if name is not None:
            classes[class_id].name = name
        if professor is not None:
            classes[class_id].professor = professor
        if description is not None:
            classes[class_id].description = description
        return {"message": "Class partially updated successfully"}
    else:
        return {"message": "Class not found"}