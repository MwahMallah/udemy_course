from turtle import Turtle

STARTING_POSITION = (0, -280)
SPEED = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start_level()
        self.speed = SPEED

    def up(self):
        self.forward(self.speed)

    def start_level(self):
        self.goto(STARTING_POSITION)
