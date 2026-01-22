class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # atribut privat

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Suma depusa trebuie sa fie pozitiva.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Suma retrasa trebuie sa fie pozitiva.")
        if amount > self._balance:
            raise ValueError("Fonduri insuficiente.")
        self._balance -= amount

    def get_balance(self):
        return self._balance

try:
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(300)
    print("Sold curent:", account.get_balance())

except ValueError as e:
    print("Eroare:", e)
