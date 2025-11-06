from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Добро пожаловать в моё FastAPI-приложение!"}

@app.get("/user/{username}")
def greet_user(username: str):
    return {"message": f"Привет, {username}!"}
