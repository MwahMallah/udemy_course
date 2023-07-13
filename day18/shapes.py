from turtle import Turtle, Screen
import random

LEN_PATH = 150

timmy = Turtle()
timmy.shape("turtle")
timmy.color("slate blue")

colors = ["chartreuse", "orange", "firebrick", "tomato", "spring green", "navy", "steel blue"]
num_of_color = 0

for num_of_angles in range(3, 9):
    timmy.color(colors[num_of_color])
    num_of_color += 1

    current_angle = 360 / num_of_angles 
    for _ in range(num_of_angles):
        timmy.forward(LEN_PATH)
        timmy.right(current_angle)

screen = Screen()
screen.exitonclick()