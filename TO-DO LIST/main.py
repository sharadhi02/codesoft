print("welcome to To Do list app:")
tasks = []
while True:
    print("\nEnter the following options:")
    print("1.Show Tasks")
    print("2.Add Task")
    print("3.Delete Task")
    print("4.Quit")
    choice = input("Enter your choice:")
    if choice=='1':
        if not tasks:
            print("No tasks")
        else:
            print("Your Tasks:")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
    elif choice=='2':
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added")
    elif choice=='3':
        if not tasks:
            print("No tasks to delete")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            try:
                num = int(input("Enter number of task to delete:"))
                if 1<=num<=len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Deleted task:{removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number")
    elif choice=='4':
        print("Thank you for using To Do List")
        break
    else:
        print("Invalid choice. Please try again")
