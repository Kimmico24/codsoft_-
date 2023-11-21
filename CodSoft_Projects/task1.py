import os

# Define a list to store tasks
tasks = []


# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Function to add a task to the to-do list
def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


# Function to update a task
def update_task():
    display_tasks()
    task_num = int(input("Enter the task number you want to update: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_num] = new_task
        print(f"Task {task_num + 1} updated.")
    else:
        print("Invalid task number.")


# Function to remove a task
def remove_task():
    display_tasks()
    task_num = int(input("Enter the task number you want to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task number.")


# Main loop for the to-do list application
while True:
    print("\nTo-Do List Application")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# Save the to-do list to a file
with open("todo_list.txt", "w") as file:
    file.writelines('\n'.join(tasks))

