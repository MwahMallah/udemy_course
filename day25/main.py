# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# max = data["temp"].max()
# print(max)
# print(data[data.day == "Monday"])
# maximum_temp_day = data[data.temp == data.temp.max()]

# monday = data[data.day == "Monday"]
# monday_temp_F = monday.temp * 9 /5 + 32 

# print(monday_temp_F)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
