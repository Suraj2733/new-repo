from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import starlette.responses as _responses


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

todos =[]
class Course(BaseModel):
    id : int
    todo : str

users =[]
class UserData(BaseModel):
    id : int
    username : str

@app.get("/")
async def check_root()->dict:
    return _responses.RedirectResponse("/docs")

@app.get("/use", tags=['users'])
async def root_name()->dict:
    return {"data" : users}


@app.post("/use", tags=["users"])
def add_user(user:UserData) -> dict:
    users.append(user.dict())
    return users[-1]

   

@app.get("/todo", tags=['todos'])
async def root()->dict:
    return {"data" : todos}


@app.post("/todo", tags=["todos"])
def add_todo(todo:Course) -> dict:
    todos.append(todo.dict())
    return todos[-1]


#------------------------------------------------


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {"data": f"Todo with id {id} has been removed."}

    return {"data": f"Todo with id {id} not found."}




