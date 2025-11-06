CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
);"""
INSERT_SAMPLE_TASKS_QUERY = """INSERT INTO tasks (title, description) VALUES
    ('Do the laundry', 'Wash, dry, and fold clothes'),
    ('Clean the kitchen', 'Wash dishes, wipe counters, and mop the floor'),
    ('Grocery shopping', 'Buy vegetables, fruits, and other essentials'),
    ('Take out the trash', 'Collect and dispose of household garbage'),
    ('Vacuum the living room', 'Vacuum carpets and clean under furniture');"""
SELECT_ALL_TASKS_QUERY = "SELECT * FROM tasks;"
SELECT_TASK_BY_ID_QUERY = "SELECT * FROM tasks WHERE id = ?;"
INSERT_TASK_QUERY = "INSERT INTO tasks (title, description) VALUES (?, ?);"
DELETE_TASK_BY_ID_QUERY = "DELETE FROM tasks WHERE id = ?;"
UPDATE_TASK_BY_ID_QUERY = "UPDATE tasks SET title = ?, description = ? WHERE id = ?;"