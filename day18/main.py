import turtle as t
import random
from typing import Tuple

NUM_CIRCLES = 70
FULL_ANGLE = 360
RADIUS = 100

def random_color() -> Tuple:
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

angles = [90, 180, 270, 360]
t.colormode(255)

timmy = t.Turtle()
timmy.width(2)
timmy.speed(0)

for _ in range(NUM_CIRCLES):
    timmy.color(random_color())
    timmy.circle(RADIUS)
    timmy.right(FULL_ANGLE / NUM_CIRCLES)

screen = t.Screen()
screen.exitonclick()