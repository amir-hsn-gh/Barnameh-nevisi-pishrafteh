import math

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return (root1, root2), "2 risheh haghighi"
    elif delta == 0:
        root = -b / (2*a)
        return (root,), "1 risheh haghighi"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-delta) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2), "risheh haghighi nadarad"

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

roots, message = solve_quadratic(a, b, c)
print("risheh ha:", roots)
print("natigeh:", message)