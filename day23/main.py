from turtle import Turtle, Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.up, key="Up")

game_is_on = True

iteration = 0

while game_is_on:
    screen.update()

    if iteration == 6:
        car_manager.make_car()
        iteration = 0

    iteration += 1
    car_manager.drive_cars()
    car_manager.delete_cars()
    
    time.sleep(0.1)

    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 290:
        scoreboard.update_level()
        car_manager.delete_all_cars()
        player.start_level()

screen.exitonclick()