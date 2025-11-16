import sqlite3
from models.task import Task
from queries import (
    CREATE_TABLE_QUERY,
    INSERT_SAMPLE_TASKS_QUERY,  
    SELECT_ALL_TASKS_QUERY,
    SELECT_TASK_BY_ID_QUERY,
    INSERT_TASK_QUERY,
    DELETE_TASK_BY_ID_QUERY,
    UPDATE_TASK_BY_ID_QUERY
)
# Constants
DB_NAME = 'task_db.db'


# Helper function for database connection
def get_db_connection():
    """Establish and return a database connection."""
    return sqlite3.connect(DB_NAME)

# Database Initialization
def populate_tasks():
    """
    Creates the tasks table if it doesn't exist and populates it with sample data.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        cursor.execute(INSERT_SAMPLE_TASKS_QUERY)
        conn.commit()
        cursor.close()
    print("Tasks populated successfully")

# CRUD Operations
def get_all_tasks():
    """
    Fetch all tasks from the database.
    Returns:
        dict: A dictionary containing a list of all tasks.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_ALL_TASKS_QUERY)
        records = cursor.fetchall()
        cursor.close()
    tasks = [{"id": record[0], "title": record[1], "description": record[2]} for record in records]
    return {"tasks": tasks}

def insert_task(task: str):
    """
    Insert a new task into the database.
    Args:
        task (Task): The task object to insert.
    Returns:
        dict: The inserted task with its generated ID.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_TASK_QUERY, (task, "Placeholder description"))
        task_id = cursor.lastrowid
        conn.commit()
        cursor.close()
    return {"id": task_id, "title": task, "description": "Placeholder description"}

def get_task_by_id(task_id: int):
    """
    Fetch a task by its ID.
    Args:
        task_id (int): The ID of the task to fetch.
    Returns:
        dict | None: The task if found, otherwise None.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_TASK_BY_ID_QUERY, (task_id,))
        record = cursor.fetchone()
        cursor.close()
    if record:
        return {"id": record[0], "title": record[1], "description": record[2]}
    return None

def delete_task_by_id(task_id: int):
    """
    Delete a task by its ID.
    Args:
        task_id (int): The ID of the task to delete.
    Returns:
        int: HTTP status code 200 if successful.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE_TASK_BY_ID_QUERY, (task_id,))
        conn.commit()
        cursor.close()
    return 200

def update_task_by_id(task: Task):
    """
    Update a task by its ID.
    Args:
        task (Task): The task object with updated data.
    Returns:
        dict | None: The updated task if successful, otherwise None.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_TASK_BY_ID_QUERY, (task.id,))
        record = cursor.fetchone()
        if record is None:
            cursor.close()
            return None
        cursor.execute(UPDATE_TASK_BY_ID_QUERY, (task.title, task.description, task.id))
        conn.commit()
        cursor.close()
    return {"id": task.id, "title": task.title, "description": task.description}