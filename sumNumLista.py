def sumar_array(array):  #O(n)
    suma = 0 #O(0) #O(1)
    for elemento in array: #O(n)
        suma += elemento  #O(n)
    return suma #O(0)


array = [6, 2, 9, 4]  #O(0) #O(1)
print("La suma de los elementos del array es:", sumar_array(array)) #O(0)

#Complejidad Temporal: O(n)
#Complejidad Espacial: O(1)