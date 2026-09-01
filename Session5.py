n=int(input("Enter Your Marks : "))
if(n >= 90):
    print("A+")
elif(n >= 80 and n < 90 ):
    print("A")
elif(n >= 70 and n < 80):
    print("B")
elif(n >= 60 and n < 70):
    print("C")
elif(n >= 50 and n < 60):
    print("D")
else:
    print("F")
    # t2
n = int(input("Enter a Number : "))
if(n > 0):
    print(f"{n} is Positive ")
elif(n < 0):
    print(f"{n} is Negative ")
elif(n == 0 ):
    print(f"Number = {n}")
else:
    print("Enter an Integer.")

    # t3
for i in range(1,50):
    if(i % 3 ==  0 ):
        print(i)

        # t4
secret_number=25
while True:
    n=int(input("Guess a Number between 1 to 50 : "))
    if(n > secret_number):
        print("Guess Lower Number.")
    elif(n < secret_number):
        print("Guess Higher Number.")
    else:
        print("Congrats Secret Number =",secret_number)
        break

        # t5
def calculate_Area(shape,value):
    shape=shape.lower()
    if(shape == "cricle" or shape == "c"):
        print("circle has been called in paras")
    elif(shape == "rectangle" or shape == "r"):
        print("rectangle has been called in paras.")
    elif(shape == "Triangle" or shape == "t"):
        print("triangle has been called.")
    else:
        print("Please write t/c/r")
calculate_Area("Rectangle",12)

# t6
try:
    n=int(input("Enter a number which is divide by 10 :"))
    result=10/n
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
        print(result)

        # t7 Main problems
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Sara", "Ahmed", "Ali", "Zara", "Bilal"],
    "age": [22, 25, np.nan, 22, 30, 28],          # ek missing value
    "salary": [50000, 60000, 55000, 50000, np.nan, 70000],  # ek missing value
    "city": ["Lahore", "Karachi", "Islamabad", "Lahore", None, "Multan"]
}

df = pd.DataFrame(data)
df.to_csv("Mian.csv", index=False)  

df = pd.read_csv("Mian.csv")
print(" Original Data ")
print(df)
print(df.isnull().sum())  

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())

df["city"] = df["city"].fillna("Unknown")

print("\n Missing Values (after fix)")
print(df.isnull().sum())  # ab sab 0 honi chahiye
print(df.duplicated().sum())

df = df.drop_duplicates()  
print(df.duplicated().sum())  # ab 0 honi chahiye
scaler = MinMaxScaler()
df[["age", "salary"]] = scaler.fit_transform(df[["age", "salary"]])
print(df)