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
    def _(x):
        global f
        for i in range(n-1):
            if i == 0: # Se evalua la funcion original 
                polinomio = f(x0)
            else: # Se evalua con las derivadas
                dxdf = derivada(f)
                f = dxdf
                polinomio += dxdf(x0)*(x-x0**i)/math.factorial(i)           
        return polinomio
    return _


if __name__ == '__main__':
    f = lambda x: math.sin(x)
    polinomio = polinomio_taylor(f,0,4)
    print  ("Valor real:", f(0.3))
    print ("Valor aproximado:", polinomio(0.3))
    