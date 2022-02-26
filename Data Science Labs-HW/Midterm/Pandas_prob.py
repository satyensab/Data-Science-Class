# Pandas - Pandas Problems
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 2/25/2022, DSCI 1302

import pandas as pd

#adult.csv
#1.What is the average age of adults that make under 50K? whats the average age of adults that make over 50K
adult_stat = pd.read_csv('adult.csv')
print(adult_stat.groupby(["class"])[["age"]].mean())

print()
#2.What is the standard deviation of hours worked of adults that make under 50K? What is the standard deviation of hours worked of adults that make over 50K?
print(adult_stat.groupby(["class"])[["hours-per-week"]].std())

print()
#3. What is the correlation between of hours worked and age of adults that make under 50K? What is the correlation between of hours worked and age of adults that make over 50K?
print(adult_stat.groupby(["class"])[['age','hours-per-week']].corr())

print()

#car.csv
#4.Replace each text value for a meaningful integer equivalent for each column in  the data

car_stat = pd.read_csv('car.csv')
car_stat=car_stat.replace(to_replace="low",value=1)
car_stat=car_stat.replace(to_replace="med",value=2)
car_stat=car_stat.replace(to_replace="high",value=3)
car_stat=car_stat.replace(to_replace="vhigh",value=4)
car_stat=car_stat.replace(to_replace="small",value=1)
car_stat=car_stat.replace(to_replace="big",value=3)
car_stat=car_stat.replace(to_replace="unacc",value=1)
car_stat=car_stat.replace(to_replace="acc",value=2)
car_stat=car_stat.replace(to_replace="good",value=3)
car_stat=car_stat.replace(to_replace="vgood",value=4)
car_stat=car_stat.replace(to_replace="5more",value=5)
car_stat=car_stat.replace(to_replace="more",value=5)
print(car_stat)

#5.What’s the correlation between buying, safety, and maintence.
print(car_stat[['Buying','Safety','Maintenance']].corr())

print()
#iris.csv
#6. What is the median petal length and width for each flower type
iris_stat = pd.read_csv('iris.csv')
print(iris_stat.groupby(["Flower_class"])[['Petal_length','Petal_width']].median())

print()
#7.What is the correlation for each flower type
print(iris_stat.groupby(["Flower_class"]).corr().to_string())