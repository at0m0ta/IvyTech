'''
Liliana Varela-Rodriguez
M07 Chapter 11
11.9 Tic Tac Toe
'''

#11.9 TicTacToe
def main():
#creating matrix
choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))
    
#setting boolean statements, these will change as program runs
playerOneTurn = True
winner = False

#tictactoe board
def printBoard() :
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')
#while there is still no winner...
while not winner :
    printBoard()
    #if it is player 1's turn print player 1
    if playerOneTurn :
        print( "Player 1:")
        
        #else print player 2
    else :
        print( "Player 2:")

    try:
        choice = int(input("Enter  "))

    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("Try another move!")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
main()
