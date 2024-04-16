# sucesion: 1, 1/3, 1/9, 1/27... hallar el n=100
# la relacion de recurrencia está dada por an = an-1/3 con n>=1

'''
nota1: en este ejercicio lo que hacemos es plantear un algoritmo el cual da solucion a la ecuacion de primer orden que 
se le plantee dada una condicion inial a1 y que quede sin recursion para que podamos llegar facilmente a la pregunta 
de cual es la posicion que se pregunta

nota2: para este ejercicio la formula se saco observando y analizando por tanteo la cual seria an = an-1/3 con n>=1,
como nos dan los primeros valores de la sucesion podemos decir que a1 = 1 
y ya se utiliza el codigo para darle solucion, lo explicado en la nota 1

'''

from sympy import symbols, solve, Eq

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

def solucion(n):
    return k_variable * linear_variable[0] ** n

# Imprimimos la solución general de la ecuación
print("La solución general de la ecuación es: a_n = " + str(k_variable) + " * (" + str(linear_variable[0]) + ")^n")

# Calculamos y mostramos el valor en la posición n = 100
print(f'la posicion n = 100 es: {solucion(100)}')
