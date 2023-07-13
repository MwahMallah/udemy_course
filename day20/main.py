from turtle import Screen, Turtle
import time
import random
from scoreboard import Scoreboard
from snake import Snake
from food import Food
# from tower import Tower

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

turn_off_boundaries = screen.textinput(title="Choose mode", prompt="Turn off boundaries?: ")

snake = Snake()
food  = Food()
scoreboard = Scoreboard()
towers = []

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.update_score(1)

        # if scoreboard.score % 3 == 0:
        #     new_tower = Tower(snake_head=snake.head)
        #     towers.append(new_tower)

    if turn_off_boundaries == "yes":
        if snake.head.xcor() > 290:
            snake.head.setx(-290)
        if snake.head.xcor() < -290:
            snake.head.setx(290)
        if snake.head.ycor() > 290:
            snake.head.sety(-290)
        if snake.head.ycor() < -290:
            snake.head.sety(290)
    else:
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            time.sleep(2)
            scoreboard.reset()
            snake.reset()
    

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset() 
            snake.reset()
            time.sleep(2)

    # for tower in towers:
    #     if snake.head.distance(tower) < 20:
    #         is_game_on = False
    #         scoreboard.game_over()

screen.exitonclick()
