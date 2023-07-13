from turtle import Turtle
from typing import Tuple

UP = 90
SPEED = 20

class Paddle(Turtle):
    def __init__(self, start_position : Tuple) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.setheading(UP)
        self.start_position = start_position
        self.reset_pos()
        self.shape("square")
        self.shapesize(stretch_len=5)
    
    def up(self) -> None:
        self.forward(SPEED)

    def down(self) -> None:
        self.backward(SPEED)

    def reset_pos(self):
        self.goto(self.start_position)
