class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        dep = input()
        if dep.isdigit():
            print(f"The Client {self.owner}'s previous balance:{self.balance}\n")
            self.balance+=int(dep)
            print(f"The Client {self.owner}'s current balance:{self.balance}\n")
        else:
            print("Incorrect input\n")
    def withdraw(self):
        widr = input()
        if widr.isdigit():
            widr=int(widr)
            if self.balance < widr:
                print("The Client {self.owner} does not have enough money\n")
            else:
                print(f"The Client {self.owner}'s previous balance:{self.balance}\n")
                self.balance-=widr
            print(f"The Client {self.owner}'s current balance:{self.balance}\n")
        else:
            print("Incorrect input\n")
a = Account("Nur",10000)
a.deposit()
a.withdraw()