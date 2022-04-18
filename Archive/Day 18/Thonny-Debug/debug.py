from turtle import Turtle, Screen, shape
import random

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()


mrtumble = Turtle()

mrtumble.shape("turtle")
mrtumble.color("green")
screen = Screen()
screen.colormode(255)

def draw_shape(num_sides):
    for _ in (num_sides):
        angle = 360 / num_sides
        mrtumble.forward(100)
        mrtumble.left(angle)

for shape_side_n in range(3, 11):
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    mrtumble.pencolor((r, g, b))
    draw_shape(shape_side_n)
 
    


screen.exitonclick()
  