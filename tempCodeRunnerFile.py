class BankAccount:
    def __init__(self, initial_balance=0):
        # Double underscore (__) se variable private ho jata hai
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

# Testing Code
account = BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
print("Current Balance:", account.get_balance())

# Directly access karne par error aayega (Encapsulation Security):
# print(account.__balance) # AttributeError!