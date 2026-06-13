from datetime import datetime

def validate_task_title(title):
    if len(title) < 2:
        raise ValueError("Title must be at least 2 characters long.")
    return True
    
def validate_task_description(description):
    if not description:
        raise TypeError("Description can't be empty") 
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date)
        return True
    except TypeError:
        raise TypeError("Enter correct date")
