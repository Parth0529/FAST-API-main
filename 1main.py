from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome FastAPI"}

@app.get("/about")
def about():
    return {"message": "This is a about ecommmerce website"}

@app.get("/contact")
def contact():
    return {"message": "This is the contact page"}

@app.get("/products")
def products():
    return {"message": "This is the products page"}

@app.get("/services")
def services():
    return {"message": "This is the services page"}