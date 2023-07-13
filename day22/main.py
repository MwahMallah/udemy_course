from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 800
L_PADDLE_POS = (-350, 0)
R_PADDLE_POS = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(L_PADDLE_POS)
r_paddle = Paddle(R_PADDLE_POS)
ball = Ball()
scoreboard = Scoreboard()

key_states = {
    "Up" : False,
    "Down" : False,
    "w" : False,
    "s" : False,
}

def check_keys():
    if key_states["Up"] and r_paddle.ycor() < HEIGHT/2 - 70:
        r_paddle.up()
    if key_states["Down"] and r_paddle.ycor() > -HEIGHT/2 + 70:
        r_paddle.down()

    if key_states["w"] and l_paddle.ycor() < HEIGHT/2 - 70:
        l_paddle.up()
    if key_states["s"] and l_paddle.ycor() > -HEIGHT / 2 + 70:
        l_paddle.down()

def key_press(key: str):
    key_states[key] = True
    check_keys()

def key_release(key: str):
    key_states[key] = False
    check_keys()

screen.listen()

screen.onkeypress(key="Up", fun=lambda: key_press("Up"))
screen.onkeypress(key="Down", fun=lambda: key_press("Down"))
screen.onkeypress(key="w", fun=lambda: key_press("w"))
screen.onkeypress(key="s", fun=lambda: key_press("s"))

screen.onkeyrelease(key="Up", fun=lambda: key_release("Up"))
screen.onkeyrelease(key="Down", fun=lambda: key_release("Down"))
screen.onkeyrelease(key="w", fun=lambda: key_release("w"))
screen.onkeyrelease(key="s", fun=lambda: key_release("s"))

# screen.onkey(key="Up", fun=r_paddle.up)
# screen.onkey(key="Down", fun=r_paddle.down)
# screen.onkey(key="w", fun=l_paddle.up)
# screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > HEIGHT / 2 - 15 or ball.ycor() < -HEIGHT / 2 + 15:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.scored("l")
        time.sleep(2)
        l_paddle.reset_pos()
        r_paddle.reset_pos()
        ball.reset_position()

    elif ball.xcor() < -380:
        scoreboard.scored("r")
        time.sleep(2)
        l_paddle.reset_pos()
        r_paddle.reset_pos()
        ball.reset_position()
        

screen.exitonclick()