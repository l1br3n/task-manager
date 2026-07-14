import sqlite3
import time
from DataBase.database import create_tables, get_task, get_all_tasks, add_task, delete_task, update_task
from DataBase.functions import delete_task_by_id, get_all, get_task_by_id, input_values, update_task_by_id


def main():
    choise = input("Виберіть дію:\n1. Додати завдання\n2. Отримати всі завдання\n3. Отримати завдання за ID\n4. Оновити завдання за ID\n5. Видалити завдання за ID\nВаш вибір: ")
    
    if choise == "1":
       input_values()

    elif choise == "2":
        get_all()

    elif choise == "3":
        get_task_by_id()

    elif choise == "4":
        update_task_by_id()

    elif choise == "5":
        delete_task_by_id()
    
while True:
    main()
    time.sleep(1)