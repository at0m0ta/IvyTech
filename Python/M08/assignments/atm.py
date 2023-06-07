'''
Liliana Varela-Rodriguez
M08 Chapter 12
12.3 
'''
#12.3 Game: ATM

#creating account with id, balance, and interest rate attributes
class Account:
    def __init__(self, id = 0, balance = 100, annualIntRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualIntRate = annualIntRate
        
    def geID(self):
        return self.__id
    def setID(self, id):
        self.__id = id
        
    def getBalance(self):
        return self.__balance
    def setBalance(self, balance):
        self.__balance = balance
        
    def getannualIntRare(self):
        self.__annualIntRate = annualIntRate

    def getMonthlyInterestRate(self):
        return self.__annualIntRate / 12
    def getMonthlyInterest(self):
        return self.__balance * self.__annualIntRate / 1200
    
    def withdraw(self, amount):
        self.__balance -= amount
    def deposit(self, amount):
        self.__balance += amount

    def __st__(self):
        return "ID = " + str(self.__id) + "Account Balance = " \
               + str(self.__balance) + "Monthly Interest Rate = " \
               + str(acc.getMonthlyInterest()) + "Interest Rate + " \
               + str(self.__annualIntRate)
def main():
    accounts = []

    for i in range(10):
        accounts.append(Account(i, 100, 4.5))
    while True:
        ids = eval(input("Enter an account id: "))           
    if choice == 1:
        print("The balance is " + str(acc.getBalance()))
    if ids >= 0 and ids <= 9:
        acc = accounts
        print()
        print("1: MAIN MENU")
        print("2: CHECK BALANCE")
        print("3: WITHDRAW")
        print("4: EXIT")

    choice = eval(input("Enter a choice: "))

    if choice == 1:
        print("The balance is " + str(acc.getBalance()))
    elif choice == 2:
        amount = eval(input("Enter an amount to withdraw: " + str(acc.withdraw(amount))))
    elif choice == 3:
        amount = eval(input("Enter an amount to deposit: " + str(acc.deposit(amount))))
    elif choice == 4:
        break
    
main()
    
