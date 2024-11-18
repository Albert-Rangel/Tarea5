#Programacion numerica y no numerica-tarea 4

    #ANDERSON ESCOBAR - DCN0501IIV1
    #ALBERT RANGEL - DCN0501IIV1

import os
import matplotlib.pyplot as plt
import math
import numpy as np

def mostrar_titulo():
    banner = """
    ################################
    #                              #
    #           Tarea 4            #
    #                              #
    ################################
    """
    print(banner)

def calcular_raices_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    else:
        return None

def graficar_funcion(funcion, rango=(-10, 10)):
    x_values = np.linspace(rango[0], rango[1], 400)
    x = x_values  # Definir x en el contexto de eval
    y_values = eval(funcion)
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

def ejercicio1():
    a, b, c = -0.5, 2.5, 4.5
    funcion = f"{a}*x**2 + {b}*x + {c}"
    graficar_funcion(funcion)
    raices = calcular_raices_cuadratica(a, b, c)
    if raices:
        print("Raices reales:", raices)
    else:
        print("No hay raices reales.")
    input("Presione Enter para continuar...")
    os.system('cls')

def ejercicio2():
    funcion = "5*x**3 - 5*x**2 + 6*x - 2"
    graficar_funcion(funcion)
    raices = np.roots([5, -5, 6, -2])
    print("Raices reales:", raices)
    input("Presione Enter para continuar...")
    os.system('cls')

def ejercicio3():
    funcion = "-8*x**4 + 0.7*x**5 + 44*x**3 - 90*x**2 + 82*x - 25"
    graficar_funcion(funcion)
    raices = np.roots([0.7, -8, 44, -90, 82, -25])
    print("Raices reales:", raices)
    input("Presione Enter para continuar...")
    os.system('cls')

def menu():
    while True:
        mostrar_titulo()
        print("1: Ejercicio 1")
        print("2: Ejercicio 2")
        print("3: Ejercicio 3")
        print("4: Salir")
        opcion = input("Ingrese la opcion deseada: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida.")
        os.system('cls')

if __name__ == "__main__":
    menu()