import random
import turtle
turtle.setup(1000,1000)
t = turtle.Turtle()
t.speed(20)
turtle.colormode(255)
 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


#color = ['red', 'green', 'blue', 'orange', 'white', 'purple', 'pink', 'brown']
t.pensize(10)
distance = [10,20,30,40,50]
directions = [0, 90, 180, 270]

for _ in range(200):
    t.pencolor(random_color())
    t.forward(random.choice(distance))
    t.setheading(random.choice(directions))
