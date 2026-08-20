class Student:
    def __init__(self,Name,Eng,Math,Urdu):
        self.Name=Name
        self.Eng=Eng
        self.Urdu=Urdu
        self.Math=Math
    def Average(self):
        result=(self.Eng+self.Urdu+self.Math)/300*100
        return result
s1=Student("Ali Hassnain",92,99,100)
print(s1.Name)
print(s1.Urdu)
print(s1.Math)
print(s1.Eng)
print(s1.Average())
we can also store marks in a list like given below
class Student:
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks
    def Average(self):
        result=sum(self.Marks)/300*100
        return result
s1=Student("Ali Hassnain",[92,99,100])
print(s1.Name)
print(s1.Marks)
print(s1.Average())
if we dont want to use self as a parameter bcz self only use when we pass arguments but not when we make a simple print method for example
class car:
    @staticmethod
    def color():
        print("Car Colour is Blue :")
c1 = car()
print(c1.color())
class account:
    balance=1000
    ac_no="000001100001118"
    def debit(self):
        n=int(input("Enter Amount to credit from ur acc : "))
        self.balance-=n
        return("Your Balance is->",self.balance)
    def credit(self):
        n=int(input("Enter Amount to add in ur account :"))
        self.balance+=n
        return("Your New Balance is->",self.balance)
    def check_Balance(self):
        print("Your Current Balance is-->",self.balance)

a1=account()
print(a1.balance)
print(a1.ac_no)
print(a1.credit())
print(a1.debit())
print(a1.check_Balance())
