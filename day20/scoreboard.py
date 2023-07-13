from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.speed("fastest")
        self.goto(x=0, y=262)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.get_data_score()
        self.show_score()
        
    def update_score(self, amount):
        self.score += amount
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            
        self.score = 0
        self.show_score()

    def get_data_score(self):
        with open("data.txt") as data:
            self.highest_score = int(data.read())