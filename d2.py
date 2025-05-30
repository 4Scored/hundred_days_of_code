# tip calculator

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
p_count = int(input("How many people to split the bill? "))
split = (total + percent / 100 * total) / p_count
print(f"Each person should pay: ${round(split, 2):.2f}")