from turtle import Screen, left
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_pad = Paddle((-350, 0))
right_pad = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_pad.go_up, "Up")
screen.onkey(right_pad.go_down, "Down")
screen.onkey(left_pad.go_up, "w")
screen.onkey(left_pad.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(right_pad) < 50 and ball.xcor() > 350 or ball.distance(left_pad) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #Detect Paddle Missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()