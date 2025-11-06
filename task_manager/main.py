#from typing import Union

from fastapi import FastAPI, HTTPException
from models.task import Task
import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/task")
def insert_item(task: Task):
    return db.insert_task(task)

@app.get("/tasks")
def get_all_tasks():
    json_compatible_item_data = jsonable_encoder(db.get_all_tasks())
    return JSONResponse(content=json_compatible_item_data)

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = db.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        json_compatible_item_data = jsonable_encoder(task)
        return JSONResponse(content=json_compatible_item_data)

@app.put("/tasks")
def update_task(task: Task):
    task = db.update_task_by_id(task)
    if task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        json_compatible_item_data = jsonable_encoder(task)
        return JSONResponse(content=json_compatible_item_data)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db.delete_task_by_id(task_id)
    return 200

@app.post("/populate_tasks")
def populate_tasks():
    db.populate_tasks()

    return 200