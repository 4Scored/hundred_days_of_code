# coffee machine

from coffee_info import MENU

change = {
    "quarter": 25,
    "dime": 10,
    "nickle": 5, 
    "penny": 1 
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(ord_ingredients):   
    for ingredient in ord_ingredients:
        if ord_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    total = 0
    print("Please insert coins.")
    q = float(input("How many quarters?: "))
    d = float(input("How many dimes?: "))
    n = float(input("How many nickles?: "))
    p = float(input("How many pennies?: "))
    total += q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    return total

def process_transaction(money_recieved, cost):    
    if money_recieved >= cost:
        change = money_recieved - cost
        print(f"Here is ${round(change,2)} in change.\nHere is your coffee ~ Enjoy!")
        resources["money"] += cost
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False # else

not_off = True

while not_off:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif coffee_choice == 'off':
        not_off = False    
    elif coffee_choice in MENU:
        coffee_type = MENU[coffee_choice]        
        res_check = check_resources(coffee_type["ingredients"])
        if res_check:
            total = process_coins()
            process_transaction(total, coffee_type["cost"])
        





