def suma_digitos(): # O(1) -Definición de la función.
    n = int(input("Ingrese un número: ")) # O(1) - Solicitar un número al usuario y convertirlo a entero.

    suma = 0 #O(1) - Inicializar la variable suma.

    while n > 0: # O(n) - Bucle while que se ejecuta mientras n sea mayor que 0.
        suma = suma + (n % 10) # O(1) - Sumar el último dígito de n a la variable suma.
        n = n // 10 # O(1) - Eliminar el último dígito de n.
    print("La suma de los dígitos es:", suma) # O(1) - Imprimir la variable suma.

suma_digitos() #0(1)

#O(1): Las líneas 1, 2, 4, 7, 8, 9 y 11 se ejecutan en un tiempo constante, es decir, 
# el tiempo que tardan en ejecutarse no depende del tamaño de la entrada (el número n).
#O(n): La línea 6 se ejecuta un número de veces proporcional al número de dígitos de n.
#Complejidad Temporal: O(n)
#Complejidad Espacial: O(1)