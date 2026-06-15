from fastapi import FastAPI
app = FastAPI()

@app.post("/create_user")
def create_user(name: str, age: int, college: str, semester: int):
    return{
        "message": "user created ",
        "data": {
            "name": name,
            "age": age,
            "college": college,
            "semester": semester
        }
    }