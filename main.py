from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Добро пожаловать в моё FastAPI! Запуск через Vercel!"}

@app.get("/user/{username}")
def greet_user(username: str):
    return {"message": f"Привет, {username}!"}
