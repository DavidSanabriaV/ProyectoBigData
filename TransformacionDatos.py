from sklearn.preprocessing import StandardScaler, LabelEncoder
from IPython.display import display
# En TransformacionDatos.py
from IdentificacionyLimpieza import df_cleaned


# Columnas a utilizar para el resumen estadistico
cols_numericas = ["FullTimeHomeGoals", "FullTimeAwayGoals",
                   "HomeShots", "AwayShots",
                   "HomeShotsOnTarget", "AwayShotsOnTarget",
                   "HomeFouls", "AwayFouls",
                   "HomeCorners", "AwayCorners",
                   "HomeYellowCards", "AwayYellowCards",
                   "HomeRedCards", "AwayRedCards"]

# Transformacion de datos



#Gestion de variables categoricas 
df_transformado = df_cleaned.copy()
for col in df_transformado.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_transformado[col] = le.fit_transform(df_transformado[col].astype(str))
print("DataFrame con variables categoricas codificadas:")
display(df_transformado.head())

#Centralizacion de los datos 
df_centrado = df_cleaned.copy()
df_centrado[cols_numericas] = df_cleaned[cols_numericas] - df_cleaned[cols_numericas].mean()
print("DataFrame centrado:")
display(df_centrado[cols_numericas].head())

# Estandarizar los datos 
scaler = StandardScaler()
df_estandarizado = df_cleaned.copy()
df_estandarizado[cols_numericas] = scaler.fit_transform(df_cleaned[cols_numericas])
print("DataFrame estandarizado:")
display(df_estandarizado[cols_numericas].head())