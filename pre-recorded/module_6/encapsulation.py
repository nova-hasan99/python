
class bankAccount:
    __balance = 100

    # deposit
    def deposit(self, amount = 0):
        if amount > 0:
            self.__balance += amount
            print (f'{amount}tk Deposit Successfully')

        else:
            print (f'Invalid amount {amount}tk')

    # withdraw
    def withdraw(self, amount = 0):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print (f'{amount}tk Withdraw Successfully')

        else:
            print ('insufficient Balance :)')

    # check balance
    def checkBalance(self):
        print (f'Your Balance now {self.__balance}tk')

balance = bankAccount()
balance.deposit()
balance.withdraw()
balance.checkBalance()