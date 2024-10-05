import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo: Tamaño de las casas (en pies cuadrados) y precios (en miles de dólares)
sizes = np.array([500, 1000, 1500, 2000, 2500])
prices = np.array([150, 200, 250, 300, 350])

# Función para calcular la regresión lineal
def linear_regression(x, y):
    n = len(x)  # Número de puntos de datos
    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x ** 2) - np.sum(x) ** 2)
    b = (np.sum(y) - m * np.sum(x)) / n
    return m, b

# Obtener los coeficientes de la recta de regresión
m, b = linear_regression(sizes, prices)

# Mostrar la ecuación de la línea de regresión
print(f"Ecuación de la recta: Precio = {m:.2f} * Tamaño + {b:.2f}")

# Entrada del usuario: Tamaño de la casa en pies cuadrados
size_to_predict = float(input("Introduce el tamaño de la casa (en pies cuadrados): "))

# Función para predecir el precio basado en el tamaño de la casa
def predict_price(size, m, b):
    return m * size + b

# Predicción del precio
predicted_price = predict_price(size_to_predict, m, b)
print(f"El precio estimado de una casa de {size_to_predict} pies cuadrados es: {predicted_price:.2f} mil dólares")

# Graficar los datos y la línea de regresión
plt.scatter(sizes, prices, color='blue', label='Datos reales')

# Graficar la línea de regresión
predicted_prices = m * sizes + b
plt.plot(sizes, predicted_prices, color='red', label='Línea de regresión')

# Graficar el punto predicho
plt.scatter(size_to_predict, predicted_price, color='green', label=f'Predicción: {predicted_price:.2f} mil dólares', zorder=5)

# Etiquetas y título
plt.xlabel('Tamaño de la casa (pies cuadrados)')
plt.ylabel('Precio (miles de dólares)')
plt.title('Precios de Casas en Cuidad de San Cristóbal Zona 8 Mixco')

# Mostrar leyenda y gráfico
plt.legend()
plt.grid(True)
plt.show()
