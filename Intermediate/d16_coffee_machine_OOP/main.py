from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

not_off = True

while not_off:    
    coffee_choice = input(f"What would you like? ({menu.get_items()}): ")
    if coffee_choice == "off":
        not_off = False
    elif coffee_choice == "report":
        coffee_maker.report()        
        money_machine.report()               
    elif coffee_choice in menu.get_items().split("/"):
        coffee_type = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(coffee_type):                        
            if money_machine.make_payment(coffee_type.cost):
                coffee_maker.make_coffee(coffee_type)
        