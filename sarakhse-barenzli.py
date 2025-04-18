import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("sarakhse barenzli")
screen.setup(800, 800)

fern = turtle.Turtle()
fern.speed(0)
fern.hideturtle()
fern.penup()

x, y = 0, 0

colors = ["#2e8b57", "#3cb371", "#20b2aa", "#66cdaa", "#8fbc8f"]

points = 50000

def transform1(x, y):
    return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6

def transform2(x, y):
    return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6

def transform3(x, y):
    return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

def transform4(x, y):
    return 0, 0.16 * y

def get_transform():
    r = random.random()
    if r < 0.01:
        return transform4
    elif r < 0.86:
        return transform1
    elif r < 0.93:
        return transform2
    else:
        return transform3

for _ in range(points):
    transform = get_transform()
    x, y = transform(x, y)
    
    fern.goto(x * 50, y * 50 - 250)
    fern.color(random.choice(colors))
    
    fern.dot(2)

turtle.done()