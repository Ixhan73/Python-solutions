def view_tasks(tasks):
    if tasks:
        print("\nYour tasks:\n")
        for i, task in enumerate(tasks, start=1):
            print('\t',i,task)
        print()
    else:
        print("\nYou don't have any tasks.\n")


def add_task(tasks):
    task_to_add = input("\nEnter the task you want to add: ")
    if task_to_add not in tasks:
        tasks.append(task_to_add)
        print("Task added!\n")
    
    else:
    
        duplicate_task = input("\nThe task already exists, do you want to add it again(y/n): ").lower()
        if duplicate_task == 'y':
            tasks.append(task_to_add)
            print("Task added!\n")
        elif duplicate_task == 'n':
            print("Task not added\n")
        else:
            print("\nInvalid input!\n")


def remove_task(tasks):
    task_to_remove = input("\nEnter the task you want to remove: ")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print("Task removed!\n")
    else:
        print("\nTask doesn't exist!\n")





tasks = []
options = ['1. Add Task', '2. Remove Task', '3. View Tasks', '4. Exit']

print('='*30,'\n\tTO-DO LIST\n'+'='*30)

while True:
    for option in options:
        print(option)
    user_choice = input("\nChoose from 1-4: ")

    if user_choice == '1':
        add_task(tasks)
        

    elif user_choice == '2':   
        remove_task(tasks)
    

    elif user_choice == '3':
       view_tasks(tasks)


    elif user_choice == '4':
        print("\n\tExited")
        break

    else:
        print("\nInvalid input!\n")
        continue