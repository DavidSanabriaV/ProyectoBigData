import pandas as pd
import matplotlib.pyplot as plt



# Carga del Dataset
# Columnas a utilizar para el resumen estadistico
cols_numericas = ["FullTimeHomeGoals", "FullTimeAwayGoals",
                   "HomeShots", "AwayShots",
                   "HomeShotsOnTarget", "AwayShotsOnTarget",
                   "HomeFouls", "AwayFouls",
                   "HomeCorners", "AwayCorners",
                   "HomeYellowCards", "AwayYellowCards",
                   "HomeRedCards", "AwayRedCards"]

df = pd.read_csv('epl_final.csv')


# Identifcacion y limpieza de Valores Atipicos


Q1 = df[cols_numericas].quantile(0.25)
Q3 = df[cols_numericas].quantile(0.75)
IQR = Q3 - Q1

df_cleaned = df[~((df[cols_numericas] < (Q1 - 1.5 * IQR)) |
                   (df[cols_numericas] > (Q3 + 1.5 * IQR))).any(axis=1)]

print(f"Filas originales: {len(df)} - Filas sin outliers: {len(df_cleaned)}")

# Boxplot para visualizar los atipicos antes de limpiar
df.boxplot(column=cols_numericas)
plt.title("Deteccion de valores atipicos (antes de limpiar)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

