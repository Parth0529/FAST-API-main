from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    address: address    

#create the route
@app.post("/create_user/")
def create_user(user: User):
    return user
