
# WAP to do menu driven program using arithmetic operation
import sys
def addition():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    print("Addition=",a+b)
def substraction():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    print("Substraction=",a-b)
def Multiplication():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    print("Multiplication=",a*b)
def Division():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    print("Division=",a/b)
while True:
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            addition() #calling function
        elif choice==2:
            substraction()
        elif choice==3:
             Multiplication()
        elif choice==4:
            Division()
        elif choice==5:
            sys.exit()

#output:

# 1.Addition
# 2.Substraction
# 3.Multiplication
# 4.Division
# 5.Exit
# Enter your choice:1
# Enter the value of a:2
# Enter the value of b:3
# Addition= 5
# 1.Addition
# 2.Substraction
# 3.Multiplication
# 4.Division
# 5.Exit
# Enter your choice:2
# Enter the value of a:4
# Enter the value of b:2
# Substraction= 2
# 1.Addition
# 2.Substraction
# 3.Multiplication
# 4.Division
# 5.Exit
# Enter your choice:3
# Enter the value of a:5
# Enter the value of b:6
# Multiplication= 30
# 1.Addition
# 2.Substraction
# 3.Multiplication
# 4.Division
# 5.Exit
# Enter your choice:4
# Enter the value of a:4
# Enter the value of b:2
# Division= 2.0
# 1.Addition
# 2.Substraction
# 3.Multiplication
# 4.Division
# 5.Exit
# Enter your choice:5