def main():
    tasks = []  # List to store tasks

    while True:  # Use the correct capitalization for True
        print("\n======= TO-DO LIST =======")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task As Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Add tasks
            print()
            try:
                n_tasks = int(input("How many tasks do you want to add? "))
                for i in range(n_tasks):
                    task = input(f"Enter task {i + 1}: ")
                    tasks.append({"task": task, "done": False})
                    print("Task added!")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '2':  # Show tasks
            print("\nTasks:")
            if not tasks:
                print("No tasks available!")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':  # Mark a task as done
            if not tasks:
                print("No tasks available to mark as done.")
            else:
                try:
                    task_index = int(input("Enter the task number to mark as done: ")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '4':  # Exit the program
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
