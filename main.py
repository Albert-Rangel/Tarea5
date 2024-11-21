#Programacion numerica y no numerica-tarea 5 

    #ANDERSON ESCOBAR - DCN0501IIV1
    #ALBERT RANGEL - DCN0501IIV1

import numpy as np
import matplotlib.pyplot as plt
import os

def f(x):
    """Calcula el valor de la función f(x) = x + log(x)."""
    return x + np.log(x)

def obtener_datos_usuario():
    """Obtiene los datos necesarios del usuario para graficar la función.

    Returns:
        tuple: Una tupla con los valores de xi, xf y n.
    """

    while True:
        try:
            xi = float(input("Ingrese el valor inicial de x: "))
            xf = float(input("Ingrese el valor final de x: "))
            n = int(input("Ingrese el número de puntos: "))
            if n <= 0:
                print("El número de puntos debe ser mayor que cero.")
            else:
                return xi, xf, n
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números.")

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Función principal del programa."""

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            limpiar_pantalla()
            xi, xf, n = obtener_datos_usuario()
            x = np.linspace(xi, xf, n)
            y = f(x)
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Gráfica de f(x) = x + log(x)')
            plt.grid(True)
            plt.show()
        elif opcion == "2":
            limpiar_pantalla()
            print("Saliendo del programa...")
            break
        else:
            limpiar_pantalla()
            print("Opción no válida.")

def mostrar_menu():
    limpiar_pantalla()
    print("Calculadora de Funciones")
    print("------------------------")
    print("1: Graficar f(x) = x + log(x)")
    print("2: Salir")

if __name__ == "__main__":
    main()