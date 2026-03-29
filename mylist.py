mylist=["prashat","Ashis","komal","ankush","Ashish",77,"sandip",60.52,"prashant"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])
print(mylist[:])
print(mylist[::-1])

mylist[2]="Akshay"
print(mylist)
#how to change the index value

if "ankush" in mylist :
    print("yes ankush is available")
else:
    print('not available')

mylist.append('harsh')
mylist.append("laxman")
print(mylist)

mylist.insert(1,"sanket")
print(mylist)
#if we have to add the value at specified index

mylist.remove("sandip")
print(mylist)

newlist=mylist.copy() #cloning
print(mylist)
print(newlist)

mylist=[['prashant','jha'],['85.56'],[440022,"yyy"]]
print("example of multidimensional list:")
print(mylist)
# print(mylist[row][col]]) 
print(mylist[0][0])                       
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

list1=["prashant","jha"]
print(list1*4) # it will print two times
list2=[50,25.50]
print(list1+list2)

list2=[50,25.50,'prashant']
# del list2[2]
del list2
print(list2)

list2=[50,25.50,'prashant']
list2.clear()
print(list2) #[]

name="prashat" #str
print(name)
myname=list(name)#typecasting
print(myname)
#we have used list constructor

mylist=[40,30,20,10]
mylist.reverse()
print(mylist)

#sorting example
mylist=[44,22,77,0,9,88]
mylist.sort(reverse=True)
print(mylist)
#default sorting order for number is ascending order
#default sorting order for string is alphabetical order
#we should know that list should contain homogenious
#data otherwise we will get TypeError
#python2 first short number then string follow

mylist=[44,22,77,0,9,88]
newlist=mylist
print(id(mylist))
print(id(newlist))