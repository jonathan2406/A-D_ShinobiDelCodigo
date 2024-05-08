#greddy

def min_operaciones_para_N(N):
    operaciones = 0
    while N > 0:
        if N % 2 == 0:
            N //= 2  
        else:
            N -= 1   
        operaciones += 1
    return operaciones


N = 8
resultado = min_operaciones_para_N(N)
print(f"El número mínimo de operaciones para llegar a {N} a partir de 0 es: {resultado}")
