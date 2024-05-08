#divide y venceras

def minimo_lista(arr):
    
    def minimo_subrango(arr, inicio, fin):
        
        if inicio == fin:
            return arr[inicio]
        
        
        if inicio + 1 == fin:
            return min(arr[inicio], arr[fin])
        
        
        mitad = (inicio + fin) // 2
        min_izquierda = minimo_subrango(arr, inicio, mitad)
        min_derecha = minimo_subrango(arr, mitad + 1, fin)
        
        
        return min(min_izquierda, min_derecha)
    
    
    return minimo_subrango(arr, 0, len(arr) - 1)


lista = [5, 3, 9, 0, 7, 2]
minimo = minimo_lista(lista)
print("El mínimo de la lista es:", minimo)