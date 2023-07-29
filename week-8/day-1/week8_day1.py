# # Q1)
# class Rectangle:
#     def inputDimension(self):
#         self.length = int(input("enter length : "))
#         self.breadth = int(input("enter breadth : "))

#     def area(self):
#         return self.length*self.breadth


# a = Rectangle()
# a.inputDimension()
# print(a.area())

# # Q2)
# class Car:
#     def getMakeModel(self):
#         self.make = input("Enter make of car : ")
#         self.model = input("Enter model of the car : ")
#         return str(f"The make of car is  {self.make}  and model of car is {self.model}")


# c1 = Car()
# print(c1.getMakeModel())

# Q3)
import random


class BankAccount:
    balance = 0
    accountNumber = random.randint(100000, 999999)

    def deposit(self):
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount
        print(f"Your balance is {self.balance}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print(
                f"Insufficient balance. Your actual balance is {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Your balance is {self.balance}")


a = BankAccount()
a.deposit()
a.withdraw()
