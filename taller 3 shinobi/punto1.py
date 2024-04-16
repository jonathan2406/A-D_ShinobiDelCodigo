print('solucion punto 1------------------------------------------')
# sucesion: 1, 1/3, 1/9, 1/27... hallar el n=100
# la relacion de recurrencia está dada por an = an-1/3 con n>=1

'''
nota1: en este ejercicio lo que hacemos es plantear un algoritmo el cual da solucion a la ecuacion de primer orden que 
se le plantee dada una condicion inial a1 y que quede sin recursion para que podamos llegar facilmente a la pregunta 
de cual es la posicion que se pregunta

nota2: para este ejercicio la formula se saco observando y analizando por tanteo la cual seria an = an-1/3 con n>=1,
como nos dan los primeros valores de la sucesion podemos decir que a1 = 1 
y ya se utiliza el codigo para darle solucion, lo explicado en la nota 1

nota3: al final se pone el codigo que resuelve el ejercicio pero de manera recursiva y a demas se cuenta cuanto se demoro
cada uno para comparar tiempos

'''

from sympy import symbols, solve, Eq
import time



x = symbols("x")

# Ahora la ecuación es de primer orden
equation_factor = -x + 1/3

# Solución de la ecuación lineal
linear_variable = solve(equation_factor)

k1 = symbols("k1")

# Definimos el valor inicial de la secuencia
a_1 = 1

# Ya que es de primer orden, solo necesitamos una ecuación
equation_1 = Eq(k1*(linear_variable[0]**1), a_1) # Usamos a_1 en lugar de a_n

# Resolvemos para k1
solve1x1 = solve(equation_1, k1)

# Obtenemos el valor de k
k_variable = solve1x1[0] # Accedemos al resultado como una lista

def modoNoRecursivo(n):
    return k_variable * linear_variable[0] ** n

# Imprimimos la solución general de la ecuación
print("La solución general de la ecuación es: a_n = " + str(k_variable) + " * (" + str(linear_variable[0]) + ")^n")

#declaramos una variable que tome el tiempo antes de ejecutar el algoritmo que no es de manera recursiva a ver cuanto se demora:
inicioSinRecursion = time.perf_counter()

# Calculamos y mostramos el valor en la posición n = 100
print(f'la posicion n = 100 con el algoritmo sin recursion es: \n{modoNoRecursivo(100)}')

# declaramos una variable que tome el tiempo actual y le reste el tiempo de la variable de inicio para que arroje cuanto se demoro el codigo sin recursion ejecutando
finSinRecursion = time.perf_counter()
resultadoSinRecursion = finSinRecursion - inicioSinRecursion
print(f'el codigo sin recursion se demoro: {resultadoSinRecursion} segundos')


#ahora recursivavemente seria asi
def modoRecursivo(n, a0):
    if n == 1:
        return a0
    else:
        return modoRecursivo(n-1, a0) / 3

    
#declaramos una variable que tome el tiempo antes de ejecutar el algoritmo que es de manera recursiva a ver cuanto se demora:
inicioRecursion = time.perf_counter()

# Calculamos y mostramos el valor en la posición n = 100
print(f'la posicion n = 100 con el algoritmo recursivo es: \n{modoRecursivo(100, 1)}')

# declaramos una variable que tome el tiempo actual y le reste el tiempo de la variable de inicio para que arroje cuanto se demoro el codigo conrecursion ejecutando
finRecursion = time.perf_counter()
resultadoRecursivo = finRecursion - inicioRecursion
print(f'el codigo con recursion se demoro: {resultadoRecursivo} segundos')

if resultadoSinRecursion > resultadoRecursivo:
    print('la manera recursiva es mas rapida que la no recursiva')
else:
    print('la manera no recursiva es mas rapida que la no recursiva')

    


    


