print('solucion punto 2------------------------------------------')

#encontrar la posicion n = 1245123 de la ecuacion particular
# 3an+1 - 4an = 0, n>= 0, a1 = 5

'''
nota: en este ejercicio lo que hacemos es plantear un algoritmo el cual da solucion a la ecuacion de primer orden que 
se le plantee dada una condicion inial a1 y que quede sin recursion para que podamos llegar facilmente a la pregunta 
de cual es la posicion que se pregunta

nota2: al final se pone el codigo que resuelve el ejercicio pero de manera recursiva y a demas se cuenta cuanto se demoro
cada uno para comparar tiempos

nota3 y la mas importante: el algoritmo de manera recursiva no aguanta ese numero de recursiones tan grande que pide 
el ejercicio, ni con librerias para calculo numerico, tambien se intento hacer con lenguajes de calculo rapido como
c++, lisa, rust, c, fortran, cython y no fue posible el calculo pero de la manera no recursiva si se podia,
asi que lo deje hasta un maximo de 2000 para que hiciera la comparacion de esa manera

'''

from sympy import symbols, solve, Eq
import time
import sys

# Definimos el símbolo 'x' para usar en nuestra ecuación
x = symbols("x")

# Definimos la ecuación de la relación de recurrencia, que es de primer orden en este caso
equation_factor = 3*x - 4

# Resolvemos la ecuación para encontrar 'x', que es nuestro factor lineal
linear_variable = solve(equation_factor)

# Creamos un símbolo 'k1' para representar nuestra constante en la solución general
k1 = symbols("k1")

# Definimos el primer término de la secuencia 'a_1' con el valor inicial
a_1 = 5.0

# Escribimos la ecuación de la forma general de la sucesión utilizando 'a_1'
equation_1 = Eq(k1*(linear_variable[0]**1), a_1) 

# Resolvemos la ecuación para encontrar el valor de 'k_variable', que representa nuestra constante en la solución general
solve1x1 = solve(equation_1, k1)

# Obtenemos el valor de 'k_variable'
k_variable = solve1x1[0] 

# Definimos una función 'solucion(n)' que nos da el término 'n' de la sucesión
def modoNoRecursivo(n):
    return k_variable * linear_variable[0] ** n

# Imprimimos la solución general de la ecuación encontrada
print("La solución general de la ecuación es: a_n = " + str(k_variable) + " * (" + str(linear_variable[0]) + ")^n")

#declaramos una variable que tome el tiempo antes de ejecutar el algoritmo que no es de manera recursiva a ver cuanto se demora:
inicioSinRecursion = time.perf_counter()

# Calculamos y mostramos el valor en la posición n = 100
print(f'la posicion n = 2000 con el algoritmo sin recursion es: \n{modoNoRecursivo(2000)}')

# declaramos una variable que tome el tiempo actual y le reste el tiempo de la variable de inicio para que arroje cuanto se demoro el codigo sin recursion ejecutando
finSinRecursion = time.perf_counter()
resultadoSinRecursion = finSinRecursion - inicioSinRecursion
print(f'el codigo sin recursion se demoro: {resultadoSinRecursion} segundos')

#ahora recursivavemente seria asi
def modoRecursivo(n, a=5):
    # Caso base
    if n == 1:
        return a
    else:
        # Fórmula recursiva
        return (4/3) * modoRecursivo(n-1, a)

#declaramos una variable que tome el tiempo antes de ejecutar el algoritmo que es de manera recursiva a ver cuanto se demora:
inicioRecursion = time.perf_counter()

# Calculamos y mostramos el valor en la posición n = 100
sys.setrecursionlimit(10000)
print(f'la posicion n = 2000 con el algoritmo recursivo es: \n{modoRecursivo(2000)}')

# declaramos una variable que tome el tiempo actual y le reste el tiempo de la variable de inicio para que arroje cuanto se demoro el codigo conrecursion ejecutando
finRecursion = time.perf_counter()
resultadoRecursivo = finRecursion - inicioRecursion
print(f'el codigo con recursion se demoro: {resultadoRecursivo} segundos')

if resultadoSinRecursion > resultadoRecursivo:
    print('la manera recursiva es mas rapida que la no recursiva')
else:
    print('la manera no recursiva es mas rapida que la no recursiva')


    


