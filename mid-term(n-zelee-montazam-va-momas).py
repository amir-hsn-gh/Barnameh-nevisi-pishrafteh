import turtle

def n_zelee(zel_ha):
    if zel_ha <= 2:
        print("lotfan yek adade bozorg tar az 2 vared komid.")
        return

    rasm = turtle.Turtle()
    angle = 360 / zel_ha

    for _ in range(zel_ha):
        rasm.forward(100)
        rasm.left(angle)

    turtle.done()

n = int(input("yek adade bozorg tar az 2 vared komid: "))
n_zelee(n)