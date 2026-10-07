tasks = []
while True:
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Remove tasks")
    print("Exist")
    choice = input("choose: ")
if choice == "1":
     task = input("Enter task:")
     tasks.append(task)
     print("Task added")
    
elif choice == "2":
      for nunber, task in enumerate(tasks, start=1):
         print(number, task)
         
elif choice == "3":
    number = int(input("task number to remove:"))
    task.pop(number - 1)
    print("Task remove")
    
elif choice == "4":
     print("Goodbye!")
     break
     
        
    