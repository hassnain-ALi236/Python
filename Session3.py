n1=int(input("Please Enter One Number : "))
n2=int(input("Please Enter Second Number : "))
n3=int(input("Please Enter Third Number : "))
if(n1 > n2 and n1 > n3):
    print(f"{n1} is Greater Than {n2} and {n3}. ")
elif(n2 > n3):
    print(f"{n2} is Greater than {n1} and {n3}")
else:
    print(f"{n3} is greater than {n1} and {n2}")

    # t2
name=input("Enter a Name : ")
n=name[::-1]
print(n)
if(n==name):
    print("Palindrome.")
else:
    print("not.")

    # t3
numbers = [12, 5, 8, 19, 21, 40, 7, 33]
even_count=0
odd_count=0
for i in numbers:
    if(i % 2 == 0):
        even_count+=1
    else:
        odd_count+=1
print("Total Even Number-->",even_count)
print("Total Odd Number-->",odd_count)
              
              # t4
items = [2, 4, 2, 6, 8, 4, 10, 6, 12]
my_set=set(items)
print("No Duplicate Values : " , my_set)

# t5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Job:
    def __init__(self, company, salary):
        self.company = company
        self.salary = salary
class Employee(Person, Job):
    def __init__(self, name, age, company, salary):
        Person.__init__(self, name, age)
        Job.__init__(self, company, salary)
    def show_profile(self):
        print("=== Employee Profile ===")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Company: {self.company}")
        print(f"Salary: Rs. {self.salary}")
emp1 = Employee("Hassnain", 22, "Tech Solutions", 95000)
emp1.show_profile()

# t6
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs. {amount} Deposited Successfully!")
        else:
            print("Invalid Amount!")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance!")
        elif amount <= 0:
            print("Invalid Amount!")
        else:
            self.__balance -= amount
            print(f"Rs. {amount} Withdrawn Successfully!")
    def get_balance(self):
        return self.__balance
account = BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
print("Current Balance:", account.get_balance())