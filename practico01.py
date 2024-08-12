import numpy as np
import pandas as pd

# Establecer una semilla para garantizar la consistencia en los resultados
np.random.seed(42)
# Generar 100 valores aleatorios de estatura entre 1.4 m y 2.0 m
estaturas = np.random.uniform(1.4, 2.0, 100)
# Lista para almacenar los valores de peso calculados
pesos = []

# Generar valores de peso aleatorios adecuados según la estatura
for estatura in estaturas:
    
    # Determinar el rango de peso saludable usando un IMC de 18.5 a 24.9
    peso_min = 18.5 * (estatura ** 2)  
    peso_max = 24.9 * (estatura ** 2)  

    # Seleccionar un peso aleatorio dentro del rango calculado
    peso = np.random.uniform(peso_min, peso_max)
    pesos.append(peso)  

# Crear un DataFrame con los datos de estatura y peso generados
data = pd.DataFrame({
    'Estatura': estaturas,
    'Peso': pesos
})



# Calcular la pendiente y la intersección de la línea y = mx + b
x = data['Estatura']
y = data['Peso']
m = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
b = np.mean(y) - m * np.mean(x)

# Generar valores de y usando la ecuación de la línea recta
y_line = m * x + b



# Visualización de los datos generados y la recta ajustada

import matplotlib.pyplot as plt

plt.scatter(data['Estatura'], data['Peso'], label='Datos')
plt.plot(x, y_line, color='red', label='Recta ajustada')
plt.title('Estatura vs Peso con Recta Ajustada')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()