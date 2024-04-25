class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdraw successful")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def check_balance(self):
        print(f"Your balance is {self.balance}")


atm = ATM(1000,5000)

atm.withdraw(800)

atm.deposit(700)

atm.check_balance()