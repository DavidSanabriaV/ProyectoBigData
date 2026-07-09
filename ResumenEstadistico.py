import pandas as pd
from IPython.display import display

#  Carga del dataset
df = pd.read_csv('epl_final.csv')

# Muestra del dataset
print("DataFrame original:")
display(df.head())
print(df.info())

# Columnas a utilizar para el resumen estadistico
cols_numericas = ["FullTimeHomeGoals", "FullTimeAwayGoals",
                   "HomeShots", "AwayShots",
                   "HomeShotsOnTarget", "AwayShotsOnTarget",
                   "HomeFouls", "AwayFouls",
                   "HomeCorners", "AwayCorners",
                   "HomeYellowCards", "AwayYellowCards",
                   "HomeRedCards", "AwayRedCards"]

# Resumen estadistico general 
print("Resumen estadistico general:")
display(df[cols_numericas].describe())

# Distribucion de los resultados finales 
print("Distribucion de resultados (FullTimeResult):")
display(df['FullTimeResult'].value_counts())

#Distribucion de los resultados finales en porcentaje
print("Porcentaje de partidos por resultado:")
display(df['FullTimeResult'].value_counts(normalize=True) * 100)

# Promedio de goles local visitante 
promedio_local = df["FullTimeHomeGoals"].mean()
promedio_visitante = df["FullTimeAwayGoals"].mean()
print(f"Promedio goles local: {promedio_local:.2f}")
print(f"Promedio goles visitante: {promedio_visitante:.2f}")