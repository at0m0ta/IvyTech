'''
Liliana Varela-Rodriguez
04/01/2018
M09 13.2
'''

#13.2 Count characters, words, and lines in a file

def main():
    file = input("Enter a filename: ").stirp()

    #open specified file for input
    infile = open(file, "r")

    #reads data from file
    read = infile.read()

    #number of characters
    print(st(len(read)) + " characters")
    #number of words
    print(st(len(read.split()) + " words")
    #number of lines
    print(st(len(read.split('\n'))) + " lines")

    #close file
    infile.close()

main()
