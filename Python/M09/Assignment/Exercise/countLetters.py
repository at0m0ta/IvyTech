'''
Liliana Varela-Rodriguez
04/01/2018
M09 14.5
'''
#importing all needed tools
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

def showResult():
    analyzeFile(filename.get())

def analyzeFile(filename):
    try:
        infile = open(filename, "r")

        letters = 26 * [0]
        for line in infile:
            countLetters(line.lower(), letters)
            infile.close()

        drawGraph(letters)

def countLetters(line, letters):
    for chr in line:
        if chr.isalpha():
            letters[ord(chr) - ord('a')] += 1

def openFile():
    fileRead = askopenfilename()
    filename.set(fileRead)
    
def drawGraph(count):
    canvas.delete("bar")
    wide = 400
    high = 400
    canvas.create_line(0, high-15, wide, high-15)

    barWidth = (wide-20) / len(count)
    unitHeight = (high-20) / max(count)

    for i in range(len(count)):
        height = count[i] * unitHeight

        canvas.create_rectangle(i * barWidth + 10, high-height-15, (i + 1) * barWidth + 10, high-15, tags = "bar")
        canvas.create_text((i + 1) * barWidth, high-5, text = chr(i + ord('a')), tags = "bar")

    window = Tk()
    window.title("Occurrence of Letters Histogram")

    size = 400
    canvas = Canvas(window, width = size, height = size)
    convas.pack()

    frame2 = Frame(window)
    frame2.pack()

    Label(frame2, text = "Enter a filename").pack(side = LEFT)
    filename = StringVar()

    Entry(frame2, width = 20, textvariable = filename).pack(side = LEFT)

    Button(frame2, text = "browse", command = openFile).pack(side = LEFT)
    Button(frame2, text = "Show Results", command = showResult).pack(side = LEFT)

    window.mainloop()
    









    
