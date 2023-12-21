# import pandas as pd

# # data = pd.read_csv("weather_data.csv", sep=",")

# # print(data[data.temp == data.temp.max()])

# # print(data[data.day == "Monday"].temp * (9 / 5) + 32)

# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# # print(data_dict)

# new = pd.DataFrame(data_dict)
# new.to_csv("new.csv")


import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count],
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel fur counts.csv")
