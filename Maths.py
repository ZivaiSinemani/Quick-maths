
#A simple maths program to calculate things...


#Multiplication function...
def multiply(x, y):
    z = x * y
    return z

#Division function...
def division(x, y):
    z = x / y
    return z


#Floor Division Function
def floordiv(x, y):
    z = x // y
    return z

#Subtraction function...
def subtraction(x, y):
    z = x - y
    return z


#Addition function...
def addition(x, y):
    z = x + y
    return z
    

#list of options menu
def menu():
    print("1. Multiplication")
    print("2. Division")
    print("3. Addition")
    print("4. Subtraction")
    print("5. Floor Division")
    choice = int(input("Select what you want to do:"))
    if choice == 1:
        x1 = int(input("Enter the first integer:"))
        y1 = int(input("Enter the second integer:"))
        total = multiply(x1, y1)
        print(x1, "multiplied by",y1, "is",total)
        
    elif choice == 2:
        x1 = int(input("Enter the first integer:"))
        y1 = int(input("Enter the second integer:"))
        total = division(x1, y1)
        print(x1, "divided by", y1 , "is",total)
    elif choice == 3:
        x1 = int(input("Enter the first integer:"))
        y1 = int(input("Enter the second integer:"))
        total = addition(x1, y1)
        print("The sum of", x1, "and", y1, "is",total)
    elif choice == 4:
        x1 = int(input("Enter the first integer:"))
        y1 = int(input("Enter the second integer:"))
        total = subtraction(x1, y1)
        print(x1, "minus", y1, "is",total)
    elif choice == 5:
        x1 = int(input("Enter the first integer:"))
        y1 = int(input("Enter the second integer:"))
        total = floordiv(x1, y1)
        print(total)
    else:
        print("Invalid choice. Please try again.")
        menu()
        
        
#Print the menu
menu()
                 
        
    
    