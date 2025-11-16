#from typing import Union

from fastapi import FastAPI, HTTPException, Request, Response, Form
from models.task import Task
import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    tasks = db.get_all_tasks()
    return templates.TemplateResponse(name="index.html", request=request, context={"tasks": tasks["tasks"]})

@app.post("/task")
def insert_item(task: str = Form(...)):
    print(task)
    inserted_item = db.insert_task(task)
    html_response = f"""
    <li id="task-{inserted_item['id']}">
      <div class="task">
        <div class="task-info">
          <span class="date">Task ID: {inserted_item['id']} </span>
          <span>{inserted_item['title']}</span>
        </div>
        <button  hx-target="closest ul" hx-swap="innerHTML" hx-delete="/tasks/{inserted_item['id']}">Done</button>
      </div>
    </li>
    """
    return HTMLResponse(content=html_response)

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
    task = db.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete_task_by_id(task_id)
    html_response = ""
    for task in db.get_all_tasks()["tasks"]:
      html_response += f"""
      <li id="task-{task['id']}" >
        <div class="task">
          <div class="task-info">
            <span class="date">Task ID: {task['id']} </span>
            <span>{task['title']}</span>
          </div>
          <button hx-target="closest ul" hx-swap="innerHTML" hx-delete="/tasks/{task['id']}">Done</button>
        </div>
      </li>
      """
    return HTMLResponse(content=html_response)

@app.post("/populate_tasks")
def populate_tasks():
    db.populate_tasks()
    return 200