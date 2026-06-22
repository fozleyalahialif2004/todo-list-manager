"""
To-Do List Manager
A simple program to manage tasks with add, view, complete, and delete functionality.
Tasks are saved to a file so they persist between program runs.
"""

# Function to display the main menu
def display_menu():
    """Display the main menu options to the user"""
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Quit")
    print("===============================")

# Function to load tasks from a file
def load_tasks():
    """
    Load tasks from tasks.txt file
    Returns a list of task dictionaries
    Each task has keys: 'description' and 'status'
    """
    task_list = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                # Remove newline character and split by comma
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    if len(parts) == 2:
                        description = parts[0]
                        status = parts[1]
                        task_list.append({"description": description, "status": status})
    except FileNotFoundError:
        # If file doesn't exist, just return empty list
        print("No existing tasks found. Starting fresh!")
    return task_list

# Function to save tasks to a file
def save_tasks(task_list):
    """
    Save all tasks to tasks.txt file
    Each line stores: description,status
    """
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(task["description"] + "," + task["status"] + "\n")

# Function to add a new task
def add_task(task_list):
    """
    Get task description from user and add to task list
    New tasks start with status "Incomplete"
    """
    description = input("Enter task description: ").strip()
    if description:  # Make sure description is not empty
        new_task = {"description": description, "status": "Incomplete"}
        task_list.append(new_task)
        save_tasks(task_list)
        print("Task added successfully!")
    else:
        print("Task description cannot be empty!")

# Function to view all tasks
def view_tasks(task_list):
    """
    Display all tasks with their numbers and status
    [ ] = Incomplete, [x] = Complete
    """
    if not task_list:
        print("\nNo tasks found!")
        return
    
    print("\nYour Tasks:")
    print("-----------")
    for i, task in enumerate(task_list, start=1):
        # Determine the status symbol
        if task["status"] == "Complete":
            status_symbol = "[x]"
        else:
            status_symbol = "[ ]"
        print(f"{i}. {status_symbol} {task['description']}")

# Function to mark a task as complete
def mark_complete(task_list):
    """
    Display tasks, ask user which one to mark complete,
    and update its status
    """
    view_tasks(task_list)
    if not task_list:
        return
    
    try:
        task_num = int(input("\nEnter task number to mark complete: "))
        if 1 <= task_num <= len(task_list):
            task_list[task_num - 1]["status"] = "Complete"
            save_tasks(task_list)
            print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to delete a task
def delete_task(task_list):
    """
    Display tasks, ask user which one to delete,
    and remove it from the list
    """
    view_tasks(task_list)
    if not task_list:
        return
    
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(task_list):
            removed_task = task_list.pop(task_num - 1)
            save_tasks(task_list)
            print(f"Task '{removed_task['description']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program function
def main():
    """
    Main program loop that runs the to-do list manager
    """
    # Load existing tasks from file
    task_list = load_tasks()
    
    running = True
    print("Welcome to the To-Do List Manager!")
    
    # Main program loop
    while running:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            mark_complete(task_list)
        elif choice == "4":
            delete_task(task_list)
        elif choice == "5":
            # Save before quitting
            save_tasks(task_list)
            running = False
            print("\nGoodbye! Your tasks have been saved.")
        else:
            print("Invalid choice! Please enter a number from 1 to 5.")

# Run the program
if __name__ == "__main__":
    main()