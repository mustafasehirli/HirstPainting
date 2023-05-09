
import random
import turtle
from turtle import Turtle, Screen

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make You Bet", prompt="Bir Renk Seç")
color = ["red", "yellow", "green", "purple", "orange", "blue"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_on = True
while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"you've winner {winner_color}")
            else:
                print(f"you've lost {winner_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()

