import numpy as np
import pandas as pd

df = pd.read_csv('athlete_events.csv')

dfChile = df[df['Team'] == 'Chile']

#cantidad_atletas = dfChile['Year'].value_counts()
#max_cantidad_atletas = cantidad_atletas.head(1)
max_cantidad_atletas = dfChile['Year'].value_counts()[0]

maximo_anio_chilenos = dfChile['Year'].value_counts().index[0]
minimo_anio_chilenos = dfChile['Year'].value_counts(ascending = True).index[0]

winners = dfChile[dfChile['Medal'].notna()]


nombres_ganadores = winners['Name'].drop_duplicates()

medallas = dfChile[dfChile['Medal'].notna()]
medallas_por_evento = medallas.loc[:, ['Year', 'Event','Medal']].drop_duplicates()
agrupar_medallas = medallas_por_evento['Year'].value_counts().index[0]
