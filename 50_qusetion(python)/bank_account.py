class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount()
acc.deposit(500)
acc.withdraw(200)
acc.show_balance()