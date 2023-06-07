'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Exercises 3.14
    
    01/27/2018
    
    '''
# 3.14 Turtle: draw the Olympic symbol

import turtle

radius = eval(input("Enter the radius for the circle: "))

turtle.showturtle()
turtle.pensize(10)

turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(radius)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(radius)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(radius)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(radius)

turtle.done()
