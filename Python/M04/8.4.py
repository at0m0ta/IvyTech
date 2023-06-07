'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 8.4
    
    02/10/2018
    
    '''
# 8.4 Occurrences of a specified character

def main ():
    s1 = input("Enter a string: ").strip()
    char = input("Enter a character to see how many times \
it repeats in the string: ").strip()

    print(CharCount(s1, char))

def CharCount(s1, char):
    CharCount = 0
    for x in s1:
        if char == x:
            CharCount += 1
    return CharCount
main()
