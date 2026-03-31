#Pillars of OOPS: 1.Inheritance 2.Polymorpism 3.Abstraction 4.Encapsulation
# Inheritance:Extending property from one class to another class is called inheritance.
#Base class: A class which inherits its property to another is called base class or parent class.
#Derived class: A class in which properties are inherited called as derived class or child class.

# Single level inheritance  
class College: # parent class  
  def college_name(self): # member function of college  
    print("Modern College")  
    
class Student(College): # child class  
  def student_info(self): # memeber function  
    print("Name:   Suchitra Munyal")  
    print("Branch: CSE")  
     
obj = Student()# object create child class  
obj.college_name()  
obj.student_info()  

#Output
# Modern College 
# Name: Suchitra Munyal
# Branch: CSE


# Multilevel inheritance  
class College:   #first class  first- level  
  def college_name(self):  
    print("Modern College")  
#============================================  
class Student(College): #second class second - level  
  def student_info(self):  
    print("Name:   Suchitra Munyal")  
    print("Branch: CSE")  
#=============================================  
class Exam(Student): #child class  
  def subject(self):  
    print("Subject1: Computer Science")  
    print("Subject2: Math")  
    print("Subject3: C-Language")  
obj = Exam()  
obj.college_name()  
obj.student_info()  
obj.subject()  

# Output
# Modern College
# Name: Suchitra Munyal
# Branch: CSE
# Subject1: Computer Science 
# Subject2: Math 
# Subject3: C-Language

 #Multiple Inheritance:- A subclass inherits from more than one parent class. 
class SubjMarks: # class-1  
  math = int(input("Enter paper marks of math :"))  
  DE = int(input("Enter paper marks of design engineering :"))  
  c = int(input("Enter paper marks of c language :"))  
  english = int(input("Enter paper marks of English :"))  
#================================= parent class -1  
class PractMarks: # class-   
  cpract = int(input("Enter practicals marks of c language :"))    
#================================= parent class -2  
class Result(SubjMarks,PractMarks): # child class  
  #print("if student pass in both = subject and practical paper then pass")  
  def total(self):  
    if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:  
      print("pass")  
    else:  
      print("fail")  
obj = Result()  
obj.total()  
#Output:
# Enter paper marks of math :45 
# Enter paper marks of design engineering :55
# Enter paper marks of c language :66
# Enter paper marks of English :77
# Enter practical's marks of c language :23 
# pass


# Polymorphism: means having many forms. 
# Types of polymorphism in Python 

# 1.Duck Typing: (Dynamic Typing) Python follows the principle of "duck typing," which means that an object's behavior is determined by the methods and properties it has, rather than its actual class.
# 2.Compile Time Polymorphism: Method overloading(Not directly supported in python) 
# 3.Runtime Polymorphism: Method overriding(Supported)

#polymorphism example  
class Principal:  
    def role(self):  
        print("i am managing all activity of college")  
  
class Dean:  
    def role(self):  
        print('Dean= I am decision taking person')  
          
class Hod:  
    def role(self):  
        print('Hod= I have responsibility of Teachers and Students')         
class Faculty:  
    def role(self):  
        print('Faculty= I have to complete syllabus successfully')  
# ========== class declaration completed=====================================  
def  func(obj): # called func obj =1:Dean  
    obj.role()# calling func  
campus=[Principal(),Dean(),Hod(),Faculty()]   
for obj in campus: #obj =[0:Principal(),1:Dean(),2:Hod()]  
    func(obj)   # calling fun  

# Output
# i am managing all activity of college 
# Dean= I am decision taking person
# Hod= I have responsibility of Teachers and Students 
# Faculty= I have to complete syllabus successfully
# Note:- The problem in this approach is if obj does not contain role() method then we will get AttributeError

#Method Overloading
# WAP to understand why directly method overloading not supported in python.
#If we are trying to declare multiple methods with same name and different number of arguments then python will always consider last method.

class Arithmatic:  
    def add(self,a):  
        print(a)  
    def add(self,a,b):  
        print(a+b)  
    def add(self,a,b,c):  
        print(a+b+c)  
obj = Arithmatic()  
obj.add(10)  
obj.add(10,20)  
obj.add(1,2,3)  
#Output
# Traceback (most recent call last): 
# File "d:\D-Drive\Python programs\poly.py", 
# line 122, in <module> obj.add(10) 
# TypeError: Arithmatic.add() missing 2 required positional arguments: 'b' and 'c'


#WAP to understand why directly constructor overloading not supported in python.
#  Constructor overloading is not possible in Python.
#  If we define multiple constructors then the last constructor will be considered.

class Arithmatic:  
    def __init__(self):  
        print("There is no argument")  
    def __init__(self,a):  
        print("passing one argument")  
    def __init__(self,a,b):  
        print("passing two arguments")  
  
obj = Arithmatic()  
obj = Arithmatic(10)  
obj = Arithmatic(2,2)  
#Output
# Traceback (most recent call last): 
# File "d:\D-Drive\Python programs\poly.py", 
# line 153, in <module> obj = Arithmatic()
# TypeError: Arithmatic.__init__() missing 2 required positional arguments: 'a' and 'b'


#Method Overriding
class Rbi:
    def homeLoan_ROI(self):
        print("Home Loan rate of interest=7.5%")
    def carLoan(self):
        print("Car Loan Rate of interest=8%")

class Sbi(Rbi):
    def homeLoan_ROI(self):
        print("Home Loan Rate of interest=6.5%")

obj=Sbi()
obj.homeLoan_ROI()
obj.carLoan()

#Output
# Home Loan Rate of interest=6.5%
# Car Loan Rate of interest=8%
     
#using super() method we can access parent class method in child class
class Rbi:
    def homeLoan_ROI(self):
        print("Home Loan rate of interest=7.5%")
    def carLoan(self):
        print("Car Loan Rate of interest=8%")

class Sbi(Rbi):
    def homeLoan_ROI(self):
        print("Home Loan Rate of interest child=6.5%")
        super().homeLoan_ROI()
obj=Sbi()
obj.homeLoan_ROI()
obj.carLoan()

#Output 
# Home Loan Rate of interest child=6.5%
# Home Loan rate of interest=7.5%
# Car Loan Rate of interest=8%


#  WAP to take the examples of constructor overriding. (Here when we create the object of child class that time child class constructor override the parent class constructor)

#Constructor overriding  
class Father:  
    def __init__(self):  
        print("Father:= i am on time at breakfast table")  
  
class Child(Father):  
    def __init__(self):  
        print("Child:= i will be late for breakfast")  
  
obj = Child()  
# Output
# Child:= i will be late for breakfast

# using super() method constructor overriding
class Father:  
    def __init__(self):  
        print("Father:= i am on time at breakfast table")  
  
class Child(Father):  
    def __init__(self):  
        print("Child:= i will be late for breakfast")  
        super().__init__()
obj = Child() 

#Output
# Child:= i will be late for breakfast
# Father:= i am on time at breakfast table


#Abstraction:This concept help us to hide the complexity and shows only what is important and necessary. 
#Abstraction method has declaration but does not have implementation,we write implementation in child class

#WAP to take the example of abstraction.

from abc import ABC, abstractmethod  
class Help4code(ABC): # abstract class  
    @abstractmethod # decorator  
    def training(self):# abstract method  
        pass  
       
    @abstractmethod   # abstract method  
    def placement(self):  
        pass  
  
class Ashish(Help4code):  
    def training(self):  
        print('C , C++ , Java')  
    def placement(self):  
        print("Java placement")  
  
class Ankush(Help4code):  
    def training(self):  
        print("Python | Django")  
    def placement(self):  
        print("Python placement students")  
  
class Prashant(Help4code):  
    def training(self):  
        print("Machine learning")  
    def placement(self):  
        print("Data science placement")  
  
obj1 = Ashish()  
obj1.training()  
obj1.placement()  
  
obj2 = Ankush()  
obj2.training()  
obj2.placement()  
  
obj3 = Prashant()  
obj3.training()  
obj3.placement()  
#Output
# C , C++ , Java
# Java placement
# Python | Django
# Python placement students
# Machine learning 
# Data science placement
