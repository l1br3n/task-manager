from DataBase.database import add_task, delete_task, get_all_tasks, get_task, update_task

def input_values():
    a = input("Введіть кількість завдань:")
    for i in range(int(a)):
        name = input(f"Введіть назву завдання {i + 1}: ")
        description = input(f"Введіть опис завдання {i + 1}: ")
        due_date = input(f"Введіть термін виконання завдання {i + 1}: ")
        status = input(f"Введіть статус завдання {i + 1} (True/False): ")
        add_task(None, name, description, due_date, status)

def get_all():
    tasks = get_all_tasks()
    for task in tasks:
        print(task)

def get_task_by_id():
    r = input("\nОтримати завдання з ID:")
    task = get_task(int(r))
    print(task)

def update_task_by_id():
    name = input("Введіть нову назву завдання: ")
    description = input("Введіть новий опис завдання: ")
    due_date = input("Введіть новий термін виконання завдання: ")
    status = input("Введіть новий статус завдання (True/False): ")
    update_task(None, name, description, due_date, status)

def delete_task_by_id():
    task_id = int(input("\nВведіть ID завдання для видалення: "))
    delete_task(task_id)
    print(f"Завдання з ID {task_id} було видалено.")