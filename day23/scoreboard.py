from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.level = 0
        self.hideturtle()
        self.goto(x=-280, y=255)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-20, 0)
        self.write("Game over!", font=FONT)
