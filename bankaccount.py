class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    # Create a deposit method
    def Deposit(self, d):
        self.balance = self.balance + d

    # Create a withdrawal method
    def Withdrawal(self, w):
        if self.balance < w:
            print('Insufficient funds')
        else:
            self.balance = self.balance - w

    # Create a bank fees method
    def bankFees(self):
        self.balance = (95/100) * self.balance 

    # Create a display method
    def display(self):
        print('Your account details :')
        print('----------------------')
        print('Your account number :', self.accountNumber )
        print('Your name is :', self.name )
        print('Your account balance :', 'R', self.balance)

# Testing the code
myacc = BankAccount(4568912088, 'Joe Soap', 2000)
myacc.Withdrawal(500)
myacc.Deposit(50)
myacc.bankFees()
myacc.display()
