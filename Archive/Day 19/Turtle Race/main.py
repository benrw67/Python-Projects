from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["Ben", "Claire", "Lilie", "Drew", "Poppy", "Lockie"]
location = 150
turtle_names=[]

for turtle_index in range(0, 6):
    name = random.choice(names)
    names.remove(name)
    name = Turtle(shape="turtle")
    name.penup()
    turtlecolor = random.choice(colors)
    colors.remove(turtlecolor)
    name.color(turtlecolor)
    name.goto(-240, location)
    location -= 50
    turtle_names.append(name)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_names:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        random_distance = random.randint(0, 6)
        turtle.forward(random_distance)

screen.exitonclick()