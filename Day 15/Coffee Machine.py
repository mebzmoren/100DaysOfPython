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
}

done = False
money = 0
user_money = 0

def menu_prompt():
    order = input(f"What would you like? (espresso/latte/cappuccino): ")
    return order
    
def check_resources(order):
    if order == "espresso":
        if MENU[order]['ingredients']['water'] > resources["water"]:
            print("Sorry not enough water.")
            return False
        elif MENU[order]['ingredients']['coffee'] > resources["coffee"]:
            print("Sorry not enough coffee.")
            return False
        else:
            return True
    elif order == "latte" or order == "cappuccino":
        if MENU[order]['ingredients']['water'] > resources["water"]:
            print("Sorry not enough water.")
            return False
        elif MENU[order]['ingredients']['milk'] > resources["milk"]:
            print("Sorry not enough milk.")
            return False
        elif MENU[order]['ingredients']['coffee'] > resources["coffee"]:
            print("Sorry not enough coffee.")
            return False
        else:
            return True
        
def process_money(user_money):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    user_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return user_money
    
def check_money(order, user_money):
    user_money = process_money(user_money)
    if MENU[order]['cost'] < user_money:
        change = user_money - MENU[order]['cost']
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

def check_prompt(order, user_money):
    if order == "report":
        for key in resources:
            if key == "coffee":
                suffix = "g"
            else:
                suffix = "ml"
            print(f"{key.title()}: {resources[key]}{suffix}")
        print(f"Money: ${money}")
        return False
    elif order == "off":
        return True
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        enough_resources = check_resources(order)
        if enough_resources == True:
            enough_money = check_money(order, user_money)
            if enough_money == True:
                return False
            
def make_coffee(order, dictionary, available, money):
    if order == 'espresso':
        available['water'] -= dictionary[order]['ingredients']['water']
        available['coffee'] -= dictionary[order]['ingredients']['coffee']
        money += dictionary[order]['cost']
        return money
    elif order == "latte" or order == "cappuccino":
        available['water'] -= dictionary[order]['ingredients']['water']
        available['milk'] -= dictionary[order]['ingredients']['milk']
        available['coffee'] -= dictionary[order]['ingredients']['coffee']
        money += dictionary[order]['cost']
        return money
    print(f"Here is your {order}. Enjoy!")

while not done:
    order = menu_prompt()
    done = check_prompt(order, user_money)
    if done == False:
        money = make_coffee(order, MENU, resources, money)