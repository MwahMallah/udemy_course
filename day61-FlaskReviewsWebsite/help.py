import csv

with open("cafe-data.csv", "r", encoding='utf8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    next(csv_data)
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

    print(list_of_rows)