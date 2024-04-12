#Implementa una función no recursiva que cuente el número de dígitos en un número entero

def contar_digitos_numero_entero(numero):    #O(n)
    contador = 0 #O(0) #O(1)
    numero = abs(numero) #O(0) #O(1)


    while numero > 0:  #O(n)
        contador += 1  #O(n)
        numero //= 10  #O(n)

    return contador #O(0)

numero = 170943876  #O(0) #O(1)
print("El número de dígitos en", numero, "es:", contar_digitos_numero_entero(numero))  #O(0)

#Complejidad Temporal: O(n)
#Complejidad Espacial: O(1) 