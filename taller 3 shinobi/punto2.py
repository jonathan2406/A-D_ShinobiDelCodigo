#encontrar la posicion n = 1245123 de la ecuacion particular
# 3an+1 - 4an = 0, n>= 0, a1 = 5

'''
nota: en este ejercicio lo que hacemos es plantear un algoritmo el cual da solucion a la ecuacion de primer orden que 
se le plantee dada una condicion inial a1 y que quede sin recursion para que podamos llegar facilmente a la pregunta 
de cual es la posicion que se pregunta

'''

from sympy import symbols, solve, Eq

# Definimos el símbolo 'x' para usar en nuestra ecuación
x = symbols("x")

# Definimos la ecuación de la relación de recurrencia, que es de primer orden en este caso
equation_factor = -4*x + 3

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
def solucion(n):
    return k_variable * linear_variable[0] ** n

# Imprimimos la solución general de la ecuación encontrada
print("La solución general de la ecuación es: a_n = " + str(k_variable) + " * (" + str(linear_variable[0]) + ")^n")

# Calculamos y mostramos el valor en la posición 'n = 1,245,123' de la sucesión
print(f'la posicion n = 1.245.123 es: {solucion(1245123)}')
