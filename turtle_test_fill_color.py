import turtle
from turtle import*

screen = turtle.Screen()
screen.setup(550,600,startx=0)
starty=10

t=turtle.Turtle()
t.penup()
t.goto(-250,150)
t.pendown()

t.speed(10)


def make_rectangle():
    t.fillcolor("white")
    t.begin_fill()
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.end_fill()


    
make_rectangle()
make_rectangle()
