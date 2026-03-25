# 1
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# 2
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# 3
import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# 4
print(data["temp"].mean())
print(data["temp"].max())

# 5 Get data in columns
print(data["condition"])
print(data.condition)

# 6 Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# 7 C to F
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# 8 Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")