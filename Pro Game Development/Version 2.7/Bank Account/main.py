class BankAccount:
    def __init__(self, oname, balance = 0):
        self.oname = oname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def display_balance(self):
        return f"{self.oname}'s balance: {self.balance}"


account1 = BankAccount("Alica", 500)
account2 = BankAccount("Kaity", 300)

account1.deposit(200)
account1.withdraw(50)

account2.deposit(100)
account2.withdraw(50)

print(account1.display_balance())
print(account2.display_balance())

if account1.balance > account2.balance:
    print(f"{account1.oname} has the higher balance.")
elif account2.balance > account1.balance:
    print(f"{account2.oname} has the higher balance.")
else:
    print("Both accounts have the same balance.")