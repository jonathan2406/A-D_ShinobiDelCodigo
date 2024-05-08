import random

def caminosAll(matriz, current=(0, 0), visitados=None):
    if visitados is None:
        visitados = []

    visitados.append(current)

    if current[0] == len(matriz) - 1 and current[1] == len(matriz[0]) - 1:
        return [visitados]

    caminos = []

    if current[0] + 1 < len(matriz):
        if matriz[current[0] + 1][current[1]] != 0 and (current[0] + 1, current[1]) not in visitados:
            caminos.extend(caminosAll(matriz, (current[0] + 1, current[1]), visitados.copy()))

    if current[1] + 1 < len(matriz[0]):
        if matriz[current[0]][current[1] + 1] != 0 and (current[0], current[1] + 1) not in visitados:
            caminos.extend(caminosAll(matriz, (current[0], current[1] + 1), visitados.copy()))

    return caminos

def nxn(matriz):
    if not matriz:
        return False  
    longitud_fila = len(matriz[0])  
    for fila in matriz:
        if len(fila) != longitud_fila:
            return False  
    return True


def caminoMasCorto(matriz):
    if nxn(matriz) == False: 
        print("gravisimo")
        return
    caminos = caminosAll(matriz)
    masCorto = caminos[0]
    for iteracion in caminos:
        if len(iteracion) < len(masCorto):
            masCorto = iteracion
    print("el camino mas corto es: ")
    return masCorto

def generar_matriz(n):
    matriz = []
    for _ in range(n):
        fila = [random.randint(0, 9) for _ in range(n)] 
        matriz.append(fila)
    return matriz


print(caminoMasCorto(generar_matriz(5)))