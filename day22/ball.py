from turtle import Turtle
import random
import math

SPEED = 25

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.move_speed = 0.1
        self.setheading(40)
        self.reset_position()

    def move(self):
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)
    
    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_speed = random.randint(0, SPEED)
        self.y_speed = math.sqrt(SPEED ** 2 - self.x_speed ** 2)



