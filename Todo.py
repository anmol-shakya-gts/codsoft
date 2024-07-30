""" A To-Do-List application is a useful project that helps users manage and organize their tasks efficiently.
   This project aimas to create a comman-line or GUI base application using Python, allowing user to create,
    update, and track their to-do-lists.
    1. add_tasks
    2. view_task
    3.delete_task
    4.Quit   """

tasks = []
# add a new task to the to-do list.
def add_task():
    task = (input("Enter a new tasks:"))
    tasks.append(task)
    print("Tasks Added Successfully:")
    
# View the task in the do-do list.1
def view_tasks():
    if len(tasks) == 0:
        print("No tasks:")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
    
# Delete a task from the to-do list.
def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete:")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input("Enter the tasks number to delete:"))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task Deleted Successfully:")
        else:
            print("Invalid your task number:")

    # Run the command line to-do list application.
def main():
    while True:
        print("\n***** To-Do-List Application: *****")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Quit")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the To-Do-List Application:")
            break
        else:
            print("Invalid choice. Please try again:")

if __name__ == "__main__":
    main()