import random


class Bank:
    """This class is used to create a bank object with some functions"""

    def __init__(self):
        self.amount = 0
        self.accno = random.randint(100000, 999999)
        self.name = input("Enter your name = ")
        self.bankName = input("Enter your bank name = ")

    def __str__(self):
        return "You have printed an object directly"

    def display(self):
        print(f"\n-------INFO-------")
        print(f"Account number = {self.accno}")
        print(f"Balance = {self.amount}")
        print(f"Name = {self.name}")
        print(f"Bank name = {self.bankName}")

    def displayBalance(self):
        """This is used to display all balance"""
        print(f"Your balance = {self.amount}")

    def deposit(self):
        """This method is used to deposit money in bank account"""
        newAmount = int(input("Enter amount to deposit = "))
        self.amount = self.amount + newAmount
        self.displayBalance()

    def withdraw(self):
        newAmount = int(input("Enter amount to withdraw = "))
        if newAmount > self.amount:
            print(
                f"Insufficient balance. Your actual balance is {self.amount}")
        else:
            self.amount = self.amount - newAmount
            self.displayBalance()

    def update(self):
        newName = input(
            "Enter new name. Or if you want default leave blank = ")
        if newName != "":
            self.name = newName
        newBankName = input(
            "Enter new bank name. Or if you want default leave blank = "
        )
        if newBankName != "":
            self.bankName = newBankName


accounts = []


def searchAccount(accountNumber):
    for i in accounts:
        if i.accno == accountNumber:
            return i
    else:
        return None


while True:
    print("1. Add an account")
    print("2. Print all accounts")
    print("3. search accounts")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Check Balance")
    print("7. Transfer")
    print("8. Exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        print(f"Account added. Your acc number = {obj.accno}")
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts found")
        else:
            for i in accounts:
                i.display()
    elif choice == 3:
        acc_no = int(input("Enter account number : "))
        for i in accounts:
            if i.accno == acc_no:
                i.display()
                break
        # this is for-else. Else part will run when for loop runs fully without any break.
        else:
            print("No accounts found")
    elif choice == 4:
        acc_no = int(input("Enter account number : "))
        for i in accounts:
            if i.accno == acc_no:
                i.deposit()
                break
        else:
            print("No accounts found")
    elif choice == 5:
        acc_no = int(input("Enter account number : "))
        for i in accounts:
            if i.accno == acc_no:
                i.withdraw()
                break
        else:
            print("No accounts found")
    elif choice == 6:
        acc_no = int(input("Enter account number : "))
        for i in accounts:
            if i.accno == acc_no:
                i.displayBalance()
                break
        else:
            print("No accounts found")
    elif choice == 7:
        acc_no = int(input("Enter account number = "))
        senderAccount = searchAccount(acc_no)
        if senderAccount != None:
            rec_acc_no = int(input("Enter reciver accno number = "))
            reciverAccount = searchAccount(rec_acc_no)
            if reciverAccount != None:
                transferAmount = int(input("Enter amount to transfer = "))
                if transferAmount > senderAccount.amount:
                    print("Insufficient Balance")
                else:
                    reciverAccount.amount += transferAmount
                    senderAccount.amount -= transferAmount
                    print(f"Your balance is {senderAccount.amount}")
            else:
                print("Reciver account number is invalid")
        else:
            print("Your account does not exists")
    elif choice == 8:
        break
    else:
        print("choose correct option.")
