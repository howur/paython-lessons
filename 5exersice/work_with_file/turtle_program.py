import turtle
from turtle import*

screen = turtle.Screen()
screen.setup(550,600,starx=0)
starty=10
t=turtle.Turtle()

t.penup()
t.goto(-250,150)
t.pendown()

t.color("black")
t.begin_full()

t.begin_fill()
t.right(270)
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)

t.color("blue")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.end_fill()
t.forward(100)


