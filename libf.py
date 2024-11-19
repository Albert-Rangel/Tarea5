import numpy as np
import matplotlib.pyplot as plt

def plotf(f, xi, xf, n):
  """
  Grafica una función en un intervalo dado.

  Args:
    f: La función a graficar.
    xi: El valor inicial del eje x.
    xf: El valor final del eje x.
    n: El número de puntos a evaluar.
  """

  # Generamos los valores de x en el intervalo
  x = np.linspace(xi, xf, n)

  # Evaluamos la función en los valores de x
  y = f(x)

  # Creamos la gráfica
  plt.plot(x, y)
  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.title('Gráfica de f(x)')
  plt.grid(True)
  plt.show()
