#importing necessary libraries
import pandas as pd

#reading in file
df = pd.read_csv("cinemaTicket_Ref.csv")
df.shape
df.head()

#1. Determine common factors in poor-performing ticket sales?
#Early showtimes tend to have worse ticket sales. Comparing the capacity of theatres with high ticket sales and low tickets sales, higer capacity tends to lead to more tickets sold while low capacity theatres dont sell as much.
sort_rev_ticket_sal = df.sort_values(by=['tickets_sold'], ascending = True)
print(sort_rev_ticket_sal.head(15))
print(sort_rev_ticket_sal.tail(15))

#2 Is there a connection between ticket sales and price?
#There is no significant connection between tickets sales and price. The correlation is 0.1 between tickets sales and price and that is to little correlation to make any assumptions
print(df[['tickets_sold','ticket_price']].corr())

#3. Is there a connection between ticket sales and time of day?
#Yes the highter the ticket sales it tends to be  later  in the day. We know this because the correlation between tickets sold and show time is 0.5 which means that they are moderately correlated with one another and a assumption can be made.
print(df[['tickets_sold','show_time']].corr())

#4.Is there a connection between ticket sales and the time of year?
#There is no significant correlation between tickets sales and time of year. Though the correlation is -0.1 we cant make any assumptions because how it is.
print(df[['tickets_sold','month']].corr())

#5.Can you tell off of this Data set if certain theaters are under performing? 
#You can see that cinema codes 470 and 534 has a track record of low total sales because their are amongst the lowest total sales but still it is very hard to tell based on this data if a specific theatres is under performing each time or if that was just a one time case. There has to be other certain parameters on the cinema codes that may identify the location,etc. which could indicate certain types of theatres under performing. 
sort_rev_sal = df.sort_values(by=['total_sales'], ascending = True)
sort_rev_sal[['cinema_code','total_sales']].head(20) #time of day analysis
