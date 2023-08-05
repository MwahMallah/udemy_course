import datetime as dt
import random
import smtplib

today = dt.datetime.now()
user = "maksim0dubrovin0@gmail.com"
to_addr = "maksimdubrovin@yahoo.com"

with open("password.txt", mode="r") as file:
    password = file.read()

with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()

if today.weekday() == 4:
    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user, to_addrs=to_addr, msg=f"Subject:Hello\n\n{quote}")