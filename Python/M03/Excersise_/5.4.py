'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 5.4
    
    02/10/2018
    
    '''
# 5.4 Conversion from miles to kilometers

print("{0:<15s}{1:>10s}".format("Miles", "Kilometers"))
# "{}{}" are place holders for miles and kilometers and inserts those strings
# "Miles" goes into index 0, aligning left (:<) and including the string will take up
# 15 spacesfor the string before starting "Kilometers" at index 1, aligning it to the right (:>)
# with 10 spaces available for the string

print("-----------------------------")
#this prints the line that seperates the column labels and the data

miles = 1
# starting off with the first line of miles and kilometers

while miles <= 10:
    # while there are at most 10 entries for miles
    
    print("{0:<15d}{1:>10f}".format(miles, miles * 1.609 ))
    miles += 1
# miles at 0 left aligned with 15 spaces, d = decimal int which is multiplied by 1.609
# to give, f = floating point value

