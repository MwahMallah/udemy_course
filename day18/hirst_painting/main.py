import turtle as t
import random

t.colormode(255)

LEN = 50
X_DOTS = 10
Y_DOTS = 10

color_list = [(236, 80, 224), (197, 71, 7), (195, 13, 164), (201, 15, 75), (231, 132, 54), (110, 216, 179)]

timmy = t.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed(0)
timmy.sety(-250)
timmy.setx(-250)

for y in range(Y_DOTS):
    for x in range(X_DOTS): 
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.forward(LEN)
        timmy.dot(20)
    timmy.left(90)
    timmy.forward(LEN)
    timmy.left(90)
    timmy.forward(LEN*X_DOTS)
    timmy.left(180)


screen = t.Screen()
screen.exitonclick()