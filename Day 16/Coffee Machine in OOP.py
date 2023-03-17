from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
over  = False

def display_report():
    coffee_maker.report()
    money_machine.report()

def prompt(choice):
    if choice ==  "report":
        display_report()
        return False
    elif choice == "off":
        return True
    else:
        found = menu.find_drink(choice)
        if found:
            sufficient = coffee_maker.is_resource_sufficient(found)
            if sufficient:
                enough_money = money_machine.make_payment(found.cost)
                if enough_money:
                    coffee_maker.make_coffee(found)

while not over:
    choices = menu.get_items()
    choice = input(f"What would you like? ({choices}): ")
    over = prompt(choice)