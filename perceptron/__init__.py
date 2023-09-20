# El siguiente codigo emula el comportamiento 
# de una compuerta logica OR con cuatro entradas

import numpy as np
import matplotlib.pyplot as plt

class PerceptronOR:
    def __init__(self, n):
        self.pesos = np.random.randn(n)
        self.n = n

    def propagacion(self, entradas):
        self.salida = 1 if np.dot(self.pesos, entradas) > 0 else 0
        self.entradas = entradas

    def actualizacion(self, alfa, salida_deseada):
        for i in range(self.n):
            self.pesos[i] = self.pesos[i] + alfa * (salida_deseada - self.salida) * self.entradas[i]

perceptron_or = PerceptronOR(4)

ejemplos_or = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1]
])


grad_pesos = [perceptron_or.pesos.copy()]
for epoca in range(100):
    for ejemplo in ejemplos_or:
        entradas = ejemplo[:4]  
        salida_deseada = ejemplo[4] 
        perceptron_or.propagacion(entradas)
        perceptron_or.actualizacion(0.1, salida_deseada)
        grad_pesos.append(perceptron_or.pesos.copy())

grad_pesos = np.array(grad_pesos)

plt.plot(grad_pesos[:, 0], 'k', label='Peso 0')
plt.plot(grad_pesos[:, 1], 'r', label='Peso 1')
plt.plot(grad_pesos[:, 2], 'b', label='Peso 2')
plt.plot(grad_pesos[:, 3], 'g', label='Peso 3')
plt.legend()
plt.xlabel('Iteración')
plt.ylabel('Valor de los Pesos')
plt.show()


print("Pesos finales:", perceptron_or.pesos)

# A continuación podemos ver qué de acuerdo con el funcionamiento
# de la compuerta OR siempre que haya siquiera un 1 entre las entradas la salida será 1
# y la salida sera cero solo si todas las entradas son cero

perceptron_or.propagacion([1,0,1,1])
print("Salida:", perceptron_or.salida)

perceptron_or.propagacion([0,0,0,0])
print("Salida:", perceptron_or.salida)

perceptron_or.propagacion([0,0,0,1])
print("Salida:", perceptron_or.salida)
