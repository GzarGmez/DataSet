import pandas as pd

# Carga el dataSet desde un archivo CSV
data = pd.read_csv('D:\Phyton\DataSet\Spotify_final_dataset.csv')

# Exploración inicial del dataSet
print("Número de filas y columnas:", data.shape)
print("\nPrimeras filas del dataSet:")
print(data.head())
print("\nInformación sobre el dataSet:")
print(data.info())
print("\nEstadísticas descriptivas del dataSet:")
print(data.describe())
print("\nNombres de las columnas del dataSet:")
print(data.columns)

