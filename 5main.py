from fastapi import FastAPI
from sympy import limit

app = FastAPI()

@app.get("/items")
def get_items(price: int):
    return {"price": price}