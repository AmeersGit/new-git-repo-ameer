import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
    except:
        print("Invalid input.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1.Show 2.Add 3.Delete 4.Exit")
        choice = input("Choose: ")
        if choice == "1": show_tasks(tasks)
        elif choice == "2": add_task(tasks)
        elif choice == "3": delete_task(tasks)
        elif choice == "4": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
