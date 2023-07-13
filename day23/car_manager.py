from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 10

class Car(Turtle):
    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.goto(x=x_pos, y=y_pos)
        self.setheading(180)
        self.driving_speed = STARTING_MOVE_DISTANCE

    def drive(self):
        self.forward(self.driving_speed)


class CarManager():
    def __init__(self) -> None:
        self.cars = []
        
    def make_car(self):
        self.cars.append(Car(x_pos=random.randint(320, 960), y_pos=random.randint(-250, 250)))

    def drive_cars(self):   
        for car in self.cars:
            car.drive()

    def delete_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.clear()
                car.hideturtle()

    def delete_all_cars(self):
        for car in self.cars:
            car.clear()
            car.hideturtle()
        self.cars.clear()

