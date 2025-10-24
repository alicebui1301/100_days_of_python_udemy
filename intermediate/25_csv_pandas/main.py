# import csv

# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

# import pandas as pd

# data = pd.read_csv("intermediate/25_us_states_game_csv/weather_data.csv")
# data_dict = data.to_dict()

# temperature_list = data["temp"].to_list()

# print(data["temp"].max())
# print(data["temp"].mean())
# print(len(temperature_list))

# print(data["condition"])
# print(data[data.day == "Monday"])

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("intermediate/25_us_states_game_csv/new_data.csv")

import pandas as pd

data = pd.read_csv("intermediate/25_us_states_game_csv/squirrel_data.csv")

data_gray = data[data["Primary Fur Color"] == "Gray"]
data_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
data_black = data[data["Primary Fur Color"] == "Black"] 

gray_count = len(data_gray)
cinnamon_count = len(data_cinnamon)
black_count = len(data_black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("intermediate/25_us_states_game_csv/squirrel_count.csv")