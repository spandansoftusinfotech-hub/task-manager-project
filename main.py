from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FILE_NAME = "tasks.json"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


@app.get("/")
def home():
    return {"message": "Task Manager API Running"}


@app.get("/tasks")
def get_tasks():
    with open(FILE_NAME, "r") as f:
        return json.load(f)


@app.post("/tasks/{task}")
def add_task(task: str):
    with open(FILE_NAME, "r") as f:
        tasks = json.load(f)

    tasks.append(task)

    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

    return {
        "message": "Task Added",
        "task": task
    }
print("Hello"
      