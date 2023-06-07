'''
Liliana Varela-Rodriguez
04/01/2018
M09 14.2
'''

#14.2 Count occurrences of numbers

def main():
    #enter string of numbers
    s = input("Enter the numbers: ").strip()
    #evaluate the numbers inside the string
    numbers = [eval(x) for x in s.split()]

    #create a dictionary to store string/number pairs
    dictionary = {}

    for numbers in numbers:
        #if the number is in dictionary already add 1 to that number
        if number in dictionary:
            dictionary[number] += 1
        #if the number is not in dictionary then make it equal to 1
        else:
            dictionary[number] = 1

    #getting the number with the maxium occurences in dictionary
    maxVal = max(dictionary.values())

    #get pairs
    pairs = list(dictionary.items())
    reverse = [[x, y] for (x, y) in pairs]

    #display number with max occurences
    print("The numbers with the most occurrences are: ", end = "")
    for (x, y) in reverse:
        if y == maxVal:
            print(x, end = " ")

    main()
