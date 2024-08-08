menu = ["Add a task", "view tasks", "Mark a task as complete", "Delete a task", "Quit"]


to_do_list = []    

def add_task(task_list):
    while True:
        new_task = input("Please provide the task you wish to add: ")
        to_do_list.append(new_task)
        while True:
            more_new_task = input("Would you like to add another task? (yes/no): ")
            if more_new_task.lower() == 'yes':
                break
            elif more_new_task.lower() == 'no':
                print(f"To do list: {to_do_list}") 
                break
            else:
                print("invalid input, please try again.")
                continue
        if more_new_task.lower() == 'yes':
            continue
        else:
            break
def view_tasks(task_list):
    print(f"\nTo-Do List: \n{to_do_list}\n")

def complete_tasks(task_list):
    pass
def delete_tasks(task_list):
    while True:
        try:
            remove_task = input("Please provide the task you wish to remove: ")
            to_do_list.remove(remove_task)
        except ValueError:
            print("Item is not on the list, please try again.")
            break
        else:
            while True:
                remove_more_task = input("Would you like to remove another task? (yes/no): ")
                if remove_more_task.lower() == 'yes':
                    break
                elif remove_more_task.lower() == 'no':
                    print(f"To do list: {to_do_list}") 
                    break
                else:
                    print("invalid input, please try again.")
                    continue
            if remove_more_task.lower() == 'yes':
                continue
            else:
                break

def quit(task_list):
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
            add_task(to_do_list)
        elif choice == 2:
            view_tasks(to_do_list)
        elif choice == 3:
            complete_tasks(to_do_list)
        elif choice == 4:
            delete_tasks(to_do_list)
        else:
            quit(to_do_list)
            break
        
        
