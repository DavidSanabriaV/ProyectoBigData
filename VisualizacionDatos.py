#2. Visualizacon de datos
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('epl_final.csv')

#Goles del equipo local
df['FullTimeHomeGoals'].dropna().plot(kind='hist', bins=15, color="salmon", edgecolor="black")
plt.title("Distribucion de Goles Local")
plt.xlabel("Goles")
plt.ylabel("Frecuencia")
plt.show()

#Goles del equipo visitante
df['FullTimeAwayGoals'].dropna().plot(kind='hist', bins=15, color="skyblue", edgecolor="black")
plt.title("Distribucion de Goles Visitante")
plt.xlabel("Goles")
plt.ylabel("Frecuencia")
plt.show()

#Tarjetas amarillas del local
df['HomeYellowCards'].dropna().plot(kind='hist', bins=10, color="gold", edgecolor="black")
plt.title("Distribucion de Tarjetas Amarillas (Local)")
plt.xlabel("Tarjetas amarillas")
plt.ylabel("Frecuencia")
plt.show()

#Tiros a puerta local, segun resultado del partido
df.boxplot(column="HomeShotsOnTarget", by="FullTimeResult", grid=False)
plt.title("Tiros a puerta (local) segun resultado del partido")
plt.suptitle("")
plt.xlabel("Resultado (H=Local, D=Empate, A=Visitante)")
plt.ylabel("Tiros a puerta")
plt.show()

#Tarjetas amarillas segun resultado del partido
df.boxplot(column="HomeYellowCards", by="FullTimeResult", grid=False)
plt.title("Tarjetas amarillas (local) segun resultado del partido")
plt.suptitle("")
plt.xlabel("Resultado")
plt.ylabel("Tarjetas amarillas")
plt.show()

#Faltas cometidas segun resultado del partido
df.boxplot(column="HomeFouls", by="FullTimeResult", grid=False)
plt.title("Faltas cometidas (local) segun resultado del partido")
plt.suptitle("")
plt.xlabel("Resultado")
plt.ylabel("Faltas")
plt.show()

#Tiros a puerta vs Goles del Local
tabla_cruzada = pd.crosstab(df['FullTimeHomeGoals'], df['HomeShotsOnTarget'])

plt.figure(figsize=(10, 6))
plt.imshow(tabla_cruzada, cmap="Blues", aspect='auto', origin='lower')
plt.colorbar(label='Cantidad de partidos')
plt.title("Relacion entre tiros a puerta y goles (local)")
plt.xlabel("Tiros a puerta")
plt.ylabel("Goles")
plt.xticks(range(len(tabla_cruzada.columns)), tabla_cruzada.columns)
plt.yticks(range(len(tabla_cruzada.index)), tabla_cruzada.index)
plt.show()

#Faltas vs Tarjetas amarillas
tabla_cruzada2 = pd.crosstab(df['HomeYellowCards'], df['HomeFouls'])

plt.figure(figsize=(12, 6))
plt.imshow(tabla_cruzada2, cmap="Oranges", aspect='auto', origin='lower')
plt.colorbar(label='Cantidad de partidos')
plt.title("Relacion entre faltas cometidas y tarjetas amarillas")
plt.xlabel("Faltas")
plt.ylabel("Tarjetas amarillas")
plt.xticks(range(len(tabla_cruzada2.columns)), tabla_cruzada2.columns)
plt.yticks(range(len(tabla_cruzada2.index)), tabla_cruzada2.index)
plt.show()
