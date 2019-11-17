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
    aux=0
    aux2=0
    def polinomio(x):
        for i in range(n):
            if i==0:
                aux=f(x0)
                f2=f
            else:
                aux2=derivada(f2)
                f2=aux2
                aux3=aux2(x0)
                aux= aux+(((aux3*((x-x0)**i)))/math.factorial(i))
        return aux
    return polinomio

if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    f=lambda x: math.sin(x)
    p=polinomio_taylor(f,0,4)
    x=0.30
    print(p(x))
    pass