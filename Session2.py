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