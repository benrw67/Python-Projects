#with open("weather_data.csv") as weather_file:
#    data = weather_file.readlines()
#print(data)

#import csv
import pandas

#with open("weather_data.csv") as weather_file:
#    data = csv.reader(weather_file)
#    temperatures = []
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    for row in data:
#    print(temperatures)
#    total_temp = 0
#    count = 0
#    for i in temperatures:
#        total_temp = total_temp + i
#        count = count + 1
#    average = int(total_temp / count)
#    print(f"The average tempreture for the week was {average} degrees Celcius.")

#data = pandas.read_csv("weather_data.csv")
#temp_list = data["temp"].to_list()
#total_temp = 0
#count = 0
#for i in temperatures:
#    total_temp = total_temp + i
#    count = count + 1
#average = int(total_temp / count)
#average = data["temp"].mean()
#average = sum(temp_list) / int(len(temp_list)
#print(data["temp"].max())
#print(f"The average tempreture for the week was {average} degrees Celcius.")

#print(temp_list)
#monday = data[data.day == "Monday"]
#monday_temp = int(monday["temp"])
#monday_f = monday_temp * 9/5 +32
#print(monday_f)



data = pandas.read_csv("squirrel_data.csv")

red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]

no_red = len(red_squirrel)
no_black = len(black_squirrel)
no_gray = len(gray_squirrel)


squirrel_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [no_gray, no_red, no_black]
}

squirrel_dataf = pandas.DataFrame.from_dict(squirrel_count)
squirrel_dataf.to_csv("squirrel_count.csv")




