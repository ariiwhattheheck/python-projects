print("TO DO LIST!!!")

todo_list=[]
xp=0

while True:
  if len(todo_list) == 0:
    print("List empty!!")
  else:
    index=1
    for tasks in todo_list:
        print(f"{index} . {tasks}")
        index+=1

    
  print("What do you wanna do?")
  print("1) Add task to list")
  print("2) Remove task from my list")
  print("3) See XP")
  print("4) Quit Program")

  choice = input("Choose your option: ")

  if choice == "1":
      print("ADDING TASKS: ")
      new_task=input("What task do you wanna add?")

      todo_list.append(new_task)

  if choice == "2":
      print("Removing Tasks: ")
      if len(todo_list) == 0:
        print("Your list is empty")
      else:
        todo_list.pop()
        xp+=10
        print("TASK DONE!!! You gained 10 XP")

  if choice == "3":
      print(f"Your Current XP: {xp}")
 
  if choice == "4":
      print("Quitting Program")
      break
      

