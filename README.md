# Proyecto Polinomio de Taylor.

### Cada participante debe completar su módulo y luego solicitar el Pull-Request (PR).

A cada participante se le presenta un módulo en lenguaje *Python* con la siguiente estructura:

```python
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
    
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su polinomio de Taylor.
    pass
```
## Requerimientos.

1. El participante deberá completar en su módulo la función `polinomio_taylor(f, x0, n)`, utilizando la función `derivada(f, h = 0.01)`.
2. La función `polinomio_taylor(f, x0, n)` **deberá retornar una función**, el *Polinomio de Taylor* centrado en `x0`, de grado `n`, de la función `f` pasada por parámetro.
3. El participante deberá probar su función `polinomio_taylor(f, x0, n)` en la sección `main` del código, pudiendo implementar funciones adicionales para las pruebas. Las **funciones lambda** pueden ser de utilidad.

## Notas.

**NOTA 1**: Cualquier duda o pregunta sobre este proyecto, por favor abra un [**issue**](https://github.com/ejdecena/proyecto_polinomio_taylor/issues).

**NOTA 2**: Solo se recibirá UNA y solo una petición de PR por participante.

**NOTA 3**: Marque con **Watch** este repositorio para que reciba todas las notificaciones.

**NOTA 4**: Recuerde que hay un [**Tutorial Git**](https://github.com/ejdecena/tutorial_git) y un [**Tutorial Python**](https://github.com/ejdecena/tutorial_python) que pueden ser útiles en caso de cualquier duda.

**NOTA 5**: Se recibirán solicitudes de PR hasta el día **domingo 17 de noviembre de 2019, 11:59 pm**, SIN PRÓRROGA.