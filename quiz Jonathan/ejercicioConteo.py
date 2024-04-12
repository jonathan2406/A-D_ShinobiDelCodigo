"Examen realizado por Jonathan Mauricio Garcia Alvarez"

"""Se ordenan en una fila de 5 bolas negras, 2 bolas blancas y 3 bolas verdes. Si las bolas de
   igual color no se distinguen entre sí, ¿de cuantas formas posibles pueden ordenarse?"""

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

    def permutacionRepeticion(n, listaRepetidos):
            denominador = 1 
            for numero in listaRepetidos: 
                denominador = Operaciones.factorial(numero) * denominador 
            return Operaciones.factorial(n)/denominador 
    

print("decidi que era una permutacion con repeticion ya que si importa el orden, si entran todos los elementos y tambien hay elementos repetidos \nn seria 10 osea la suma de todos los elementos involucrados y ya los de repeticion son los que se nombran en el enunciado")
print(f"la solucion seria esta: {Operaciones.permutacionRepeticion(10,[5,3,2])}")