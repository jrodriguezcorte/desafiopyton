import numpy as np
import pandas as pd

df = pd.read_csv('athlete_events.csv')

winner_gold = df[df['Medal'] == 'Gold']
winner_silver = df[df['Medal'] == 'Silver']
winner_bronze = df[df['Medal'] == 'Bronze']
no_winner = df[df['Medal'].isna()]


female_gold = np.where(winner_gold['Sex']  == 'F', 1, 0)
winner_gold["Female"] = female_gold

female_silver = np.where(winner_silver['Sex']  == 'F', 1, 0)
winner_silver["Female"] = female_silver

female_bronze = np.where(winner_bronze['Sex']  == 'F', 1, 0)
winner_bronze["Female"] = female_bronze

female_na = np.where(no_winner['Sex']  == 'F', 1, 0)
no_winner["Female"] = female_na


gteams =  winner_gold['Team'].value_counts()
gteams = gteams.head(10)

steams =  winner_silver['Team'].value_counts()
steams = steams.head(10)

bteams =  winner_bronze['Team'].value_counts()
bteams = bteams.head(10)

nateams =  no_winner['Team'].value_counts()
nateams = nateams.head(10)


gsex =  winner_gold['Sex'].value_counts()

ssex =  winner_silver['Sex'].value_counts()

bsex =  winner_bronze['Sex'].value_counts()

nasex =  no_winner['Sex'].value_counts()



#grouped = winner_gold.groupby('Female').mean()
#grouped = grouped['Medal']



def media(df,analyze,gender = 'Female'):
    grouped = df.groupby(gender).mean()
    grouped = grouped[analyze]
    return grouped


mean_g = media(winner_gold,'Height')
mean_s = media(winner_silver,'Height')
mean_b = media(winner_bronze,'Height')
mean_na = media(no_winner,'Height')

mean_gw = media(winner_gold,'Weight')
mean_sw = media(winner_silver,'Weight')
mean_bw = media(winner_bronze,'Weight')
mean_naw = media(no_winner,'Weight')
