import pandas

data = pandas.read_csv("./Squirrel_Data.csv")
gray_squirels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_squirels_count)
print(black_squirels_count)
print(cinnamon_squirels_count)

df = pandas.DataFrame({"Fur color":["Gray", "Black", "Cinnamon"], 
                  "Count":[gray_squirels_count, black_squirels_count, cinnamon_squirels_count]
                  })
df.to_csv("my_data.csv")
