import json

my_details = {
    "Name" : "Lalit Salunkhe",
    "Age" : 28,
    "Job" : True,
    "Married" : False,
    "Bikes" : [
        {"Model1": "Jupiter 120", "price": 62000},
        {"Model2": "Yamaha YZF-R15", "price": 150000}
        ]
}

print(json.dumps(my_details, indent = 3, sort_keys=True))