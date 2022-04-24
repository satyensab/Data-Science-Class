#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#reading csv file
df_2021_22 = pd.read_csv("2021-2022 NBA Player Stats.csv", sep = ";", encoding='latin-1')
df_2020_21 = pd.read_csv("nba2021_advanced.csv")
df_2020_21.head(5)

#1. Model the data using PER and TrueShooting percentage to determine the best players in the league and the most average players in the league
# Best Players In The League 2020 - 2021
# 1.Nikola Jokić
# 2.Joel Embiid	
# 3.Giannis Antetokounmpo.

sort_PER_2021 = df_2020_21.sort_values(by=['PER','TS%','G'], ascending = [False,False,False])
print(sort_PER_2021[['Player','PER','TS%','G']].head(50))

# Most Average Players 
# 1. Theo Pinson
# 2. Quinndary Weatherspoon
# 3. Markus Howard

print(sort_PER_2021[['Player','PER','TS%','G']].tail(30))

# Best Players In The League 2021 - 2022
# 1.Nikola Jokić
# 2.Giannis Antetokounmpo
# 3.Joel Embiid
df_2021_22['TS%'] = df_2021_22['PTS']/(2*(df_2021_22['FGA'] + (0.44 * df_2021_22['FTA'])))

sort_PER_2021 = df_2021_22.sort_values(by=['TS%','G'], ascending = [False,False])
# print(sort_PER_2021[['Player','TS%','G']].head(50))

# Most Average Players 
# 1. Sharife Cooper 
# 2. Robert Woodard II
# 3. Solomon Hill
print(sort_PER_2021[['Player','TS%','G']].tail(50))

#2 What players have become much better in that year?
# Giannis Antetokounmpo did better in 2021 than in 2020

#3. What players have become much worst?
# Joel Embiid did a little worse in 2021 than in 2020

scatter_2021 = plt.scatter(df_2020_21['PER'], df_2020_21['TS%'],c='red', alpha=0.5, label = "2020-2021")
scatter_2022 = plt.scatter(df_2021_22['PTS'], df_2021_22['TS%'],c='blue', alpha=0.5, label = "2021-2022")
plt.title("NBA STATS")
plt.xlabel("PER")
plt.ylabel("TS%")
plt.legend()
plt.show()
