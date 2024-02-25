''' Dado las dimensiones de una matriz cuadrada, mostrar los
    índices de la matriz en forma de zig-zag empezando por la
    posición[n][n].'''


class PrimerPunto:

    def main():
        numero = PrimerPunto.menu()
        matriz = [[i + j * numero + 1 for i in range(numero)] for j in range(numero)]
        PrimerPunto.printMatriz(matriz)
        PrimerPunto.zigZag(matriz, numero-1, numero-1)
       
    def menu():
        while(True):
            numero = input('ingrese de que tamano quiere su matriz cuadrada: ')
            if numero.isdigit() == False:
                print('eso no es un numero >:(((')
                continue
            return int(numero)

    def printMatriz(matriz):
        for row in matriz: print(row)    

    def zigZag(matriz, filaActual, columnaActual, direccion = 'down'):
        print(f'posicion: ({filaActual},{columnaActual}) contenido: {matriz[filaActual][columnaActual]}')
        if filaActual == 0 and columnaActual == 0: return
        if direccion == 'up':
            if columnaActual == len(matriz)-1 and filaActual == 0:
                PrimerPunto.zigZag(matriz,filaActual, columnaActual-1, 'down')
            elif columnaActual == len(matriz)-1:
                PrimerPunto.zigZag(matriz, filaActual-1, columnaActual, 'down')
            elif filaActual == 0:
                PrimerPunto.zigZag(matriz, filaActual, columnaActual-1, 'down')
            else:
                PrimerPunto.zigZag(matriz, filaActual-1, columnaActual+1 , 'up')
        else:
            if columnaActual == 0 and filaActual == len(matriz)-1:
                PrimerPunto.zigZag(matriz, filaActual-1, columnaActual, 'up')
            elif columnaActual == 0:
                PrimerPunto.zigZag(matriz, filaActual-1, columnaActual, 'up')
            elif filaActual == len(matriz)-1:
                PrimerPunto.zigZag(matriz, filaActual, columnaActual-1, 'up')
            else:
                PrimerPunto.zigZag(matriz, filaActual+1, columnaActual-1 , 'down')    

PrimerPunto.main()

        
        
