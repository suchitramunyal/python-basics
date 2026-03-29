#WAP to implement some predefined functions?


Name  = 'Suchitra'    
sid   = 101    
percentage = 88.8
Result = True    
print(type(Name)) # type function returns the data type     
print(type(sid))  # class of variable    
print(type(percentage))    
print(type(Result))    
# id function returns the address of variable    
print(id(Name))     
print(id(sid))      
print(id(percentage))    
print(id(Result))    

#Output:

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# 135178506771120
# 135178519633736
# 135178508126352
# 135178519627200

#WAP to implement user defined functions?


def login():# called function  
        username = input("Enter your username")  
        password = input("Enter your password")  
        if username ==  password:  
                print("login successfully")   
        else:  
                print("you have entered wrong credentials")  
  
login()#calling function  

#output:

# Enter your username Suchitra
# Enter your password Suchitra
# login successfully

# WAP to implement user defined functions along with positional argument?
def info(firstname,lastname): # called function   
     print( 'First name=', firstname)  
     print( 'Last name=', lastname)  
  
info( 'suchitra', 'munyal' ) # calling function  
# Output:
# First name= suchitra
# Last name= munyal

# WAP to return the multiple values at the same time?

def arithmatic( a, b ): # called function  
    r = a+b  
    n = a*b  
    m = a-b  
    return r,n,m   
  
result = arithmatic( 10, 5 )#calling function  
print("Result = ", result)  

# Output:

# Result = (15, 50, 5)


#Keyword argument: In keyword argument position does not matter but parameter name and argument must be matched.

# WAP to implement keyword argument?

def func(fname,lname):#called function  
    print("Hi",fname)  
    print("Hi",lname)  
func(fname="suchitra",lname="munyal")#calling function  
func(lname="suchitra", fname="munyal")#calling function    

# Output:

# Hi suchitra
# Hi munyal
# Hi suchitra
# Hi munyal


# WAP to implement keyword argument?

def func(fname,lname):#called function  
     print("Hi",fname)  
     print("Hi",lname)  
fname = input("Enter first name")  
lname = input("Enter last name")  
func(fname, lname) #calling function 

# Output:
# Enter first name suchitra
# Enter last name munyal
# Hi suchitra
# Hi munyal


#Default argument: In default argument when user does not pass argument then the default value is used.

# WAP to implement default argument?

def nameOfCity(city ='Nagpur' ):  
      print('City Name=', city)  
  
nameOfCity( 'Mumbai' )  
nameOfCity( 'Pune' )  
nameOfCity( )#in this case default value will used  

# Output:
# City Name= Mumbai
# City Name= Pune
# City Name= Nagpur


#Variable length argument: In variable length arguments when we pass the variable number of arguments then it is called as variable length arguments and this is used to pass multiple positional arguments. arguments are stored as a tuple inside the function.

# WAP to implement variable length argument?

def nameOfCity(*city):  
      print('Name of city=',city)  
nameOfCity('Mumbai','Pune','Nagpur','Nashik')  

# Output:
# Name of city= ('Mumbai', 'Pune', 'Nagpur', 'Nashik')


#Keyword variable length argument: here we can pass multiple keyword arguments and arguments are stored as a dictionary inside function.

# WAP to implement variable length keyword variable length argument?


def pcmMarks(**kwargs):  
     for key, value in kwargs.items():  
         print(f"{key}: {value}")  
pcmMarks(phy = 50, chem = 60, math = 70, hindi=80, english=90)  

# Output:
# phy: 50
# chem: 60
# math: 70
# hindi: 80
# english: 90

#WAP for recursive functions?

def factorial(n):  
      if n == 0:  
          return 1  
      return n * factorial(n - 1)  
print(factorial(5))  

# Output:
# Output: 120

# WAP for implementation of nested function?

# Nested function  
def myname(): # outer called function  
        print("my name is radha")  
        def myrollno(): # inner called function  
                print('my rollno is 1001')  
        myrollno() # inner calling function  
myname() # outer calling function  

# Output:
# my name is radha
# my rollno is 1001

 #WAP for addition of numbers using lambda function?

add = lambda val: val+val  
print("The sum of 10 is :",add(10))  
print("The sum of 20 is :",add(20)) 

# Output:
# The sum of 10 is : 20
# The sum of 20 is : 40


# WAP for subtraction of numbers using lambda function?

sub = lambda x,y: x-y
print("The result is :",sub(30-10))  
 
# Output:
# The result is : 20


#WAP to take another function as an argument?

num = [10, 20, 30, 40]
squared_number = list(map(lambda x: x**2, num))
print(squared_number) 
# Output:
# [100, 400, 900, 1600]


# WAP to use the filter() function?

list_val=[0,1,2,3,4,5,6,7,8,9]  
finalResult=list(filter(lambda x:x%2==0,list_val))  
print(finalResult)  

# Output:
# [0, 2, 4, 6, 8]



