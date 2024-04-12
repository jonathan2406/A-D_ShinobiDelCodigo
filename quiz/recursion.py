# : Escribir un algoritmo que realice la multiplicación de los valores de un vector de forma recursiva

def multiplicacionRecursiva(lista, cont = 1):
    if len(lista) == 0: return cont
    cont *= lista.pop()
    return multiplicacionRecursiva(lista,cont)

print(multiplicacionRecursiva([1,5,3,6,-10,0,6555]))

