'''
Liliana Varela - Rodriguez
04/11/2018
M06 Programming Exercises 10.2
'''

#10.2 Reverse the numbers entered 
def main():
    #input number
    i = input("Enter numbers, seperate with ( space ) : ")
    #print input numbers
    print("Forward: ", i)
    #takes string of numbers
    items = i.split()
    #reverse the numbers
    items.reverse()
    #print reverse
    print("Backwards: ", items)

main()