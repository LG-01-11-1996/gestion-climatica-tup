import os
import pandas as pd
import matplotlib.pyplot as plt

print("=== [Rol P2-Paco] Iniciando Procesamiento Climático ===")

# 1. Crear datos climáticos de Córdoba
datos_clima = {
    'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
    'Temperatura_C': [26.5, 25.2, 22.8, 18.5, 14.3, 11.2],
    'Precipitacion_mm': [120, 110, 95, 50, 20, 10]
}
df = pd.DataFrame(datos_clima)

# Asegurar que existe la carpeta para guardar los datos procesados
os.makedirs('datos', exist_ok=True)
df.to_csv('datos/registro_climatico.csv', index=False)
print("-> Archivo 'registro_climatico.csv' generado con éxito en /datos.")

# 2. Generar y guardar un gráfico de temperaturas
plt.figure(figsize=(8, 4))
plt.plot(df['Mes'], df['Temperatura_C'], marker='o', color='red', linestyle='--', label='Temp. Promedio (°C)')
plt.title('Evolución de Temperatura - Córdoba 2026')
plt.xlabel('Mes')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()

# Guardar el gráfico en la carpeta datos
plt.savefig('datos/grafico_temperaturas.png')
plt.close()
print("-> Gráfico 'grafico_temperaturas.png' guardado con éxito en /datos.")
print("=== Procesamiento Finalizado Exitosamente ===")
