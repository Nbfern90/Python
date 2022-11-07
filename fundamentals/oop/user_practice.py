class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_withdrawl(self, amount):
        self.amount -= amount

    def make_deposit(self, amount):
        self.amount += amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance {self.amount}")


nick = User("nick")
bob = User("bob")
john = User("john")

nick.make_deposit(200)
nick.make_deposit(300)
nick.make_deposit(500)
nick.make_withdrawl(500)
nick.display_user_balance()

bob.make_deposit(100)
bob.make_deposit(600)
bob.make_withdrawl(50)
bob.make_withdrawl(50)
bob.display_user_balance()

john.make_deposit(1000)
john.make_withdrawl(200)
john.make_withdrawl(100)
john.make_withdrawl(200)
john.display_user_balance()
