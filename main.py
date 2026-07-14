import sqlite3
import time

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY,
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

def main():
    choise = input("Виберіть дію:\n1. Додати завдання\n2. Отримати всі завдання\n3. Отримати завдання за ID\n4. Оновити завдання за ID\n5. Видалити завдання за ID\nВаш вибір: ")
    if choise == "1":
        a = input("Введіть кількість завдань:")
        for i in range(int(a)):
            task_id = i + 1
            name = input(f"Введіть назву завдання {task_id}: ")
            description = input(f"Введіть опис завдання {task_id}: ")
        due_date = input(f"Введіть термін виконання завдання {task_id}: ")
        status = input(f"Введіть статус завдання {task_id} (True/False): ")
        add_task(task_id, name, description, due_date, status)

    elif choise == "2":
        tasks = get_all_tasks()
        for task in tasks:
            print(task)

    elif choise == "3":
        r = input("\nОтримати завдання з ID:")
        task = get_task(int(r))
        print(task)

    elif choise == "4":
        task_id = int(input("\nВведіть ID завдання для оновлення: "))
        name = input("Введіть нову назву завдання: ")
        description = input("Введіть новий опис завдання: ")
        due_date = input("Введіть новий термін виконання завдання: ")
        status = input("Введіть новий статус завдання (True/False): ")
        update_task(task_id, name, description, due_date, status)

    elif choise == "5":
        task_id = int(input("\nВведіть ID завдання для видалення: "))
        delete_task(task_id)
        print(f"Завдання з ID {task_id} було видалено.")

    
while True:
    main()
    time.sleep(1)