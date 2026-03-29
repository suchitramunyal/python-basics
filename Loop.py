for i in range(1,5):
    if i==3:
        break
    print(i)

for i in range(1,5):
    if i==3:
        continue #it will directly go to next iteration and 3 will not print
    print(i)

list=[10,20,30,40,50] 
for i in list:  #in is a membership operator
    print(i)

mycart=[10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("This is my purchased cart item")
        continue
    print(i)

#WAP to calculate the sum of list elements
list=[1,2,3,4,5,6,7,8,9,10]
sum=0 #sum=
for x in list: #x=0,1 2.. : 1,2,3..
    sum=sum+x
print("The Sum=",sum)

name="prashant"
     #01234567
for i in name:
    print(i)

name="prashant"
     #01234567
newname=""
for i in range[-1:]:
        for i in name:
            if i not in newname:
                 newname += i
print(newname)

rollno=[3,5,7,1,11,4,5,2]
for x in rollno:
    if x==2 or x==4 or x==6 or x==8 or x==10:
        print("even no is found",x)
        break

#s.replace(oldstring,newstring)
#inside s, every occurrence of oldstring will be replaced with newstring.
s="easydifficult"
s1=s.replace("difficult","easy")
print(s1)
#All occurrences will be replaced
s="abababababab"
s1=s.replace("a","b")
print(s1)

x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x != z)
# is it comparing the value or address check it

val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.index(1))
print(val.index(2))
print(val.index(3))
print(val.index(4))
print(val.index(5))
print(val.index(6))
#it is returning the index value

n=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print(n.count(5))
print(n.count(6))
print(n.count(7))

import datetime
#datetime formating
date=datetime.datetime.now()
print("It's now:{:%d/%m/%y %H:%M:%S}".format(date))