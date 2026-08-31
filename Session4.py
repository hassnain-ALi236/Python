n=int(input("Erter  digits : "))
rev=0
while n > 0:
    digits = n % 10
    rev = rev *10 + digits
    n = n // 10
print("Reversed Number = ", rev)
#  t2
def isprime(num):
    if num < 2:
        print("Not Prime")
    else:
        prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not Prime")
isprime(7)

#  t3
li = [12, 45, 2, 41, 31, 10]
largest = second = float('-inf')

# t4
for num in li:
    if num > largest:
        second = largest
        largest = num
    elif num > second:
        second = num

print("Largest:", largest)
print("Second Largest:", second)

# t5
class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def calaculate_Average(self,marks):
        result=(sum(marks) / 300)*100
        print(result)
s1=student("Ali Hassnain", 1208 , [98,99,100])
print(s1.name)
print(s1.roll_no)
print(s1.marks)
print(s1.calaculate_Average([98,99,100]))

# t6
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def display_Teacher(self):
        print(f"Teacher: {self.name} | Age: {self.age} | Subject: {self.subject}")
t1=teacher("Hassnain",19,"Science")
t1.display_Teacher()

# t9

class Animal:
    def speak(self):
        print("Animal makes a sound.")
class Dog(Animal):
    def speak(self):
        print("Dog barks!")
class Cat(Animal):
    def speak(self):
        print("Cat meows!")
print("Q9 - Polymorphism Output:")
d = Dog()
c = Cat()
d.speak()
c.speak()

# t10
class Bank:
    bank_name = "HBL" # Class Variable

    def __init__(self, acc_holder, acc_number):
        self.acc_holder = acc_holder 
        self.acc_number = acc_number 
    def print_details(self):
        print(f"Q10 - Bank: {Bank.bank_name} | Holder: {self.acc_holder} | Acc #: {self.acc_number}")

b1 = Bank("Ali Hassnain", 100293)
b2 = Bank("Umair", 100294)

b1.print_details()
b2.print_details()
