#for(initialization; condition; inc/dec)

for i in range(1,11):
    print(i*2," ",i*3," ",i*4," ",i*5," ",i*6)
for i in range(1,11):
    print(i*7," ",i*8," ",i*9," ",i*10)    


#WAP to print even and odd numbers
for i in range(1,11):
    if i%2==0:
        print("even=",i)
    else:
        print("odd=",i)

#WAP to print the count of even and odd
even=0 
odd=0
for i in range(1,11):
    if i%2==0:
        even +=1
    else:
        odd +=1
print("Even=",even)
print("Odd=",odd)

username=input("Enter Username:")
password=input("Enter password:")
if username==password:
    print("login successful")
else:
    print("Invalid login")

# brand=input("Enter your cooldrink name either in upper case or in lower case but not combine:")
if brand=="pepsi" or brand=="PEPSI":
    print("swag")
elif brand=="dew" or brand=="DEW":
    print("dar ke age jeet hai")
elif brand=='thumsup' or brand=='THUMSUP':
    print('taste the thunder')
else:
    print('go with your brand')

#biggest number
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("Biggest Number is:",n1)
elif n2>n3:
    print("Biggest Number is:",n2)
else:
    print("Biggest Number is:",n3)

#smallest number
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1<n2 and n1<n3:
    print("Smallest Number is:",n1)
elif n2<n3:
    print("Smalles Number is:",n2)
else:
    print("Smalles Number is:",n3)