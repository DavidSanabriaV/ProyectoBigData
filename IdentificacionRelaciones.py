import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#  Carga del dataset
df = pd.read_csv('epl_final.csv')

# Variables de interes segun el documento (Seccion VI)
cols_numericas = ["FullTimeHomeGoals", "FullTimeAwayGoals",
                   "HomeShots", "AwayShots",
                   "HomeShotsOnTarget", "AwayShotsOnTarget",
                   "HomeFouls", "AwayFouls",
                   "HomeCorners", "AwayCorners",
                   "HomeYellowCards", "AwayYellowCards",
                   "HomeRedCards", "AwayRedCards"]


# Matriz de correlacion con todas las variables del documento
matriz_cor = df[cols_numericas].corr()
print("Matriz de correlacion completa:")
display(matriz_cor)

#Ejemplos de relaciones mas relevantes 

# Goles segun tiros a puerta
promedio_goles_por_tiro = df.groupby('HomeShotsOnTarget')['FullTimeHomeGoals'].mean()
plt.figure(figsize=(10, 6))
promedio_goles_por_tiro.plot(kind='line', marker='o', color="darkblue")
plt.title("Promedio de goles segun tiros a puerta (local)")
plt.xlabel("Tiros a puerta")
plt.ylabel("Promedio de goles")
plt.grid(True, alpha=0.3)
plt.show()

# Tarjetas segun faltas
promedio_tarjetas_por_falta = df.groupby('HomeFouls')['HomeYellowCards'].mean()

plt.figure(figsize=(10, 6))
promedio_tarjetas_por_falta.plot(kind='line', marker='o', color="darkorange")
plt.title("Promedio de tarjetas amarillas segun faltas cometidas")
plt.xlabel("Faltas")
plt.ylabel("Promedio de tarjetas amarillas")
plt.grid(True, alpha=0.3)
plt.show()