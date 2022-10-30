import turtle
from turtle import*

def make_rectangle(color,width,height):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def go_down(height):
    t.right(90)
    t.forward(height)
    t.left(90)



screen = turtle.Screen()
screen.setup(1000,600,startx=0)
starty=10

t=turtle.Turtle()
t.penup()
t.goto(-250,150)
t.pendown()

t.speed(5)

t.color("black")
t.color("black")
t.begin_fill()

a = 800
b = 300

make_rectangle("white",a,b)
go_down(b)
make_rectangle("blue",a,b)
go_down(b)
make_rectangle("red",a,b)



