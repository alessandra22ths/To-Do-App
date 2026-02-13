def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_name, priority, done = line.strip().split("|")
                tasks.append({
                    "task": task_name,
                    "priority": priority,
                    "done": done == "True"
                })
    except FileNotFoundError:
        pass
    return tasks

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['priority']}|{task['done']}\n")

tasks = load_tasks()

print("To-Do List")

while True:
    print("\nMenu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Task name: ")
        priority = input("Priority (High / Medium / Low): ")

        task = {
            "task": task_name,
            "priority": priority,
            "done": False
        }

        tasks.append(task)
        save_tasks()
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Pending"
                print(f"{index}. {task['task']} | Priority: {task['priority']} | Status: {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']}")

            task_number = int(input("Enter task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["done"] = True
                save_tasks()
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
