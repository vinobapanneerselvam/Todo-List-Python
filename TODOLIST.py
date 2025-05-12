
tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")
    
    elif choice == '2':
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            status = "done" if t["done"] else "not done"
            print(f"{i+1}. [{status}] {t['task']}")
    
    elif choice == '3':
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    
    elif choice == '4':
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            deleted = tasks.pop(num)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    
    elif choice == '5':
        print("Exiting To-Do List. Bye!")
        break
    
    else:
        print("Invalid choice. Try again.")
