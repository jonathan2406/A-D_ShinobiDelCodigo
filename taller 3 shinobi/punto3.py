print('punto 3-----------------------------------------------------')
# resolver la ecuacion: an + 2an-1 + 2an-2 = 0, n>=2, a0=1, a1=3
'''
nota1: en este punto lo que hacemos es realizar un algoritmo que dada la ecuacion de segundo orden con las condiciones
iniciales este nos de la solucion de la ecuacion sin recursion para que simplemente tengamos que darle el termino n 

nota2: los valores de la solucion de le ecuacion cuadratica dan imaginarios  pero igualmente se trato de llegar
a la solucion de este :)

nota3: al final se pone el codigo que resuelve el ejercicio pero de manera recursiva y a demas se cuenta cuanto se demoro
cada uno para comparar tiempos

nota4 y la mas importante: el algoritmo de manera recursiva no aguanta ese numero de recursiones tan grande que pide 
el ejercicio, ni con librerias para calculo numerico, tambien se intento hacer con lenguajes de calculo rapido como
c++, lisa, rust, c, fortran, cython y no fue posible el calculo pero de la manera no recursiva si se podia,
asi que lo deje hasta un maximo de 2000 para que hiciera la comparacion de esa manera

'''

from sympy import symbols, solve, Eq
import time
import sys

# Definimos el símbolo 'x' para usar en nuestra ecuación
x = symbols("x")

# Definimos la ecuación cuadrática
equation_factor = x**2 + 2*x + 2

# Resolvemos la ecuación cuadrática para encontrar las raíces
cuadratic_variables = solve(equation_factor)

# Ordenamos las soluciones de mayor a menor en base a su magnitud
cuadratic_variables = sorted(cuadratic_variables, key=abs, reverse=True)

# Definimos los valores iniciales de la secuencia
a_0 = 1
a_1 = 3

# Creamos los símbolos 'k1' y 'k2' para representar las constantes en la solución general
k1, k2 = symbols("k1 k2")

# Escribimos las ecuaciones para resolver 'k1' y 'k2'
equation_1 = Eq(k1*(cuadratic_variables[0]**0) + k2*(cuadratic_variables[1]**0), a_0)
equation_2 = Eq(k1*(cuadratic_variables[0]**1) + k2*(cuadratic_variables[1]**1), a_1)

# Resolvemos el sistema de ecuaciones para encontrar 'k1' y 'k2'
solve2x2 = solve((equation_1, equation_2), (k1, k2))

# Obtenemos los valores de 'k1' y 'k2' como una lista
k_variables = list(solve2x2.values())

# Definimos una función 'solucion(n)' que nos da el término 'n' de la sucesión
def modoNoRecursivo(n):
    # Calculamos el término n de la sucesión usando 'k1' y 'k2' y las raíces cuadráticas
    result = k_variables[0]*cuadratic_variables[0]**n + k_variables[1]*cuadratic_variables[1]**n
    # Convertimos el resultado a un número complejo de Python
    result = complex(result.evalf())
    # Si la parte imaginaria es muy pequeña, redondeamos a un número real
    if abs(result.imag) < 1e-10:
        result = result.real
    return result

# Imprimimos la ecuación final de la sucesión
print(f"la ecuacion final quedaria: \nzn = {k_variables[0]}*{cuadratic_variables[0]}**n + {k_variables[1]}*{cuadratic_variables[1]}**n")

#declaramos una variable que tome el tiempo antes de ejecutar el algoritmo que no es de manera recursiva a ver cuanto se demora:
inicioSinRecursion = time.perf_counter()

# Calculamos y mostramos el valor en la posición n = 100
print(f'la posicion n = 2000 con el algoritmo sin recursion es: \n{modoNoRecursivo(100)}')

# declaramos una variable que tome el tiempo actual y le reste el tiempo de la variable de inicio para que arroje cuanto se demoro el codigo sin recursion ejecutando
finSinRecursion = time.perf_counter()
resultadoSinRecursion = finSinRecursion - inicioSinRecursion
print(f'el codigo sin recursion se demoro: {resultadoSinRecursion} segundos')

#ahora recursivavemente seria asi
def modoRecursivo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    else:
        return -2 * modoRecursivo(n-1) - 2 * modoRecursivo(n-2)

#declaramos una variable que tome el tiempo antes de ejecutar el algoritmo que es de manera recursiva a ver cuanto se demora:
inicioRecursion = time.perf_counter()

# Calculamos y mostramos el valor en la posición n = 100
sys.setrecursionlimit(10000)
print(f'la posicion n = 2000 con el algoritmo recursivo es: \n{modoRecursivo(100)}')

# declaramos una variable que tome el tiempo actual y le reste el tiempo de la variable de inicio para que arroje cuanto se demoro el codigo conrecursion ejecutando
finRecursion = time.perf_counter()
resultadoRecursivo = finRecursion - inicioRecursion
print(f'el codigo con recursion se demoro: {resultadoRecursivo} segundos')

if resultadoSinRecursion > resultadoRecursivo:
    print('la manera recursiva es mas rapida que la no recursiva')
else:
    print('la manera no recursiva es mas rapida que la no recursiva')
    

    



