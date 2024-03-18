#clase encargada de las operaciones matematicas para la realizacion del programa con todas sus clasificaciones

class Operaciones:

    def factorial(numero): #O(n)
        acum = 1 #O(1)
        for i in range(1, numero + 1): #O(n)
            acum = acum * i #O(1)
        return acum #O(1)
    
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