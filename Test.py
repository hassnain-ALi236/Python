# name=input("Enter your name : ")
# age=input("Enter your age : ")
# print(name,"your age is",age )

# Test 02
x = 10
y = 10.5,
z = "10",
a = True,
b = [1,2,3]
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
# Test 03
n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
if(n1 % 2==0 ):
    print("Your Entered Number =",n1, "is an even Number ")
elif(n2 % 2 == 0):
    print("your Entered Number =" ,n2, "is an even number" )
elif(n1 % 2==0 and n2 == 0 ):
    print("Both are Even Numbers")
elif(n1 % 2!=0 and n2 != 0 ):
    print("Both are Odd Numbers")
else:
    print("Please Enter Integer")
    # Test 04
t1=int(input("Enter First Number : "))
t2=int(input("Enter Second Number : "))
t3=int(input("Enter Third Number : "))
if(t1 > t2 and t1 > t3):
    print(t1,"is greate than other Numbers")
elif(t2>t3):
    print(t2,"is greater than other numbers")
else:
    print(t3,"is greater than other")
    # Test 05
li=[2,4,6,28,39,40,50,52,53]
print(li)
i=0
if(li>=50 ):
    print("YES")
else:
    print("NO")
#Test 06_____________________________________________----------------
for i in range(2,,1):
    if(i%2 ==0 or i**0.5 % i ==0 ):
        print("this is a prime number")
        i+=1
    print(i)