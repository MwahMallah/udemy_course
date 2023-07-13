from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True

while is_on:
    request = input("What would you like? (espresso/latte/cappuccino): ")

    if request == 'report':
        coffee_machine.report()
        money_machine.report()
    elif request == 'off':
        is_on = False
    else:
        coffee = menu.find_drink(request)        

        if (not coffee is None) and coffee_machine.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_machine.make_coffee(coffee)
