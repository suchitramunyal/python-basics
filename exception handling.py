# WAP to understand why ZeroDivisionError Exception occurs.

a  =int(input("Enter any one value :"))  
b = int(input("Enter the second value: "))  
print(a/b)  
#-------------Output--------------------
# Enter any one value :2
# Enter the second value: 0
# Traceback (most recent call last): File "d:\D-Drive\Python programs\try.py", 
# line 11, in <module> print(a/b) ~^~ZeroDivisionError: division by zero



# WAP to understand why ValueError exception occurs.


a  =int(input("Enter any one value :"))  
b = int(input("Enter the second value: "))  
print(a/b)  
#-----------------OutPut-----------------------
# Enter any one value :2
# Enter the second value: &
# Traceback (most recent call last): File "d:\D-Drive\Python programs\try.py", 
# line 10, in <module> b = int(input("Enter the second value: ")) ^
# ValueError: invalid literal for int() with base 10: '&'


# WAP to handle the Division by zero exception by using try and except.


a  =int(input("Enter any one value :"))  
b = int(input("Enter the second value: "))  
try:  
    print(a/b)  
except:  
    print('can not devide by zero')  
#-------------Output-----------------------
# Enter any one value :2 
# Enter the second value: 0 
# can not devide by zero


# WAP to create short cut name of ZeroDivisionError in except block and handle the exception.


a  = int(input("Enter first number"))  
b  = int(input("Enter second number"))   
try:  
    print(a/b)  
except ZeroDivisionError as message:    
    print("The description of exception:",message)  
#---------------------output--------------------
# Enter first number 2
# Enter second number 0
# The description of exception: division by zero

# WAP how to handle multiple exception using multiple except block

try:  
    a=int(input("enter first integer no")) # *  
    b=int(input("enter second integer no"))  
    print(a/b)  
except ZeroDivisionError as message:  
    print("plz ensure that you can't divide any no by zero:",message)  
except ValueError as message:  
    print("Enter only interger no=>", message)  
#------------------output-------------------------
# enter first integer no: 2 
# enter second integer no: &
# Enter only interger no=> invalid literal for int() with base 10: '&'



# WAP how to handle multiple exception in single except block.


try:  
    a=int(input("enter first integer no"))  
    b=int(input("enter second integer no"))  
    print(a/b)  
except (ValueError, ZeroDivisionError) as message:  
    print(message)  
#-----------------Output----------------------------------
# enter first integer no :4
# enter second integer no :0
# division by zero


#WAP for default except block.


try:  
    a=int(input("enter first integer no"))  
    b=int(input("enter second integer no"))  
    print(a/b)  
except (ValueError, ZeroDivisionError) as message:  
    print("Enter correct number: ",message)  
except:  
    print("This is default part of except block")  
# default except block must be last because if we take the default except block as a first except block then syntax error will come.


# WAP to use else block along with try and except block.


try:  
    a=int(input("enter first integer no"))  
    b=int(input("enter second integer no"))  
    print(a/b)  
except (ValueError, ZeroDivisionError) as message:  
    print("Enter correct number: ",message)  
else:  
    print("Everything is ok")  
# if there is no error inputs are correct then try and else block will execute.
#---------------------------OutPut-----------------------------------------------------
# enter first integer no :4
# enter second integer no:2
# 2.0
# Everything is ok


#WAP for Try, Except and finally block. The finally block runs no matter, whether an exception occurs or not.It's useful for cleanup operations like closing files or releasing resources.


try:  
    a=int(input("enter first integer no"))  
    b=int(input("enter second integer no"))  
    print(a/b)  
except (ValueError, ZeroDivisionError) as message:  
    print("Enter correct number: ",message)  
finally:  
    print("I will always executed ")  
#----------------------OUTPUT-1----------------------------
# enter first integer no :4
# enter second integer no:2
# 2.0
# I will always executed
# #---------------------OUTPUT-2-----------------------------
# enter first integer no :4 
# enter second integer no:0
# Enter correct number: division by zero 
# I will always executed


# WAP for Nested Try Except block.

try:  
    a = int(input("Enter first number"))  
    b = int(input("Enter second number"))  
    try:  
        print(a/b)  
    except ZeroDivisionError as msg:  
        print(msg)      
except ValueError as msg:  
    print(msg)  
#------------------OUTPUT---------------
# Enter first number 4
# Enter second number 0
# division by zero


# WAP to implement try, except, else, finally block.

try:  
    a=int(input("enter first integer no"))  
    b=int(input("enter second integer no"))  
    print(a/b)  
except (ZeroDivisionError, ValueError) as message:  
    print(message)  
else:  
    print("there are no error in try block")  
finally:  
    print("I am finally block I always executed weather error raise or not")  
#-----------------------------OUTPUT-1---------------------------
# enter first integer no 2
# enter second integer no 0
# division by zero 
# I am finally block i always executed weather error raise or not
# #----------------------------OUTPUT-2---------------------------
# enter first integer no 2
# enter second integer no 2
# 1.0t
# there are no error in try block
# I am finally block i always executed weather error raise or not