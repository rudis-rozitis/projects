#from typing import Union

from fastapi import FastAPI
from models.task import Task
import sqlite3

app = FastAPI()

sqliteConnection = sqlite3.connect('task_db.db')

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/task")
def read_item(task: Task):
    #TODO: implement litesql database insert here
    #Returns created task with an ID
    return { "id": 1, "title": "Task Title", "description": "Task Description", "status": "pending" }

@app.get("/tasks")
def get_all_tasks():
    #TODO: implement litesql database fetch all here
    #Responds with JSON array of task objects
    all_tasks = []
    return all_tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    #TODO: implement litesql database fetch a task here
    #TODO: return 404 if task not found
    #Returns JSON object of the task
    return {"Here": "be task details"}

@app.put("/tasks")
def update_task(task: Task):
    #TODO: implement litesql database fetch a task here
    #TODO: return 404 if task not found
    #Returns JSON object of updated task
    return {"Here": "be task details"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    #TODO: implement litesql database delete a task here
    #Returns a status code
    return 200