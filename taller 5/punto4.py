def encontrar_pares(a, b):
    pares = []
    for num_a in a:
        for num_b in b:
            if num_a != num_b:
                pares.append((num_a, num_b))
    return pares

def calcular_suma_resta(pares):
    resultados = []
    for par in pares:
        resultado = abs(par[0] - par[1])
        resultados.append(resultado)
    return sum(resultados)

def main():
    num = int(input("Ingrese el tamaño de los arreglos: ")) 

    a = []
    b = []
    print("Ingrese los números para el arreglo A:")
    for _ in range(num):  # Utiliza range(num) para iterar num veces
        num = int(input())
        a.append(num)

    print("Ingrese los números para el arreglo B:")
    for _ in range(num):  # Utiliza range(num) para iterar num veces
        num = int(input())
        b.append(num)

    # Encontrar los pares
    pares = encontrar_pares(a, b)
    print("Pares encontrados:", pares)

    # Calcular la suma de las diferencias
    suma_diferencias = calcular_suma_resta(pares)
    print("La suma de las diferencias absolutas entre los pares es:", suma_diferencias)

if __name__ == "__main__":
    main()