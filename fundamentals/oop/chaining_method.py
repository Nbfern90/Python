class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_withdrawl(self, amount):
        self.amount -= amount
        return self

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance {self.amount}")
        return self


nick = User("nick")
bob = User("bob")
john = User("john")

nick.make_deposit(200).make_deposit(300).make_deposit(
    500).make_withdrawl(500).display_user_balance()

bob.make_deposit(100).make_deposit(600).make_withdrawl(
    50).make_withdrawl(50).display_user_balance()

john.make_deposit(1000).make_withdrawl(
    200).make_withdrawl(100).display_user_balance()
