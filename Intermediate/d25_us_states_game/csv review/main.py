import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250610.csv")
grey_squirrels = df[df["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = df[df["Primary Fur Color"] == "Cinnamon"]
black_squirrels = df[df["Primary Fur Color"] == "Black"]

df_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(grey_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
}

df_new = pd.DataFrame(df_dict)
df_new.to_csv("squirrel_count.csv")


# ------------------------------

# df = pd.read_csv("weather_data.csv")
# print(df)
# print(df["temp"])
# print(df["temp"].mean())
# print(df["temp"].max())

# ------------------------------

# import csv

# with open("weather_data.csv") as df:
#     data = csv.reader(df)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)
