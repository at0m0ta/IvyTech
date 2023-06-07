'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Exercises 4.15
    
    01/27/2018
    
    '''
# 4.15 Game: lottery

import random

guess = eval(input("Enter your lottery pick (three digits): "))

lottery = random.randint(0, 999)

lotto1 = lottery // 100
lotto2 = (lottery % 100) // 10
lotto3 = ((lottery % 100) % 10)

dig1 = guess // 100
dig2 = (guess % 100) // 10
dig3 = ((guess % 100) % 10)

if guess == lottery:
    print("Your number is ", guess, ".", "The lottery number is ", lottery, ".", \
          "Exact match! You win $10,000! ")
elif (dig1 == lotto1 and dig2 == lotto2 and dig3 == lotto3):
    print("Your number is ", guess, ".", "The lottery number is ", lottery, ".", \
          "All digits match! You win $3, 000! ")
elif (dig1 == lotto1 \
      or dig1 == lotto2 \
      or dig1 == lotto3 \
      or dig2 == lotto1 \
      or dig2 == lotto2 \
      or dig2 == lotto3 \
      or dig3 == lotto1 \
      or dig3 == lotto2 \
      or dig3 == lotto3):
    print("Your number is ", guess, ".", "The lottery number is ", lottery, ".", \
          "You matched 1 digit! You win $1,000! ")
else:
    print("Your number is ", guess, ".", "The lottery number is ", lottery, ".", \
           "Sorry, no match.")

      
