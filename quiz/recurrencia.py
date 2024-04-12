from sympy import symbols, solve, Eq

x = symbols("x")

equation_factor = -3*x**2 - 2*x + 1

cuadratic_variables = solve(equation_factor)

# Ordenamos las soluciones de mayor a menor
cuadratic_variables = sorted(cuadratic_variables, reverse=True)

a_0 = 8
a_1 = 6

k1, k2 = symbols("k1 k2")

equation_1 = Eq(k1*(cuadratic_variables[0]**0) + k2*(cuadratic_variables[1]**0), a_0)
equation_2 = Eq(k1*(cuadratic_variables[0]**1) + k2*(cuadratic_variables[1]**1), a_1)

solve2x2 = solve((equation_1, equation_2), (k1, k2))

k_variables = list(solve2x2.values())

def solucion(n):
    return k_variables[0]*cuadratic_variables[0]**n + k_variables[1]*cuadratic_variables[1]**n



print(f"la ecuacion final quedaria: \nan = {k_variables[0]}*{cuadratic_variables[0]}**n + {k_variables[1]}*{cuadratic_variables[1]}**n")

print(f"la sucesion en el momento 1500 seria: {solucion(1500)}")


