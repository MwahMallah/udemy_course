from turtle import Turtle
import random

class Tower(Turtle):
    def __init__(self, snake_head) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("red")

        if snake_head.xcor() < 0:
            x_pos = random.randint(int(snake_head.xcor()) + 40, 280)
        else:
            x_pos = random.randint(-280, int(snake_head.xcor()) - 40)
        if snake_head.ycor() < 0:
            y_pos = random.randint(int(snake_head.ycor()) + 40, 280)
        else:
            y_pos = random.randint(-280, int(snake_head.ycor()) - 40)

        self.goto(x_pos, y_pos)
            