'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M01 Programming Exercises 2.23
    
    01/28/2018
    
    '''
#2.23 Turtle: draw four circles

import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(25,0)
turtle.pendown()
turtle.circle(25)

turtle.penup()
turtle.goto(-25,0)
turtle.pendown()
turtle.circle(25)

turtle.penup()
turtle.goto(-25, -50)
turtle.pendown()
turtle.circle(25)

turtle.penup()
turtle.goto(25, -50)
turtle.pendown()
turtle.circle(25)

turtle.done()
