# # Q1)
# class Book:
#     def __init__(self):
#         self.title = input("Enter title of the book : ")
#         self.author = input("Enter author of the book : ")
#         self.price = int(input("Enter price of the book : "))

#     def discount(self):
#         if self.price >= 5000:
#             print(
#                 f"You get a discount of 20%.Your final price will be Rs.{self.price*0.8} ")
#         elif self.price >= 1000 and self.price < 5000:
#             print(
#                 f"You get a discount of 10%.Your final price will be Rs.{self.price*0.9} ")
#         else:
#             print(
#                 f"You get a discount of 5%.Your final price will be Rs.{self.price*0.95} ")


# customer = Book()
# customer.discount()

# # Q2)
# class Employee:
#     def __init__(self):
#         self.name = input("Enter your name :")
#         self.age = int(input("Enter your age : "))
#         self.salary = int(input("Enter your salary : "))
#         self.department = input("Enter your department : ")

#     def promote(self):
#         self.salary = self.salary*1.4
#         print(
#             f"Your salary has been increased by 40%.Your new salary is {self.salary}")


# person = Employee()
# person.promote()

# # Q3)
# class Rectangle:

#     def __init__(self):
#         self.length = int(input("Enter value for length : "))
#         self.breadth = int(input("Enter value for breadth : "))

#     def area(self):
#         return self.length*self.breadth


# a = Rectangle()
# print(f"Area of rectangle is {a.area()}")

# Q4)
class BankAccount:
    def __init__(self):
        self.balance = int(input("Enter your balance : "))
        self.accountNumber = int(input("Enter your account number : "))

    def deposit(self):
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount
        print(f"Your balance = {self.balance}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print(
                f"Insufficient balance. Your actual balance is {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Your balance = {self.balance}")


customer = BankAccount()
customer.deposit()
customer.withdraw()
