from turtle import Turtle
from typing import Tuple

FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.goto((-120, 200))
        self.write(f"{self.l_score}", font=("Courier", 50, "normal"))
        self.goto((100, 200))
        self.write(f"{self.r_score}", font=("Courier", 50, "normal"))

    def scored(self, scorer: str):
        if scorer == "l":
            self.l_score += 1
        else:
            self.r_score += 1

        self.clear()
        self.show_score()
