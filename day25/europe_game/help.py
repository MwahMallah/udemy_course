import pandas

data = pandas.read_csv("europe_states.csv")
print(data[data["state"] == "Russia"]["x"].item())