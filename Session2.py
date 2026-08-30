# t1
n= int(input("Enter a Number : "))
if(n >= 1 and n <= 100 ):
    print("Number is Between 1 and 100.")
else:
    print("Number is not bertween 1 and 100.")
# t2
n= int(input("Enter a Number : "))
if(n % 4 == 0 ):
    print("Leap Year.")
else:
    print("Not a Leap Year.")
    # t3
c = int(input("Enter Temp in Celsius : "))
c1=input("in which you want to convert F/C : " ).lower()
if(c1 == "f"):
    fahrenhite=((c*9)/5+32)
    print("Temp in Fahrenhite = " , fahrenhite)
elif (c1 == "c"):
    Celsius=((c - 32)*5/9)
    print("Temp in Fahrenhite = " , Celsius)
    # t4
num=int(input("Enter Number : "))
i=0
while(i<=num):
    print(num)
    i+=1
    # t5
n1= int(input("Enter a Number : "))
i=0
sum=0
while(i<=n1):
    sum+=i
    i+=1
print(sum)
# t6
t=int(input("Enter Number : "))
i=1
while(i<=10):
    print(i*t)
    i+=1

