# whenever we declare inside a class it is called method 
class Student: #first character of classname must be capital
      roll_number=101
      num1=50
      num2=100 #data member

      def add(self): #member function
            print(self.num1+self.num2)
            self.name=input("Enter name:") #name is your new type of variable
            print(self.name)

obj=Student() #creating object of class and we always create a object
obj.add() #calling function
print(obj.roll_number) #Accessing the data member of class by using object

#output
150
# Enter name:suchitra
# suchitra
# 101


# In class level or in function first argument must be self
#By using constructor we initialize the object
#assinging the memory address to object
#Constructor call automatically whenever we create the object
# Here in python the name of the constructor is__init__(self).
# For one object Constructor will call one time

class NewClass:
    def __init__(self): #constructor declaration (called Automatically)
        print("constructor always execute first")
    def show(self): #member function inside of class (It is a use define function)
        print('welcome to class level programming')

obj=NewClass() #creating a object
#print(obj)
obj.show()
obj1=NewClass()

# output:
# constructor always execute first
# welcome to class level programming
# constructor always execute first


class Hod: #constructor
    def __init__(self):
        self.name='suchitra'
        self.age=20
        self.empid=1001

    def info(self): #instance method
        print("My name is :",self.name)
        print("My age is :",self.age)
        print("My emp id :",self.empid)

obj=Hod()#object create

#output:
# My name is : suchitra
# My age is : 20
# My emp id : 1001


class Hod: 
    def __init__(self,name,age,rollno): #parameterize constructor
        self.name=name
        self.age=age
        self.rollno=rollno

    def show(self): #instance method
        print("My name is :",self.name)
        print("My age is :",self.age)
        print("My rollno :",self.rollno)

obj=Hod('ravi',45,101)#object create
obj.show()

# output:
# My name is : ravi
# My age is : 45
# My rollno : 101

#types of variables: 1.Instance variable 2.Static variable 3.Local variable

#Instance Variable
class New:
    def __init__(self):
        self.a=10

Obj1  = New()
Obj2  = New()
Obj3  = New()
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)
Obj1.a =20
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)

 #output:
# 10
# 10
# 10
# 20
# 10
# 10

#Static variable:It is exactly opposite of instance variable
# 1 static variable= 1 memory

class New:
    a= 10 #static variable
    def __init__(self):
        self.name="suchitra" #instance variable

Obj1  = New()
Obj2  = New()
Obj3  = New()
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)
New.a = 50
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)

#Output
# 10
# 10
# 10
# 50
# 50
# 50

#Types of Method 1.Class method 2.Static method  3.Instance method
#Instance Method


class Student: 
    def __init__(self,name,rollno,mob): #parameterize constructor
        self.name=name
        self.mob=mob
        self.rollno=rollno

    def display(self): #instance method
        print(self.name, " ",self.rollno," ",self.mob)

stud= Student("Suchitra",1001,4567389276)
stud.display()

# Output
# Suchitra   1001   4567389276

#Static Method

class Student:  
    # by using class name we can access static method  
    @staticmethod # decorator  
    def get_personal_detail(firstname,lastname):  
        print("your personal detail=",firstname,lastname)  
  
    @staticmethod  
    def contact_detail(mobil_no, rollno):  
        print("your contact detail=", mobil_no,rollno)  
  
Student.get_personal_detail("suchitra", "Munyal")  
Student.contact_detail(5456454646, 1001)  

#Output:
# your personal detail= suchitra Munyal
# your contact detail  = 5456454646 1001

