import turtle
import random

turtle.setup(1000,1000)
t = turtle.Turtle()
#screen = t.     Screen(1000,1000)
t.speed(20)
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

for _ in range(180):
    t.pencolor(random_color())
    t.left(2)
    t.circle(100)


screen.exitonclick()
  