'''
Liliana Varela
M10
04/08/2018
'''
#15.13
def UppercaseCounter(s, high):
    #if there are no string characters then return 0
    if not s:
        return 0
    #else if there are Uppercase chrcts add 1 per string character is upper
    else:
        upper = UppercaseCounter(s[1:], high - 1)
        if s[0].isupper():
            return upper + 1
        #do not return lower case string, only upper
        else:
            return upper
        
def countUpper(s):
    #call uppercase counter string
    return UppercaseCounter(s, len(s) - 1)

def main():
    s = input("Enter a string: ")
    print("The string " + s + " has " + str(countUpper(s)) + " upper case letters!")

main()
