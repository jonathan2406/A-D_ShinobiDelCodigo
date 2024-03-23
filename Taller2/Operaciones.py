#clase encargada de las operaciones matematicas para la realizacion del programa con todas sus clasificaciones

class Operaciones:

    def factorial(n):
        if n<0:
            n = -1*n
            if n == 0:
                return 1
            else:
                return -(n * Operaciones.factorial(n - 1))
        if n == 0:
            return 1
        else:
            return (n * Operaciones.factorial(n - 1))
        
        
    
    def variacionOrdinaria(m, n): #O(1)
        return Operaciones.factorial(m)/Operaciones.factorial(m-n) #O(1)

    def variacionRepeticion(m, n): #O(n)
        return m**n #O(n)

    def permutacionRepeticion(n, listaRepetidos):
        denominador = 1 #O(1)
        for numero in listaRepetidos: #O(1)
            denominador = Operaciones.factorial(numero) * denominador #O(1)
        return Operaciones.factorial(n)/denominador #O(1)

    def permutacionOrdinaria(m): return Operaciones.factorial(m) #O(1)

    def combinacionOrdinaria(m, n): #O(1)
        return Operaciones.factorial(m)/(Operaciones.factorial(n)*Operaciones.factorial(m-n)) #O(1)

    def combinacionRepeticion(m, n): #O(1)
        return Operaciones.factorial(m+n-1)/(Operaciones.factorial(n)*Operaciones.factorial(m-1)) #O(1)    