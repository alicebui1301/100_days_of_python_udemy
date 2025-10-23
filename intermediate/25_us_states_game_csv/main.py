# import csv

# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

import pandas as pd

data = pd.read_csv("intermediate/25_us_states_game_csv/weather_data.csv")
data_dict = data.to_dict()

temperature_list = data["temp"].to_list()

print(data["temp"].max())
print(data["temp"].mean())
print(len(temperature_list))

print(data["condition"])
print(data[data.day == "Monday"])



