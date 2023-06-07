'''
Liliana Varela
Midterm
10.7
'''

#10.7 Count single digits

'''
(Count single digits) Write a program that generates 1,000 random
integers between 0 and 9 and displays the count for each number.
(Hint: Use a list of ten integers, say counts , to store the counts for
the number of 0s, 1s, ..., 9s.)
'''

#getting random program
import random

#from 0 -9
fromRange = 10

#to generate 1,000 integers
totalNumbers = 1000

#table/matrix
table = []

#for the i in the range of total numbers
for i in range(totalNumbers):
    #getting random integer from matrix/table
    table.append(random.randint(0, fromRange-1))
    
#making 10 rows/lists using counts 
counts = 10 * [0]

#for i in the range of the length of the table
for i in range(len(table)):
    #get each lists(counts) in the table,
    #read each individual integer (i) and go to the next  
    counts[table[i]-1] += 1
    
#for i in the range of the length of the lists (counts --> fromRange)
for i in range(len(counts)):
    #print the number of times each appears
    print("The numbers ", i, " appear ", counts[i], " times")





    
