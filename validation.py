from datetime import datetime

def validate_task_title(title):
    if len(title) < 2:
        raise ValueError("Title must be at least 2 characters long.")
    return True
    
def validate_task_description(description):
    if len(description) > 500:
        raise TypeError("Reduce the number of character") 
    return True
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date)
        return True
    except TypeError:
        raise TypeError("Enter correct date")
