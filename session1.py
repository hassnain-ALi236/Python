# age=int(input("Please Enter Your Age : "))
# name=input("Please Enter Your Name : ")
# city=input("Please Enter Your City : ")
# print(f"Your Name is {name} . You are {age} Yeare Old. You Live in {city}")
# n1=int(input("Please Enter One Number : "))
# n2=int(input("Please Enter Second Number : "))
# result=n1 + n2
# print(f"Your Sum = {result}")
# n1=int(input("Please Enter One Number : "))
# if(n1 % 2 ==0):
#     print("Number is even ")
# else:
#     print("Number is Odd")

# n1=int(input("Please Enter One Number : "))
# n2=int(input("Please Enter Second Number : "))
# if(n1 > n2):
#     print(f"{n1} is Greater Than {n2}. ")
# else:
#     print(f"{n2} is Greater than {n1}")

n1=int(input("Please Enter One Number : "))
n2=int(input("Please Enter Second Number : "))
n3=int(input("Please Enter Third Number : "))
if(n1 > n2 and n1 > n3):
    print(f"{n1} is Greater Than {n2} and {n3}. ")
elif(n2 > n3):
    print(f"{n2} is Greater than {n1} and {n3}")
else:
    print(f"{n3} is greater than {n1} and {n2}")

marks=int(input("Please Enter Your Marks : "))
if(marks >= 90 and marks <=100):
    print("Grade is A.")
elif(marks >= 80 and marks < 90 ):
    print("Grade is B.")
elif(marks >= 70 and marks < 79 ):
    print("Grade is C.")
elif(marks >= 60 and marks < 69 ):
    print("Grade is D.")
elif(marks < 60):
    print("Grade is F.")

n1=int(input("Please Enter One Number : "))
n2=int(input("Please Enter Second Number : "))
operater=input("Select an Operator (+-*/) : ")
if(operater == "+"):
    print (f"Result =", n1 + n2)
elif(operater== "-"):
    print(f"Result =", n1 - n2)
elif(operater== "*"):
    print(f"Result =", n1 * n2)
else:
    print(f"Result =", n1/n2)

n1=int(input("Please Enter One Number : "))
if(n1 % 3==0 and n1 % 5==0):
    print("Number divisble by both.")
elif(n1 % 3!=0 and n1 % 5!=0):
    print("Number is not divisble by both.")
elif(n1 % 3== 0):
    print("number is Divisible by 3.")
elif(n1 % 5 == 0 ):
    print("number is divisble by 5.")
else:
    print("Enter a NUmber")

name = "Ali"
password= 1234
Name=input("Enter Username : ").casefold()
n1 = int(input("Enter Password : "))
if(Name == name and n1 == password):
    print("Login SuccessFull ")
elif(Name == name):
    print("Username Correct. But Password is wrong")
elif(n1==password):
    print("UserName might be Wrong")
else:
    print("Login Failed. Try Again.")