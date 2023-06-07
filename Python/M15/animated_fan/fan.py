'''
Liliana Varela
02/02/2018
PYTHON Module 5
Assignment Chapter 9

'''

#9.16 (Display running fan)

#import tkinter
from tkinter import *

#circle attributes
width = 200
height = 200
radius = 80

#setting up display for fan
class MainGUI:
    def __init__(self):
        #window and title
        window = Tk()
        window.title("Moving Fan")
        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()

        #startingAngle will begin at position 0
        self.startingAngle = 0

        #running while loop to begin fan
        while True:
            #everytime we go through loop, increase startingAngle by 5
            self.startingAngle += 5
            #displays fan at wherever startingAngle is positioned
            self.displayFan(self.startingAngle)
            #after 88 milliseconds rest
            self.canvas.after(88)
            #updates startingAngle's position
            self.canvas.update()

        window.mainloop()

    def displayFan(self, startingAngle):
        self.canvas.delete("Fan")

        #create fan arc(x0, y0, x1, y1, option, option, option, option)
        self.canvas.create_arc(width / 2 - radius,
                               height / 2 - radius,
                               width / 2 + radius,
                               height / 2 + radius,
                               #begin at starting angle
                               start = self.startingAngle + 0,
                               extent = 30,
                               fill = "red",
                               tags = "fan")
        #step2
        self.canvas.create_arc(width / 2 - radius,
                               height / 2 - radius,
                               width / 2 + radius,
                               height / 2 + radius,
                               #increasing starting angle by 90
                               start = self.startingAngle + 90,
                               extent = 30,
                               fill = "red",
                               tags = "fan")
        #step3
        self.canvas.create_arc(width / 2 - radius,
                               height / 2 - radius,
                               width / 2 + radius,
                               height / 2 + radius,
                               #increase starting angle by 180 
                               start = self.startingAngle + 180,
                               extent = 30,
                               fill = "red",
                               tags = "fan")
        #step4
        self.canvas.create_arc(width / 2 - radius,
                               height / 2 - radius,
                               width / 2 + radius,
                               height / 2 + radius,
                               #increase by starting angle by 270
                               start = self.startingAngle + 270,
                               extent = 30,
                               fill = "red",
                               tags = "fan")

MainGUI()


        
