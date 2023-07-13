MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def make_coffee(coffee_name: str) -> None:
    for ingredient in MENU[coffee_name]["ingredients"]:
        if MENU[coffee_name]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return
    
    quarters = int(input("how many quarters?: "))*0.25
    dimes = int(input("how many dimes?: "))*0.10
    nickels = int(input("how many nickles?: "))*0.05 
    pennies = int(input("how many pennies?: "))*0.01
    money_given = quarters + dimes + nickels + pennies

    if money_given < MENU[coffee_name]['cost']:
        print("Sorry that's not enough money. Money refunded.")

    else: 
        for ingredient in MENU[coffee_name]["ingredients"]:
            resources[ingredient] -= MENU[coffee_name]["ingredients"][ingredient]

        resources["money"] += MENU[coffee_name]['cost']
        print(f"Here is {money_given - MENU[coffee_name]['cost']:.1f}$ in change.\nHere is your {coffee_name} 🍵. Enjoy!")
        

def menu():
    while True:
        request = input("What would you like? (espresso/latte/cappuccino): ")
        if request == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {resources['money']}$")
        elif request in MENU:
            make_coffee(request)


menu()
