from to_do_list import ToDoList

def main():
    todo = ToDoList()
    
    SEPARATOR = "-----------------------------------------\n"
    
    while True:
        print(SEPARATOR)
        print("Task Tracker Menu")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Filter Tasks by Status")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1": # Adding a Task
            desc = input("Enter task description: ").strip()
            todo.add_task(desc)
            print("Task added!")

        elif choice == "2": # List all Tasks
            todo.pretty_print()

        elif choice == "3": # Change Status of Task (Using ID)
            try:
                task_id = int(input("Enter Task ID: "))
                print("Status options: Pending, In Progress, Done")
                new_status = input("Enter new status: ").strip()
                if todo.update_task_status(task_id, new_status):
                    print("Task updated!")
                else:
                    print("Task not found")
            except ValueError:
                print("Invalid input")

        elif choice == "4": # Delete Task (Using ID)
            try:
                task_id = int(input("Enter Task ID to delete: "))
                if todo.delete_task(task_id):
                    print("Task deleted!")
                else:
                    print("Task not found")
            except ValueError:
                print("Invalid input")

        elif choice == "5": # Filter Tasks (Using Status)
            print("Status options: Pending, In Progress, Done")
            status = input("Enter status to filter by: ").strip()
            try:
                filtered = todo.filter_by_status(status)
                todo.pretty_print(filtered)
            except ValueError:
                print("Invalid status. Use exact match like 'Pending'")

        elif choice == "6": # Exit Program
            print("👋 Exiting. All tasks saved!")
            break

        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
