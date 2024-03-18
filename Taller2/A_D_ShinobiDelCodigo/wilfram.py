from Operaciones import Operaciones
from Menu import Menu
 
class Wilfram:

    def main():
        Menu.intro() #O(1)
        while(True): #O(n)
            print('Bienvenido a Wilfram alpha') # O(1)
            orden, intervencion, repeticion = (Menu.orden(), Menu.intervencion(), Menu.repeticion()) #O(1)

            if orden == True: #O(1)
                if intervencion == True: #O(1)
                    if repeticion == True: #O(1)
                        print('permutacion con repeticion detectada!!') #O(1)
                        resultado = Operaciones.permutacionRepeticion(Menu.valorN(), Menu.ingresarRepetidos()) #O(n)
                    else:
                        print('permutacion ordinaria detectada!!')#O(1)
                        resultado = Operaciones.permutacionOrdinaria(Menu.valorM()) #O(n)
                else: #O(1)
                    if repeticion == True:
                        print('variacion con repeticion detectada!!') #O(1)
                        resultado = Operaciones.variacionRepeticion(Menu.valorM(), Menu.valorN()) #O(n)
                    else: #O(1)
                        print('variacion ordinaria detectada!!') #O(1)
                        resultado = Operaciones.variacionOrdinaria(Menu.valorM(), Menu.valorN()) #O(n)
            else: #O(1)
                if repeticion == True: #O(1)
                    print('combinacion con repeticion detectada!!') #O(1)
                    resultado = Operaciones.combinacionRepeticion(Menu.valorM(), Menu.valorN()) #O(n)
                else:
                    print('combinacion ordinaria detectada!!') #O(1)
                    resultado = Operaciones.combinacionOrdinaria(Menu.valorM(), Menu.valorN()) #O(n)
            
            print(f'el resultado fue: {resultado}') #O(1)
            
            if Menu.repetirmenu() == False: break #O(1)


        
