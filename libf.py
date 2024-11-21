import numpy as np
import matplotlib.pyplot as plt

def plotf(f, xi, xf, n, xlabel='x', ylabel='f(x)', title='Gráfica de f(x)', color='blue'):
    """
    Grafica una función en un intervalo dado.

    Args:
        f: La función a graficar.
        xi: El valor inicial del eje x.
        xf: El valor final del eje x.
        n: El número de puntos a evaluar.
        xlabel: Etiqueta del eje x.
        ylabel: Etiqueta del eje y.
        title: Título de la gráfica.
        color: Color de la línea de la gráfica.
    """
    if n <= 0:
        raise ValueError("El número de puntos debe ser mayor que cero.")
    if xi >= xf:
        raise ValueError("El valor inicial debe ser menor que el valor final.")

    # Generamos los valores de x en el intervalo
    x = np.linspace(xi, xf, n)

    # Evaluamos la función en los valores de x
    y = f(x)

    # Creamos la gráfica
    plt.plot(x, y, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()