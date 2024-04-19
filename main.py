import pandas as pd
import time


# Carga el dataSet desde un archivo CSV
data = pd.read_csv('D:\Phyton\DataSet\Spotify_final_dataset.csv')

# Define las estrategias y el número de núcleos a utilizar
estrategias = ['estrategia_1', 'estrategia_2']
nucleos = [2, 4, 6]

# Definir las operaciones a realizar
def calcular_estadisticas():
    return data.describe()

def limpiar_datos():
    return data.drop_duplicates().dropna()

# Bucle para iterar sobre las estrategias y el número de núcleos
for estrategia in estrategias:
    for n in nucleos:
        start_time = time.time()  # Tiempo inicial
        # Aquí realizamos las operaciones con la estrategia y número de núcleos actuales
        # Por ejemplo, calculamos estadísticas descriptivas
        if estrategia == 'estrategia_1':
            resultado = calcular_estadisticas()
        elif estrategia == 'estrategia_2':
            resultado = limpiar_datos()
        # Calcula el tiempo de ejecución
        elapsed_time = time.time() - start_time
        # Imprime los resultados y el tiempo de ejecución
        print(f"\nEstrategia: {estrategia}, Núcleos: {n}")
        print("Resultado de la operación:")
        print(resultado)
        print(f"Tiempo de ejecución: {elapsed_time} segundos")


# Calcula la media de la columna 'Peak Streams'
media_peak_streams = data['Peak Streams'].mean()

# Imprime la media de 'Peak Streams'
print(f"Media de 'Peak Streams': {media_peak_streams}")
