'''
Liliana Varela
02/02/2018
PYTHON Module 5
Assignment Chapter 9

'''

#9.2 (Create an investment-value calculator)


#imports tinker program
from tkinter import * 

class Main:
    
    #computing future value
    def computeFuture(self):
        #getting monthly interest rate
        monthlyIntRate = float(self.annualIntRate.get()) / 1200
        #getting future value and assigning it to f
        f = float(self.investAmnt.get()) * (1 + monthlyIntRate) ** (float(self.years.get()) * 12)
        #formating the variable, 10 spaces  before decimal only 2 after decimal 
        self.futureVal.set("{0:10.2f}".format(f))
        
    def __init__(self):
        
        #creating window
        window = Tk()
        window.title("Investment-value calculator")

        #creating text telling user what to enter
        Label(window, text = "Investment Amount: ").grid(row = 1, column = 1, sticky = W)

        Label(window, text = "Annual Interest Rate: ").grid(row = 2, column = 1, sticky = W)

        Label(window, text = "Enter years money has been in account: ").grid(row = 3, column = 1, sticky = W)

        Label(window, text = "The Future Value of investment is: ").grid(row = 4, column = 1, sticky = W)

        #creating text entry for user
        self.investAmnt = StringVar()
        Entry(window, textvariable = self.investAmnt, justify = RIGHT).grid(row = 1, column = 2)

        self.annualIntRate = StringVar()
        Entry(window, textvariable = self.annualIntRate, justify = RIGHT).grid(row = 2, column = 2)

        self.years = StringVar()
        Entry(window, textvariable = self.years, justify = RIGHT).grid(row = 3, column = 2)

        self.futureVal = StringVar()
        Entry(window, textvariable = self.futureVal, justify = RIGHT).grid(row = 4, column = 2)

        #creating calculate button
        Button(window, text = "Calculate", command = self.computeFuture).grid(row = 5, column = 2)

        #creating event loop
        window.mainloop()

Main()
        
