#!/usr/bin/env python3
"""
Proyecto Polinomio de Taylor.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


def derivada(f, h = 0.01):
    """
    Retorna la función derivada de f dado un h.

    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _


def polinomio_taylor(f, x0, n):
    """
    Implementa y retorna el Polinomio de Taylor de grado n centrado en x0.

    Parámetros:
    f: función de variable real f(x).
    x0: punto centro del polinomio.
    n: grado del polinomio.
    """

    def polinomio(x, df=f, j=0):
        """
        Funcion recursiva para sacar el polinomio que retorna la serie de un grado n en una funcion.

        Parámetros:
        x: función de variable real f(x). variable a recivir
        df: funcion o deivada de la funcion en el grado j. se inicializa con la funcion original
        j: contador de iteraciones. se inicializa en 0
        """
        if(j<n):                                                                            #Concion de salida que el grado sea igual a las iteraciones
            return (df(x0)*((x-x0)**j)/math.factorial(j))+polinomio(x,derivada(df),j+1)
        else:
            return df(x0)*((x-x0)**j)/math.factorial(j) 

    return polinomio


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.

    f = lambda x: math.sin(x)
    g = lambda x: math.e**(x**2)

    x = polinomio_taylor(f,0,4)


    print (x(0.3))
