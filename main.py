from menu import Menu, MenuItem
from coffer-maker import CofferMaker
from money_machine import Moneymachine

money_machine = Moneymachine()
coffee-maker = CofferMaker()
menu = Menu()

is_on = True

while is_on:
    choice = input("​What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee-maker.report()
        money_machine.report()
    else:
        drink = menu.find_drik(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
            if is_enough_ingredients and is_payment_successful:
                coffee_make.make_coffee(drink)
