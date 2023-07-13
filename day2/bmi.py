#!/usr/bin/python3

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2

print(f"Your bmi is: {int(bmi)}")