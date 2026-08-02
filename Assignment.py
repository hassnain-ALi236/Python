# Write a Python program that takes 5 integers as input and displays the largest and smallest number.
n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
n3=int(input("Enter Third Number : "))
n4=int(input("Enter Fourth Number : "))
n5=int(input("Enter Fifth Number : "))
print(f"Your Largest Number is --> {max(n1,n2,n3,n4,n5)}")
print(f"Your Smallest Number is --> {min(n1,n2,n3,n4,n5)}")

# Write a Python program that:
# •	Takes a student's marks as input. 
# •	Uses conditional statements to display the appropriate grade (A, B, C, D, or F). 
marks = int(input("Enter Your Marks : "))
average= (marks/100*(100))
if(average > 90 ):
    print("Congrats You got A+")
elif(average >=80 and average < 90):
    print("Congrats You got B")
elif(average >=70 and average < 80 ):
    print("Congrats You got B+")
elif(average >=60 and average < 70):
    print("Congrats You got C")
elif(average >=50 and average < 60 ):
    print("Congrats You got D+")
elif(average >=40 and average < 50 ):
    print("Congrats You got D")
else:
    print("You are Failed . Try Next Year")

#     Write a Python program that:
# •	Takes 5 names as input in a list. 
# •	Sorts the list in ascending alphabetical order and displays the sorted list. 
num=[]
num1=input("Enter Your  Name: ")
num.append(num1)
num2=input("Enter Your  Name: ")
num.append(num2)
num3=input("Enter Your  Name: ")
num.append(num3)
num4=input("Enter Your  Name: ")
num.append(num4)
num5=input("Enter Your  Name: ")
num.append(num5)
print(num)
num.sort()
print("After Sorting Your Name\n", num)

# Write a Python program that defines a function factorial(n) to calculate and display the factorial of a number entered by the user.
def fac():
    n=int(input("Enter your Number : "))
    product=1
    for i in range(1, n+1):
        product=product*i

    print(f"Your Number Factorial {n} is {product}")
fac()
 

#  Write a Python program that:
# •	Takes 10 integers as input. 
# •	Uses a loop to count and display the number of even and odd numbers.

even_count = 0
odd_count = 0
for i in range(1, 11):
    num = int(input(f"Number {i} enter karein: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers:  {odd_count}")