import math
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

n = int(input("Enter a Number: "))

if n <= 1:
    print(f"{n} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"Your Entered Number --> {n} is a Prime Number")
    else:
        print(f"Your Entered Number --> {n} is NOT a Prime Number")
# Task 07
def calculate_Area(shape):
    if(shape == "Rectangle"or shape == "rectangle"):
        width=  int(input("Enter width of Rectangle: "))
        length= int(input("Enter Length Of th Rectangle: "))
        result=width*length
        print(result)
    elif(shape == "Circle" or shape == "circle"):
        radius = float(input("Enter radius value: "))
        output=3.14*(radius**2)
        print(output)
    else:
        print("Please Enter Cicle or Rectangle shapes only for Now.")
calculate_Area("Triangle")
# Test 08
def star_Pattern(rows):
    for i in range(1,rows+1):
        print('*' * i)
star_Pattern(5)
# Test 09
def reverse_string(s):
    return s[::-1]
print(reverse_string("HELLO"))
# Test 10
def list_Task(val):
    li = [5, 12, 8, 3, 19, 7]
    if val == "max":
        result = li[0]
        for num in li:
            if num > result:
                result = num
        return result 
    elif val == "min":
        result = li[0]
        for num in li:
            if num < result:
                result = num
        return result
    else:
        return "Invalid Option! Use 'max' or 'min'."

print("Max value:", list_Task("max"))  
print("Min value:", list_Task("min"))  

# Task 11

odd_squares = [x**2 for x in range(1, 21) if x % 2 != 0]

print(odd_squares)
# Task 12
dic={
    "Apple":500,
    "Banana":1000,
    "Orange":1500,
    "Watemelon":2000,
    "Grapes":2500
}
ask = input("Enter Your Fruit : ")
if ask in dic:
    print("NOT ANY PRODUCT FOUND")
else:
    # Task 13
s1=set((1,2,3))
s2=set((3,4,5))
print(s1.intersection(s2))

# Task 14
la=[1, 2, 2, 3, 4, 4, 5]
print(set(la))
print(type(la))