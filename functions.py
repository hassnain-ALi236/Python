list=["math","chemistry","physics"]
def findlength(list):
    print(len(list))
findlength(list)
def void():
    print("This is a void function")
    print("This is a void function")
    print("This is a void function")
    print("This is a void function")
void()
void()
void()

# Task 01
def factorial(n1):
    fact=1
    for i in range(1,n1+1):
        fact*=i
    print("Factorial of",n1,"is",fact)
factorial(5)

# Task 2

def converter(celcius):
    fahrenheit=(celcius*9/5)+32
    print("Temperature in fahrenheit is :",fahrenheit)
converter(37)

# Task 03

def money(USD):
    PKR=USD*280
    print("Your money in PKR is :",PKR)
money(100)

# Task 04

def odd_even(n1):
    if(n1%2==0):
        print(n1,"is even number")
    else:
        print(n1,"is odd number")
odd_even(5)