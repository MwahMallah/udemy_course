import turtle
import pandas

screen = turtle.Screen()
screen.title("Europe map game")
screen.addshape("europe_map.gif")
turtle.shape("europe_map.gif")

country_pen = turtle.Turtle()
country_pen.penup()
country_pen.hideturtle()

data = pandas.read_csv("europe_states.csv")

correct_countries = []
while len(correct_countries) < 35:
    guessed_country = screen.textinput(title=f"{len(correct_countries)}/35 Countries Correct", prompt="What's another country name?: ").title()

    if guessed_country == "Exit":
        break

    if guessed_country in data.state.tolist():
        x,y = data[data["state"] == guessed_country].x.item(), data[data["state"] == guessed_country].y.item()
        country_pen.goto(x, y)
        country_pen.write(guessed_country)
        correct_countries.append(guessed_country)

countries_in_file = data["state"].tolist()
missing_countries_list = []
for country in countries_in_file:
    if country not in correct_countries:
        missing_countries_list.append(country)

added_countries = pandas.DataFrame(missing_countries_list)
added_countries.to_csv("guessed_countries.csv")

turtle.mainloop()