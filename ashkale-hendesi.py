import turtle as t
import random as r
import time as tm
import math as m

class Forme:
    def __init__(self, typ, max_hp, spd, rival_types, col, size):
        self.obj = t.Turtle()
        self.obj.speed(0)
        self.obj.penup()

        self.typ = typ
        self.hp = max_hp
        self.spd = spd
        self.rivals = rival_types
        self.size = size

        self.obj.shape("circle")
        self.obj.shapesize(*size)
        self.obj.color(col)

        ang = r.uniform(0, 360)
        rad = m.radians(ang)
        self.dx = m.cos(rad) * spd
        self.dy = m.sin(rad) * spd

    def motion(self):
        self.obj.goto(self.obj.xcor() + self.dx, self.obj.ycor() + self.dy)

    def boundary_check(self):
        w = t.window_width() // 2 - 20
        h = t.window_height() // 2 - 20
        if abs(self.obj.xcor()) > w:
            self.dx *= -1
        if abs(self.obj.ycor()) > h:
            self.dy *= -1

    def overlap(self, other):
        dist = self.obj.distance(other.obj.pos())
        threshold = (self.size[0] + other.size[0]) * 10
        return dist < threshold

class Box(Forme):
    def __init__(self):
        super().__init__(
            typ='sq',
            max_hp=4,
            spd=2,
            rival_types=['ci'],
            col='red',
            size=(1.5, 1.5, 1)
        )
        self.obj.shape("square")

class Pyramid(Forme):
    def __init__(self):
        super().__init__(
            typ='tr',
            max_hp=3,
            spd=2.5,
            rival_types=['ci'],
            col='green',
            size=(1.3, 1.3, 1)
        )
        self.obj.shape("triangle")

class Bar(Forme):
    def __init__(self):
        super().__init__(
            typ='rt',
            max_hp=5,
            spd=1.8,
            rival_types=['sq'],
            col='blue',
            size=(2.0, 1.0, 1)
        )
        self.obj.shape("square")

class Sphere(Forme):
    def __init__(self):
        super().__init__(
            typ='ci',
            max_hp=6,
            spd=2.2,
            rival_types=['rt'],
            col='yellow',
            size=(1.0, 1.0, 1)
        )
        self.obj.shape("circle")

class Simulation:
    def __init__(self):
        self.entities = []
        self.initialize_screen()
        self.spawn_entities()

    def initialize_screen(self):
        self.scn = t.Screen()
        self.scn.title("Simulation")
        self.scn.setup(width=800, height=600)
        self.scn.bgcolor("white")
        self.scn.tracer(0)

    def spawn_entities(self):
        for cls in (Box, Pyramid, Bar, Sphere):
            for _ in range(r.randint(3, 7)):
                entity = cls()
                entity.obj.goto(r.randint(-350, 350), r.randint(-250, 250))
                self.entities.append(entity)

    def resolve_collisions(self):
        removals = set()
        for i in range(len(self.entities)):
            for j in range(i + 1, len(self.entities)):
                e1 = self.entities[i]
                e2 = self.entities[j]
                if e1.overlap(e2):
                    if e2.typ in e1.rivals:
                        e2.hp -= 1
                    elif e1.typ in e2.rivals:
                        e1.hp -= 1
                    e1.dx, e1.dy = -e1.dx, -e1.dy
                    e2.dx, e2.dy = -e2.dx, -e2.dy

                    if e1.hp <= 0:
                        removals.add(e1)
                    if e2.hp <= 0:
                        removals.add(e2)

        for rem in removals:
            rem.obj.hideturtle()
            if rem in self.entities:
                self.entities.remove(rem)

    def execute(self):
        try:
            while self.entities:
                self.scn.update()
                for ent in self.entities:
                    ent.motion()
                    ent.boundary_check()
                self.resolve_collisions()
                tm.sleep(0.01)
            print("Simulation Over!")
        except t.Terminator:
            pass
        finally:
            t.bye()

if __name__ == "__main__":
    Simulation().execute()