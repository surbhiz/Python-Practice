class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


check = BankAccount()
check.set_details("Surbhi", 200)
check.display()

check1 = BankAccount()
check1.set_details("Shashank")
check1.display()

check.withdraw(100)
check.display()

check1.deposit(100)
check1.display()