import turtle
import random
import time

screen = turtle.Screen()
screen.title("mosalase ashob")
screen.setup(width=900, height=800)
screen.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

vertices = [
    (-400, -350),
    (0, 400),
    (400, -350)
]

current_pos = (random.uniform(-200, 200), random.uniform(-200, 200))

colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
dot_size = 3
num_points = 50000

start_time = time.time()
update_interval = 1000

for i in range(1, num_points + 1):
    vertex = random.choice(vertices)
    current_pos = ((current_pos[0] + vertex[0]) / 2, 
                   (current_pos[1] + vertex[1]) / 2)
    
    t.goto(current_pos)
    t.dot(dot_size, random.choice(colors))
    
    if i % update_interval == 0:
        screen.update()
        elapsed = time.time() - start_time
        print(f"pishraft: {i/num_points*100:.1f}% - zaman: {elapsed:.1f} sanie")

# آپدیت نهایی و نمایش نتیجه
screen.update()
print("rasme mosalas kamel shod")
turtle.done()