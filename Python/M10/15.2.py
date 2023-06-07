'''
Liliana Varela
M10 15.2
04/08/2018
'''

#15.2 Fibonaci numbers

def fib(n):
    f0 = 0
    f1 = 1
    #return 0 if n is 0
    if n == 0:
        return 0
    #return 1 if n is 1
    if n == 1:
        return 1
    #if any other number, go through algorithm 
    for i in range(2, n + 1):
        currentFib = f0 + f1
        f0 = f1
        f1 = currentFib
    return f1

def main():
    #input integer
    index = eval(input("Enter an a number to get it's Fibonacci: "))
    #print out fib number
    print("The Fibonacci number at " + str(index) + " is " + str(fib(index)))
    
main()
