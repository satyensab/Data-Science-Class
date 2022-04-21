#imports neccessary libraries
import pandas as pd
import zipfile
import numpy as np

#reads in a big csv file 
zf = zipfile.ZipFile(r'C:\Users\Satyen\Desktop\Data Science Projects\Homework 3\Airline\dataverse_files.zip')
years = ['1987','1988','2000','2005','2008'] #cannot read the whole data set so we choose a subset of the data
dtypes={'Year':np.int64, 'Month':np.int16, 'DayofMonth':np.int16, 'DayOfWeek':np.int16, 'DepTime':np.float64,
        'CRSDepTime':np.float64, 'ArrTime':np.float64, 'CRSArrTime':np.float64, 'UniqueCarrier':str,
        'FlightNum':str, 'TailNum':str, 'ActualElapsedTime':np.float64, 'CRSElapsedTime':np.float64,
        'AirTime':np.float64, 'ArrDelay':np.float64, 'DepDelay':np.float64, 'Origin':str, 'Dest':str,
        'Distance':np.float64, 'TaxiIn':np.float64, 'TaxiOut':np.float64, 'Cancelled':bool,
        'CancellationCode':str, 'Diverted':bool, 'CarrierDelay':np.float64, 'WeatherDelay':np.float64,
        'NASDelay':np.float64, 'SecurityDelay':np.float64, 'LateAircraftDelay':np.float64}


files = [file for file in zipfile.ZipFile.namelist(zf) if str(file)[-12:-8] in years]
df = pd.concat([pd.read_csv(zf.open(file),compression='bz2',encoding_errors='replace',dtype=dtypes) for file in files],ignore_index=True)
print('DataFrame Shape: ',df.shape)
df.head()

#data cleaning - droping null 
df.dropna(subset=['DepTime'], inplace=True)
df.dropna(subset=['ArrTime'], inplace=True)
df.dropna(subset=['TailNum'], inplace=True)

#looking if the arrival delays and the departure delays are correlated
print(df[['ArrDelay','DepDelay']].corr())

#sorts departure delay in an ascending order and descending. We dont also use arrival delay because delay depature and arrival depature have a strong correlation so it is fine to sort only by delay depature
sorted_delay_df = df.sort_values(by=['DepDelay'], ascending = True)
sorted_delay_rev_df = df.sort_values(by=['DepDelay'], ascending = False)

#1. When is the best time of day/day of week/time of year to fly to minimize delays?
#Time of day: Early morning flights
#Day of the week: 3 - Wednesday (Around midweek Tuesday/Wednesday was my average)
#Time of Year: 12 - December (around the end of the year)

print(sorted_delay_df[['DepTime','ArrDelay','DepDelay']].head(50)) #time of day analysis
print(sorted_delay_df[['DayOfWeek','ArrDelay','DepDelay']].head(40)) #time of the day of the week analysis
print(sorted_delay_df[['Month','ArrDelay','DepDelay']].head(40)) #time of year analysis


#2. Do older planes suffer more delays?
#The plans with the highest delays tend to be more older planes so, Yes the older plans suffer more delays. I found this out by looking at the age of the tail numbers of the top 10 highest delayed planes
print(sorted_delay_rev_df[['TailNum','DepDelay']].head(10)) #highest delays and their tail number. 


#3.How does the number of people flying between different locations change over time?
#In 1987 the number of people flying was low and that number increased until 2007. In 2008 there was a massive decrease in people flying over plane probably due to the recession that happened
sorted_by_year = df.sort_values(by=['Year'], ascending = False)
print(sorted_by_year['Year'].value_counts(ascending=True).sort_index(ascending=True))


#4. How well does weather predict plane delays?
#The weather and plane depature delays have weak positive correlation which means that weather does an alright job of predicting whether the plane will be delayed
print(sorted_delay_df[['WeatherDelay','DepDelay']].corr())

#5.Can you detect cascading failures as delays in one airport create delays in others? Are there critical links in the system?
#From the data I analyzed if there is a delay of departing an airplane then that same plane most of the times arrives late, and then another plane from that same airplane tends  to also depart late. There are defenetitally critical links in that if some major airlports are delayed that delays other airports
sorted_by_day = df.sort_values(by=['Year','Month','DayofMonth'], ascending = True)
print(sorted_by_day[['Year','Month','DayofMonth','Origin','Dest','DepDelay','ArrDelay']].tail(80))

#6.Rank the Airlines by delay 
#1.Southwest Airlines Co
#2.United Air Lines Inc.
#3.American Airlines Inc.
#4.Delta Air Lines Inc.
#5.US Airways Inc.
print(sorted_delay_rev_df.groupby(['UniqueCarrier'])[['DepDelay']].sum().sort_values(by=['DepDelay'],ascending = False).head(10))

#7.Rank Airports by delay
#1.Chicago O'Hare International Airport 
#2.Hartsfield-Jackson Atlanta International Airport
#3.Dallas/Fort Worth International Airport
#4.Los Angeles International Airport
#5.Phoenix Sky Harbor International Airport

print(sorted_delay_rev_df.groupby(['Origin'])[['DepDelay']].sum().sort_values(by=['DepDelay'],ascending = False).head(10))


#8.Analyze the Data to provide suggestions for airlines to improve the cancelation rates and delays
#Earlier the time of day normally means less delay. Airports have to take this into account that flights are most delayed around midday and adjust the amount of flights that should be booked then.
df.plot(kind = 'scatter', x = 'DepTime', y = 'DepDelay')