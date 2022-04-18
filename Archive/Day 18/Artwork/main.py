import turtle as t
import random as rd

tim = t.Turtle()
screen = t.Screen()
screen.canvwidth = 500
screen.canvheight = 500
tim.speed("fastest")
t.colormode(255)
tim.hideturtle()
screen.reset()
screen.setworldcoordinates(-50, -50, 500, 500)

def reset_line_position():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.setx(0)
    tim.left(180)

def create_art():
    for _ in range(10):
        tim.penup()
        tim.dot(20, random_color())
        if _ < 9:
            tim.forward(50)

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    random_color = (r, g, b)
    return random_color

#for _ in range(180):
##    t.pencolor(random_color())
#    t.left(2)
 #   t.circle(100)

end_of_canvas = 1
while end_of_canvas < 11:
    create_art()
    if end_of_canvas < 10:
        reset_line_position()
    end_of_canvas +=1

screen.exitonclick()
  