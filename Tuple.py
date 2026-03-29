mytuple=("prashant","Ashish","Rahul","sandip","Komal","ankush","rajesh",23,3.15,77,"sandip")
print(mytuple)
print(type(mytuple))
mytuple[2]="sunil"
print(mytuple)      

myset={1,2,"sanjay",5.66,"rahul","ayush","ramesh","ankit",'rishikesh'}
print(myset)
print(type(myset))  
  
myset.add(60)
print(myset)

myset.discard(3)
print(myset)

myset.remove(3)
print(myset)

myset={10,20,30,40}
yorset={"prashant","jha"}
newset=myset.union(yorset)
print(newset)
#union() this method will combine both sets

#intersection return common element
myset={10,20,30,40}
yorset={10,50,60,30}
print(myset.intersection(yorset))

#difference() method this will return the element
#present in first set but not in second set
myset={10,20,30,40}
yorset={10,50,60,30}
print(myset.difference(yorset))

#clear() we can use to clear data
#pop() method is used to remove object
myset={10,20,30,40}
print(myset.pop())
print(myset.clear())

mydict={
    "name":"prashant",
    "professional":"developer",
    "empid":1001
}
print(mydict)
print(type(mydict))

mydict={
    101:"prashant",
    102:"ashish",
    "103":"mohini",
    "104":"trivani",
    101:"ashish",#101 is updated to ashish eventhough prashant is first saved because data is updated
    104:"ashish" #104 is printed two times because "104"-this is in string and 104 this is integer
}
print(mydict)

#with the help of key we have to print values
a=mydict[102]
print(a)

#we will replace old value by new value
mydict[102]="peter"
print(mydict)

#only print key x=0,1
for x in mydict:
    print(x)

#only print values x=0
for x in mydict.values():
    print(x)

#printing key and values both
for x,y in mydict.items():
    print(x,y)

#if i have to add new key and value pair in my dictionary
mydict["mobile_no"]=4646463738
print(mydict)

mydict={
    "name":"prashant",
    "professional":"developer",
    "empid":1001
}
mydict.pop("name")
print(mydict)
#pop() method remove pair by specific key name

newdict=mydict.copy()
print(newdict)