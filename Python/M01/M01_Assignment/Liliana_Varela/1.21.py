'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M01 Programming Assignment 1.21
    
    01/28/2018
    
    '''
# 1.21 Turtle: display a clock

import turtle
turtle.showturtle()
turtle.color("red")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(175)


turtle.pendown()
turtle.circle(175)
turtle.penup()
turtle.left(90)
turtle.back(15)
turtle.pendown()
turtle.write("9:15:00")

turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.write("6")
turtle.penup()
turtle.forward(50)
turtle.forward(100)

turtle.left(90)
turtle.pendown()
turtle.color("black")
turtle.forward(70)
turtle.penup()
turtle.forward(80)
turtle.color("red")
turtle.pendown()
turtle.write("9")
turtle.penup()
turtle.back(150)

turtle.right(90)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.forward(65)
turtle.pendown()
turtle.write("12")
turtle.penup()
turtle.back(165)

turtle.right(90)
turtle.color("grey")
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.color("red")
turtle.pendown()
turtle.write("3")
turtle.penup()
turtle.back(150)




