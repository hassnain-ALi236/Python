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