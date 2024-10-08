import pdb

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
                view_tasks(incomplete_tasks, finished_tasks) 
                break
            else:
                print("invalid input, please try again.")
                continue
        if more_new_task.lower() == 'yes':
            continue
        else:
            break

def view_tasks(task_list_1, task_list_2):
    print(f"\n--Incomplete tasks: {task_list_1}")
    print(f"--Finished tasks: {task_list_2}")
    

def complete_tasks(task_list):
    while True:
        if len(task_list) == 0:
            print("\nNo tasks in the list yet.")
            break
        else:
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
                    view_tasks(incomplete_tasks, finished_tasks)
                    break
                else:
                    print("Invalid input, please try again.")
                    continue
            if more_complete.lower() == 'yes':
                continue
            else:
                break

def delete_tasks(task_list_1, task_list_2):
    while True:
        if len(task_list_1 + task_list_2) == 0:
            print("\nNo tasks on either list.")
            break
        else:
            while True:
                task_list = input("Which list would you like to edit? (incomplete/finished): ")
                if task_list.lower() == 'incomplete':
                    if len(task_list_1) == 0:
                        print("No items in this list.")
                        continue
                    else:
                        bad_task = input("Please input the task you wish to remove from incomplete tasks: ")
                        if bad_task in task_list_1:
                            task_list_1.remove(bad_task)
                            print("Task removed.")
                            break
                        else:
                            print("Task not found. Please try again.")
                            continue
                elif task_list.lower() == 'finished':
                    if len(task_list_2) == 0:
                        print("No items in this list.")
                        continue
                    else:
                        bad_task = input("Please input the task you wish to remove from finished tasks: ")
                        if bad_task in task_list_2:
                            task_list_2.remove(bad_task)
                            print("Task removed.")
                            break
                        else:
                            print("Task not found. Please try again.")
                            continue
                else:
                    print("Invalid input, please try again.")
                    continue
            while True:
                new_remove = input("Would you like to remove another task? (yes/no): ")
                if new_remove.lower() != 'yes':
                    if new_remove.lower() == 'no':
                        view_tasks(incomplete_tasks, finished_tasks)
                        break
                    else:
                        print("invalid input, please try again.")
                        continue
                else:
                    break
            if new_remove.lower() == 'yes':
                continue
            else:
                break

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
        elif choice == 5:
            quit()
            break
        else:
            print("Invalid input, please try again")

        
        
