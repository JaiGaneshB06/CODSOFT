tasks = []
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
def update_task():
    view_tasks()
    if len(tasks) > 0:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[task_no - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
def delete_task():
    view_tasks()
    if len(tasks) > 0:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number.")
while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("\nEnter your choice(1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please try again.")