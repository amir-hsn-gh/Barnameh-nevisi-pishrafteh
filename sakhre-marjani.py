import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("midnightblue")
screen.title("sakhre marjani")

coral = turtle.Turtle()
coral.hideturtle()
coral.speed(0)
coral.width(2)
coral.color("lightcoral")

coral_colors = ["lightcoral", "plum", "salmon", "tomato", "violet", "orchid"]

def draw_branch(t, length, angle, depth):
    if depth == 0 or length < 5:
        return

    t.color(random.choice(coral_colors))
    curve = 10

    for i in range(10):
        offset = math.sin(i / 2) * 2
        t.forward(length / 10)
        t.left(offset)

    t.left(angle)
    draw_branch(t, length * 0.75, angle, depth - 1)
    t.right(angle * 2)
    draw_branch(t, length * 0.75, angle, depth - 1)
    t.left(angle)

    for i in range(10):
        offset = math.sin((10 - i) / 2) * 2
        t.backward(length / 10)
        t.right(offset)

coral.penup()
coral.goto(0, -250)
coral.setheading(90)
coral.pendown()

draw_branch(coral, length=100, angle=30, depth=5)

def draw_side_coral(x_offset):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.width(2)
    t.color("lightcoral")
    t.penup()
    t.goto(x_offset, -250)
    t.setheading(90)
    t.pendown()
    draw_branch(t, length=70, angle=25, depth=4)

draw_side_coral(-100)
draw_side_coral(100)

screen.mainloop()