##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime
import random
import os
import smtplib

def make_letter():
    file_template = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{file_template}") as letter_template:
        letter = letter_template.read()
    return letter
     
user = "maksim0dubrovin0@gmail.com"
with open("password.txt", mode="r") as file:
    password = file.read()

# 1. Update the birthdays.csv
bd_data = (pd.read_csv("birthdays.csv")).to_dict(orient='records')
today = datetime.datetime.now()

for bd in bd_data:
    if bd["month"] == today.month and bd["day"] == today.day:
        letter = make_letter().replace("[NAME]", bd['name'])
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user, to_addrs=bd['email'], msg=f"Subject:Happy Birthday!!!\n\n{letter}")






