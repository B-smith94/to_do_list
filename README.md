# Mini-Project 1: To-Do List

Author: Byron Smith

Date: 8/11/2024

Welcome to the To-Do List application!  Here are the features you can expect to find in this app:

-create a to-do list
-once you finish something on your to-do-list, mark it as complete
-remove tasks from either finished or incomplete task lists
-view the lists of tasks in real time, based on what you have completed and what you still have to do

### Instructions on use: ###

The program will start with a main menu.  It should look like this:

        Welcome to the To-Do List App!

        Menu:
        1. Add a Task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit

The program will then prompt you to select a menu item:

        Please input the menu item you wish to select (1 through 5): |

You must enter a number between 1-5, corresponding with a menu item.  If you input something other than a number that matches a menu item, the program will return an error and allow you to reenter your choice.

Below are explanations of each menu item and how they work within the program:

#### 1. Add a Task ####

If you selected option 1, the program will take you to the Add a Task function. This allows you to add tasks to a list of incompete tasks within the program.
It will ask you to input a task you wish to add:

        Please provide the task you wish to add: |

Whatever you enter will be added to the to-do list you wish to create, labeled Incompete Tasks.  For how to mark tasks as complete, see __4. Mark a Task as Complete__.

You MUST enter only one task. To add more tasks, wait until the next line, in which the program will ask you fi you wish to add another task: 

        Would you like to add another task? (yes/no): |

Entering 'yes' will allow you to add more tasks.  Entering 'no' will display the updated lists and return you to the main menu.  They will appear in the order that you enter them.

#### 2. View Tasks ####

Entering 2 on the main menu will prompt the program to take you to the View Tasks function. This will show the most recent version of both the Incomplete Tasks list and the Finished Tasks list:

        --Incomplete tasks: []
        --Finished tasks: []

Once this is done, the program will return to the main menu.

#### 3. Mark Tasks as Complete ####

Option 3 will take you to Mark Tasks as Complete. This will transfer items that you select from the Incomplete Tasks list to a list of Finished Tasks, helping you keep track of what you've already done and what you still have left to do.

__NOTE:__   In order to use this function, ***you must have items in the list of incomplete tasks.*** If there are no items, the program will return to the main menu, displying this message:

        No tasks in the list yet.

If there are tasks in the to-do list already, then the program will prompt you to enter in the tasks you wish to mark complete: 

        Enter the task you wish to mark complete: |

If you enter an item not on the list of incomplete tasks, the program will give an error message and prompt you to enter a task again.

Once you enter a task to mark complete, the program will ask if you wish to enter in another task:

        Would you like to mark another task? (yes/no): |

You MUST enter the full word, 'yes' or 'no'. The program will prompt you to reenter your answer if you put in anything else.

If you enter 'yes', the program will allow you to enter in another task to complete.  If you enter 'no', the program will display the updated lists as previously shown, and return to the main menu.

#### 4. Delete a Task ####

The 4th option will allow you to remove items from either list.

__NOTE:__ In order to use this function, ***you must have items in at least one of the lists, either Finished Tasks or Incomplete Tasks.*** If you do not, the program will return you to the main menu after displaying the following message: 

        No tasks on either list.

If you have items on at least one of the two previously mentioned lists, the program will ask you which list you would like to remove a task from:

        Which list would you like to edit? (incomplete/finished): |

At this point, you must enter either 'incomplete' or 'finished', and it will take you to the next line, which asks you to input the item you wish to remove:

        Please input the task you wish to remove from incomplete tasks: |

                            OR

        Plese input the task you wish to remove from finished tasks: |

If the selected list is already empty, the program will display the following message:

        No items in this list.

Once you enter in an item from the list, the program will ask if you wish to remove another task:

        Would you like to remove another task? (yes/no): |

Entering 'yes' will prompt you to select a list to edit, as before. Entering 'no' will display the edited lists and take you back to the main menu.

#### 5. Quit ####

Entering 5 on the main menu will display the following message:

        Thank you for using To-Do List app!  Have a wonderful day!

The program will then end.