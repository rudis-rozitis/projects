#from typing import Union

from fastapi import FastAPI, HTTPException
from models.task import Task
import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return HTMLResponse("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="/style.css">
  <title>Task Manager</title>
</head>
<body>
  <h1>TASK MANAGER</h1>

    <form class="input-area">
      <input type="text" placeholder="Input a task.." />
      <button type="submit">ADD</button>
    </form>

    <div class="task-list">

      <div class="task">
        <div class="task-info">
          <span class="date">Created: MM-DD-YYYY</span>
          <span>Task1</span>
        </div>
        <button>Done</button>
      </div>

      <div class="task">
        <div class="task-info">
          <span class="date">Created: MM-DD-YYYY</span>
          <span>Task2</span>
        </div>
        <button>Done</button>
      </div>

      <div class="task">
        <div class="task-info">
          <span class="date">Created: MM-DD-YYYY</span>
          <span>Task3</span>
        </div>
        <button>Done</button>
      </div>

      <div class="task">
        <div class="task-info">
          <span class="date">Created: MM-DD-YYYY</span>
          <span>Task4</span>
        </div>
        <button>Done</button>
      </div>

    </div>
</body>
</html>
""")


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