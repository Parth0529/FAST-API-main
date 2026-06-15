from fastapi import FastAPI
from pydantic import BaseModel      
app = FastAPI()

todos = []       #temporary in memory database
class Todo(BaseModel):
    id: int
    title: str
    completed: bool 


@app.post("/todos/")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "todo added",
        "data": todo
    }

@app.get("/todos/")
def get_all_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_single_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "todo not found"}


@app.put ("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo): 
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "data updated",
                "data": updated_todo
            }
    return {"error": "todo not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "todo deleted"}
    return {"error": "todo not found"}