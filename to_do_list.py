menu = ["Add a task", "view tasks", "Mark a task as complete", "Delete a task", "Quit"]

incomplete_tasks = []
finished_tasks = []   

def add_task(task_list):
    while True:
        new_task = input("Please provide the task you wish to add: ")
        incomplete_tasks.append(new_task)
        while True:
            more_new_task = input("Would you like to add another task? (yes/no): ")
            if more_new_task.lower() == 'yes':
                break
            elif more_new_task.lower() == 'no':
                print(f"\nTo do list: {incomplete_tasks}") 
                break
            else:
                print("invalid input, please try again.")
                continue
        if more_new_task.lower() == 'yes':
            continue
        else:
            break

def view_tasks(task_list_1, task_list_2):
    print(f"\n--Incomplete tasks: {incomplete_tasks}")
    print(f"--Finished tasks: {finished_tasks}")
    

def complete_tasks(task_list):
    while True:
        completed_task = input("Enter the task you wish to mark as complete: ")
        if completed_task in incomplete_tasks:
            if completed_task not in finished_tasks:
                finished_tasks.append(completed_task)
                incomplete_tasks.remove(completed_task)
            else:
                print("This task is already marked as complete.")
        else:
            print("Task not found.")
        while True:
            more_complete = input("Would you like to mark another task? (yes/no): ")
            if more_complete.lower() == 'yes':
                break
            elif more_complete.lower() == 'no':
                print(f"\nFinished Tasks: {finished_tasks}\nIncomplete Tasks: {complete_tasks}")
                break
            else:
                print("Invalid input, please try again.")
                continue
        if more_complete.lower() == 'yes':
            continue
        else:
            break
def delete_tasks(task_list_1, task_list_2):
    pass

def quit():
    print("\nThank you for using the To-Do List app! Have a wonderful day!\n")
    

while True:    
    print("\nWelcome to the To-Do List App!\n\nMenu:\n")
    for number in menu:
        index = str(menu.index(number) + 1) + '.'
        choices = index + ' ' + number
        print(choices)
        
    try:
        choice = int(input("\nPlease input the menu item number you wish to select (1 through 5): "))
    except ValueError:
        print("Error: Invalid input, please enter an integer (example: 5).")
    else:
        if choice == 1:
            add_task(incomplete_tasks)
        elif choice == 2:
            view_tasks(incomplete_tasks, finished_tasks)
        elif choice == 3:
            complete_tasks(incomplete_tasks)
        elif choice == 4:
            delete_tasks(incomplete_tasks, finished_tasks)
        else:
            quit()
            break
        
        
