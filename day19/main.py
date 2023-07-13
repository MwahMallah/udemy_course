from turtle import Turtle, Screen
import random

X_START = -230

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "grey"]

turtles = []

y_positions = [y_pos for y_pos in range(-70, 130, 30)]

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=X_START, y=y_positions[turtle_index])
    turtles.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0,6))
        if turtle.xcor() > -X_START:
            winning_turtle = turtle.pencolor().title()
            print(f"{winning_turtle} has won!")
            if winning_turtle == user_bet.title():
                print("You have won!")
            else:
                print("You lost!")
            is_race_on = False
            break

screen.exitonclick()
