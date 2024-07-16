print("*************A SIMPLE CALCULATOR*************")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Modulus")
print("6) Exponent")
print("7) Exit")

choice="0"

while choice != "-1":

  choice=input("Choose an option")

  if choice == "-1":
    print("Exiting program")
    break

  num1=input("Enter first number: ")
  num2=input("Enter second number: ")
  temp1=int(num1)
  temp2=int(num2)

  if choice == "1":
    result=temp1+temp2
    print(f"Result: {result}")

  elif choice == "2":
    result=temp1-temp2
    print(f"Result: {result}")
    
  elif choice == "3":
    result=temp1*temp2
    print(f"Result: {result}")

  elif choice == "4":
    if temp2 != 0:
        result=temp1/temp2
        print(f"Result: {result}")
    else:
        print("Denominator cannot be zero")
        continue

  elif choice == "5":
    if temp2 != 0:
        result=temp1%temp2
        print(f"Result: {result}")
    else:
        print("Denominator cannot be zero")
        continue

  elif choice == "6":
    result=temp1**temp2
    print(f"Result: {result}")

  else:
    print("Invalid choice!! Please enter a number between 1 and 6")

  
