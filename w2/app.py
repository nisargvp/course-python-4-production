
from fastapi import FastAPI

app = FastAPI()

# minimal app - get request
@app.get("/", tags=['ROOT'])
async def hello_world():
    return {"message": "Welcome to Root of `Python for Production`"}


@app.get("/welcome", tags=['WELCOME'])
async def hello_world():
    return {"message": "Welcome to `Python for Production`"}

# Get --> Read Todo
@app.get("/todo", tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}


# Post --> Create Todo
@app.post("/todo", tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "todo has been added!"
    }


# Put --> Update Todo
@ app.put("/todo/{id}", tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["Activity"] = body["Activity"]
            return {
                "data": f"todo with id {id} has been updated!"
            }
    return {
        "data": f"todo with id {id} not found!"
    }

# Delete --> Delete Todo
@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo_by_id(id:int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"todo with id {id} has been deleted!"
            }
    return {
        "data": f"todo with id {id} not found!"
    }


todos = [
    {
        "id": 1, 
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": 2,
        "Activity": "Writing 3 pages pf my new book at 2:00 PM."
    }
]