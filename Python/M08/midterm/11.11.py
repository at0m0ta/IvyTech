'''
Liliana Varela-Rodriguez
Midterm
11.11
'''
#11.11 Nine heads and tails

'''
(Game: nine heads and tails) Nine coins are placed in a 3 × 3 matrix with
some face up and some face down. You can represent the state of the coins
with the values 0 (heads) and 1 (tails).

Each state can also be represented using a binary number. For example,
the preceding matrices correspond to the numbers:

000010000 101001100 110100001 101110100 100111110

There are a total of 512 possibilities. So, you can use the decimal numbers 0 ,
1 , 2 , 3 , ..., and 511 to represent all states of the matrix.

Write a program that prompts the user to enter a number between 0 and 511 and
displays the corresponding 3 × 3 matrix with the characters H and T 
'''
#converting decimals to binary form
def fromDecToBin(number):
    binary = ''
    #while the number is greater than 0
    while number > 0:
        #getting the quotient and the remainder 
        binary = str((number % 2)) + binary
        number //=2
     #formatting the numbers by filling in remaining spaces with 0,
    #setting length of binary to 9 spaceces, then adding binary int to fill in space
    binary = '0'*(9-len(binary)) + binary
    return binary
   
    

def main():
    #user input
    number = int(input("Enter a number (0-511) to display the matrix: "))
    #calling from decimal to binary function
    binary = fromDecToBin(number)
    #putting binary into a list
    binary = list([int(x) for x in binary])

    
    #setting up 3x3 matrix and assigning t's and h's to elements in list
    final = ['T' if x==1 else 'H' for x in binary]
    for i in range(3):
        print("".join(final[i*3:(i+1)*3]))
main()


    
    
