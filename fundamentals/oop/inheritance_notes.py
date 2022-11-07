class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance


class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth


# this is redundant they because the parent class(BankAccount) has the two attributes already

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance


class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

# WE USE THE super() KEYWORD


class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self


class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

# THIS BECOMES:


class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self
