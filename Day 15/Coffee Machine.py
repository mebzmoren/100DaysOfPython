#Espresso - 50ml water & 18g coffee
#Latte - 200ml water, 24g coffee, & 150 ml milk
#Cappucino - 250ml water, 24g coffee, & 100ml milk
#Storage - 300ml water, 200ml milk, & 100g coffee
#Coins - penny (1), nickel (5), dime (10), & quarter (25)

#Requirements:
#1. Print storage
#2. Check if enough
#3. Process coins
#4. Check transaction successful
#5. Make coffee

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

def menu_prompt():
    order = input(f"What would you like? (espresso/latte/cappuucino): ")
    return order
    
def check_resources(order):
    machine = []
    required = []
    required.append(MENU[order]['ingredients'])

    
def check_prompt(order):
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
    
    

while not done:
    order = menu_prompt()
    done = check_prompt(order)
    check_resources(order)
