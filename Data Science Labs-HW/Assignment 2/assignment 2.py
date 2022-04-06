import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Question 1
x = np.random.choice(np.arange(1,51),(100,10))

#1.
print("Mean: " + str(np.mean(x)))
print("Median: " + str(np.median(x)))
print("Max: " + str(np.max(x)))
print("Standard Dev: " + str(round(np.std(x),2)))

#2.
print("Mean for each row:")
mn_row = 1
for row in x:
    print("Row " + str(mn_row) + " - "  + str(np.mean(row)))
    mn_row+=1

print("Median for each row:")
md_row = 1
for row in x:
    print("Row " +  str(md_row) +  " - " + str(np.median(row)))
    md_row+=1

print("Max for each row")
mx_row = 1
for row in x:
    print("Row " +  str(mx_row) + " - " + str(np.max(row)))
    mx_row+=1

print("Standard Dev. for each row")
std_row = 1
for row in x:
    print("Row " +  str(std_row) +  " - " + str(round(np.std(row),2)))
    std_row+=1



#Question 2
x = np.random.choice(np.arange(1,51),(1000,))

#1. 
print("First 10 numbers: " + str(x[:10]))
print("Last 10 numbers: " + str(x[-10:]))
print("Variance: " + str(round(np.var(x),2)))


#2.
diff_array = x[1:] - x[:-1]
print("Array of difference: " +str(diff_array))

#3.
print("Sum of difference array (using np.sum): " +  str(np.sum(diff_array)))
sum = 0
#use for loop
for i in diff_array:
    sum+=i
print("Sum of difference (using for loop): " +  str(sum))

#4.
sorted_x = np.sort(x)
print("Sorted original x array: " + str(sorted_x))

#5
print("First 10 numbers: " + str(sorted_x[:10]))
print("Last 10 numbers: " + str(sorted_x[-10:]))
print("Variance: " + str(round(np.var(sorted_x),2)))

#6
mean_col = np.mean(x, axis=0)
median_col = np.median(x,axis=0)
max_col = np.max(x,axis=0)
std_col = np.std(x,axis=0)

print("Mean Col: " + str(mean_col))
print("Median Col: " + str(median_col))
print("Max Col: " + str(max_col))
print("Standard Dev: " + str(round(std_col,2)))



#Question 3

#1.
data_x = np.loadtxt('US_population.txt', usecols=0, skiprows=1, delimiter = ",", dtype='str')
data_y = np.loadtxt('US_population.txt', usecols=1, skiprows=1, delimiter = ",")

#cleaning up data(years only)
cn = 0
for i in data_x:
    data_x[cn] =  i.replace("-12-31","")
    cn+=1


#2.
annual_growth_rate = (data_y[1:] - data_y[:-1]) / (data_y[:-1]) * 100
#Question 3

#1.
data_x = np.loadtxt('US_population.txt', usecols=0, skiprows=1, delimiter = ",", dtype='str')
data_y = np.loadtxt('US_population.txt', usecols=1, skiprows=1, delimiter = ",")

#cleaning up data(years only)
cn = 0
for i in data_x:
    data_x[cn] =  i.replace("-12-31","")
    cn+=1


#2.
annual_growth_rate = (data_y[1:] - data_y[:-1]) / (data_y[:-1]) * 100
#3
plt.xlabel("Year")
plt.xticks(np.arange(10, len(data_x)+1, 20))
plt.ylabel("Population")


plt.plot(data_x[:72],data_y[:72], color = "red",)
plt.plot(data_x[72:],data_y[72:], color = "red",  linestyle = "dashed")

plt.title("US Population")
plt.show()

#4.
plt.xticks(np.arange(10, len(data_x)+1, 20))
plt.ylabel("Annual % Change")
plt.xlabel("Year")
plt.plot(data_x[:72],annual_growth_rate[:72], color = "purple")
plt.plot(data_x[72:-1],annual_growth_rate[72:], color = "purple", linestyle = "dashed")

plt.title("US Population Growth Rate%")
plt.show()