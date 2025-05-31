# calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(f,s):
    return f + s

def subtract(f,s):
    return f - s

def multiply(f,s):
    return f * s

def divide(f,s):
    return f / s

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    accumulate = True

    print(logo)
    first_num = float(input("What's your first number?: "))

    while accumulate:    
        print("+\n=\n*\n/")
        oper = input("Pick an operation: ")
        second_num = float(input("What's your second number?: "))
        answer = operations[oper](first_num, second_num)
        print(f"{first_num} {oper} {second_num} = {answer}")

        choice = input(f"Type 'y' to continue calcultating with {answer}, or type 'n' to start a new calculation: ")
        if choice == 'y':
            first_num = answer
        else:
            accumulate = False
            calculator()

calculator()