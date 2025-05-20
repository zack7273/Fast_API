from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "This is the home page"}

@app.get("/about")
def about():
    return {"message": "This is the about page"}

@app.get("/contact")
def contact():
    return {
        "name": "xyz",
        "email": "xyz@gmail.com",
        "phone": "123456789"
    }


# for dynamic + static path

@app.get("/blog/{user_name}")
def blog_name(user_name: str):
    return {
        "page": "blog",
        "user_name": user_name
    }
