import pandas as pd

df = pd.read_csv('athlete_events.csv')

ejercicio_1 = df.shape

ejercicio_2 = df.Games.drop_duplicates().count()

#dfseason = df.loc[:,['Name','Season']]
ejercicio_3 = df.Season.value_counts('%')

dfseason =  df.loc[:, ['City','Year','Season']]
dfseason = dfseason[dfseason['Season'] == 'Summer']
ejercicio_4 = dfseason[dfseason['Year'] == dfseason['Year'].min()]['City'].drop_duplicates()

dfseason =  df.loc[:, ['City','Year','Season']]
dfseason = dfseason[dfseason['Season'] == 'Winter']
ejercicio_5 = dfseason[dfseason['Year'] == dfseason['Year'].min()]['City'].drop_duplicates()

dfteams =  df['Team'].value_counts()
ejercicio_6 = dfteams.head(10)

medallas = df.loc[:, ['Medal']]
ejercicio_7 = medallas.dropna()
ejercicio_7 = ejercicio_7['Medal'].value_counts() / len(ejercicio_7)

dfseason =  df.loc[:, ['Team','Year','Season']]
dfseason = dfseason[dfseason['Season'] == 'Summer']
ejercicio_8 = dfseason[dfseason['Year'] == dfseason['Year'].min()]['Team']
ejercicio_8 = ejercicio_8.drop_duplicates()

#print(ejercicio_1)
#print(ejercicio_2)
#print(ejercicio_3)
#print(ejercicio_4)
#print(ejercicio_5)
#print(ejercicio_6)
#print(ejercicio_7)
#print(ejercicio_8)
