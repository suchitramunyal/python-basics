# bool() is used to convert

print(bool(0)) #False
print(bool(15)) #True
print(bool(3.14))#True
print(bool(0.0))#False
print(bool(1+2j))#True
print(bool(0+0j))#False
print(bool(-1)) #True
print(bool(False)) #False
print(bool(True)) #True
print(bool(" "))

#wAP to accept days and check the working day or weekend
day=input("Enter Day:")
if day=="saturday" or day=="SUNDAY" or day=='SATURDAY' or day=='sunday':
    print("Weekend")
else:
    print("Working day")

#1.rstrip()===> remove spaces at right hand side
#2.lstrip()===>To remove spaces at left hand side
#3.strip()==>To remove spaces both sides

#BODMAS

a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)

#conditional statement
#simple if
#WAP to accept one single digit and check the entered number is positive, negative, zero
N=int(input("Enter single digit:"))
if N>0:
    print("Entered number is positive")
if N<0:
    print("Negative number")
if N==0:
    print("Zero")

s="help4code is a best platfrom for practicing programming"
print(s.find("help4code"))
print(s.find("python"))
print(s.find("program"))
# find() function return the starting index of given string and if string is not present then it returns default value -1

print('Subjects Marks:')
phy=50
chem=60
math=70
print("physics={} chemistry={} Math={} ".format(phy,chem,math))
print("physics={0} chemistry={1} Math={2} ".format(phy,chem,math))
print("physics={x} chemistry={y} Math={z} ".format(x=phy,y=chem,z=math))
total=phy+chem+math
print("total Marks",f"{total}")
print("Roll No=","7".zfill(4))

name=    "geetarkurabet"
#indexing=0123456789101112
print(name[0]) #p
print(name[1]) #r
print(name[-1]) #a
#print(name[15])Error string index out of range
print(name[0:5]) #end-1, 5-1=4 prash
print(name[1:]) #rashatjha
print(name[:5]) #5-1=4 prash
print(name[:]) #prashantjha
print(name[1:10:3]) #'''8-1=7= rsat
print(name[::-1])

s= "Python is a High level programming Language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

principal=100000
roi=10
time=1
si=principal*roi*time/100
print("simple interset=",si)

#WAP for swapping using third variable

val1=100
val2=200
print("Before Swapping",val1," ",val2)
temp=val1 #temp=100
val1=val2 #val1=200
val2=temp #val2=100
print("After Swapping",val1," ",val2)