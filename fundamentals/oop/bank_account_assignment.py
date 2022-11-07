class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def dispaly_account_info(self):
        print(f' Balance = {self.balance }')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


checking = BankAccount(.01, 1000)
savings = BankAccount(.05, 2000)

checking.deposit(500).deposit(300).deposit(
    200).yield_interest().dispaly_account_info()

savings.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(
    50).withdraw(50).yield_interest().dispaly_account_info()
