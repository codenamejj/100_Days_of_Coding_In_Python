#!/usr/bin/python3

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
our_profit = 0


def sufficient_resources(existing_resources, our_ingredients):
    """checks if existing resource are enough and returns True if yes, False if not"""
    for item in our_ingredients:
        if our_ingredients[item] <= existing_resources[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False

def process_coins():
    """returns the total amount of money from coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    return total

def transaction_successful(received_payment, drink_cost):
    """returns True if payment is equal or more than drink cost"""
    if received_payment >= drink_cost:
        global our_profit
        change = round(received_payment - drink_cost, 2)
        if received_payment > drink_cost:
            print(f"Here's your ${change} change")
        our_profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(our_resources, needed_drink_resources):
    """Takes the existing resources and subtracts the needed resources for making the drink"""
    print(f"Here's your {choice}. Enjoy")
    for item in our_resources:
        our_resources[item] -= needed_drink_resources[item]
    return our_resources


running = True
while running:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        running = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${our_profit}")
    else:
        drink = MENU[choice]
        if sufficient_resources(resources, drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(resources, drink["ingredients"])
