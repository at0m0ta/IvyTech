'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M01 Programming Assignment 1.19
    
    01/28/2018
    
    '''

# 1.9 Turtle: draw a polygon

import turtle
turtle.showturtle()

turtle.penup()
turtle.color("red")

turtle.goto(40, -69.28)
turtle.pendown()
turtle.left(180)
turtle.goto(-40, -69.28)
turtle.right(60)

turtle.goto(-80, -9.8)
turtle.right(60)

turtle.goto(-40, 69)
turtle.right(60)

turtle.goto(40, 69)
turtle.right(60)

turtle.goto(80, 0)
turtle.right(60)
turtle.goto(40, -69.28)

turtle.penup()
turtle.goto(0,50)
turtle.done()

