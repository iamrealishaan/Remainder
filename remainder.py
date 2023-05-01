import datetime

tasks = {}

def add_task(task, due_date):
    tasks[task] = due_date

def check_reminders():
    today = datetime.date.today()
    for task, due_date in tasks.items():
        if due_date == today:
            print("Reminder: You need to do", task)

# Example usage:
add_task("Buy milk", datetime.date(2023, 5, 3))
add_task("Pay bills", datetime.date(2023, 5, 4))
check_reminders()
