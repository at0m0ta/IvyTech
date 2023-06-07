'''
Liliana Varela
03/04/2018
Module 5 CH 9
Excersise 9.3
'''

#9.3 Select geometric figures

from tkinter import *

#Setting up your interface
class geometricFig:
#creating window
    def __init__(self):
        window = Tk()
        window.title("Select and Fill")
        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()
        #rectangle frame option
        frame = Frame(window)
        frame.pack()
        
        self.v1 = StringVar()
        rect = Radiobutton(frame,
                             text = "Rectangle",
                             command = self.shapeFill,
                             variable = self.v1,
                             value = '1')
        #oval frame option
        oval = Radiobutton(frame,
                             text = "Oval",
                             command = self.shapeFill,
                             variable = self.v1,
                           #new value will allow us to toggle back to rectangle
                             value = '2')
        #frame for fill check
        self.v2 = StringVar()
        cbtFill = Checkbutton(frame, text = "Fill",
                              command = self.shapeFill,
                              variable = self.v2)
        #placing widgets within a grid on GUI
        rect.grid(row=1, column = 1)
        oval.grid(row=1, column = 2)
        cbtFill.grid(row=1, column = 3)
        #call the mainloop
        window.mainloop()
    #display rectangle
    def DisplayRect(self):
        self.canvas.delete("rect", "oval")
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
    #display oval
    def DisplayOval(self):
        self.canvas.delete("rect", "oval")
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "oval")
    #fill process
    def shapeFill(self):
        self.canvas.delete("rect", "oval")
        #white fill if self.ve is 0 (false), else color is red
        color = "white" if self.v2.get() == "0" else "red"
        #if self.ve is 1 (true) and rectangle, fill 
        if self.v1.get() == '1' :
            self.canvas.create_rectangle(10, 10, 190, 90,
                                         tags = "rect",
                                         fill = color)
        #if self.v1 is 1 (true) and oval, fll           
        else:
            self.canvas.create_oval(10, 10, 190, 90,
                                    tags = "oval",
                                    fill = color)
geometricFig()

        
        
