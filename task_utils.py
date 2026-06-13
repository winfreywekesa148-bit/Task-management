# Import validation functions
from task_manager.validation import validate_task_title,validate_task_description,validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task():
    title = input("Enter title: ")
    description = input("Enter description: ")
    due_date = input("Enter due_date: ")

    task = {
        "title": "Groceries",
        "description": "Shop at Market Basket for food", 
        "due_date": "2024-06-26",
        "completed": True
    }

    tasks.append(task)

    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete():
    index = int(input("Enter index: ")) - 1

    if 0 <= index < len(tasks):
        tasks[index] ["completed"] = True
        print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    None

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    None
    return calculate_progress