STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.gotostart()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def move_left(self):
        pass

    def move_right(self):
        pass

    def gotostart(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False