import sqlite3

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            due_date TEXT,
            hours_per_day INTEGER,
            status BOOLEAN
        )
    ''')
    conn.commit() 
    conn.close()  


def get_connection():
    return sqlite3.connect('tasks.db')


def get_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE task_id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(task_id, name, description, due_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task_id, name, description, due_date, status) VALUES (?, ?, ?, ?, ?)', (task_id, name, description, due_date, status))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, name, description, due_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET name = ?, description = ?, due_date = ?, status = ? WHERE task_id = ?', (name, description, due_date, status, task_id))
    conn.commit()
    conn.close()

create_tables()