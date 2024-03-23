from Operaciones import Operaciones
from Menu import Menu
from Pruebas import Pruebas
 

#clase envolvente que se encaarga de la comunicacion entre usuario y saber que operacion debe realizar segun el input recopilado
#el arbol de decisiones para tomar la decision de cual utilizar fue el que esta en las diapositivas en la u virtual de principios de conteo
class Wilfram:

    def main():
        Menu.intro() #O(1)
        while(True): #O(n)
            print('Bienvenido a Wilfram alpha') # O(1)
            orden, intervencion, repeticion = (Menu.orden(), Menu.intervencion(), Menu.repeticion()) #O(1)
            try:
                if orden == True: #O(1)
                    if intervencion == True: #O(1)
                        if repeticion == True: #O(1)
                            print('permutacion con repeticion detectada!!') #O(1)
                            n = Menu.valorN()
                            if n == 0:
                                print("no podes organizar 0 elementos...")
                                continue
                            repetidos = Menu.ingresarRepetidos()
                            if sum(repetidos) > n:
                                print("los valores repetidos ingresados son mayores que n asi que gravisimo")
                                continue
                            resultado = Operaciones.permutacionRepeticion(n,repetidos) #O(n)
                        else:
                            print('permutacion ordinaria detectada!!')#O(1)
                            if n == 0:
                                print("no podes organizar 0 elementos...")
                                continue
                            resultado = Operaciones.permutacionOrdinaria(Menu.valorM()) #O(n)
                    else: #O(1)
                        if repeticion == True:
                            print('variacion con repeticion detectada!!') #O(1)
                            m = Menu.valorM()
                            if m == 0:
                                print("no podes organizar 0 elementos...")
                                continue
                            n = Menu.valorN()
                            if n == 0:
                                print("no podes organizar 0 elementos de algo ...")
                                continue
                            if n>m: 
                                print("no se puede porque n es mayor que m graveeeeeeeeeeeeeee")
                                continue
                            else:
                                resultado = Operaciones.variacionRepeticion(m, n) #O(n)
                        else: #O(1)
                            print('variacion ordinaria detectada!!') #O(1)
                            m = Menu.valorM()
                            if m == 0:
                                print("no podes organizar 0 elementos...")
                                continue
                            n = Menu.valorN()
                            if n == 0:
                                print("no podes organizar 0 elementos de algo ...")
                                continue
                            if n>m: 
                                print("no se puede porque n es mayor que m graveeeeeeeeeeeeeee")
                                continue
                            else:
                                resultado = Operaciones.variacionOrdinaria(m, n) #O(n)
                else: #O(1)
                    if repeticion == True: #O(1)
                        print('combinacion con repeticion detectada!!') #O(1)
                        m = Menu.valorM()
                        if m == 0:
                            print("no podes organizar 0 elementos...")
                            continue
                        n = Menu.valorN()
                        if n == 0:
                            print("no podes organizar 0 elementos de algo ...")
                            continue
                        if n>m: 
                            print("no se puede porque n es mayor que m graveeeeeeeeeeeeeee")
                            continue
                        else:
                            resultado = Operaciones.combinacionRepeticion(m, n) #O(n)
                    else:
                        print('combinacion ordinaria detectada!!') #O(1)
                        if m == 0:
                            print("no podes organizar 0 elementos...")
                            continue
                        n = Menu.valorN()
                        if n == 0:
                            print("no podes organizar 0 elementos de algo ...")
                            continue
                        if n>m: 
                            print("no se puede porque n es mayor que m graveeeeeeeeeeeeeee")
                            continue
                        else:
                            resultado = Operaciones.combinacionOrdinaria(m, n) #O(n)
                if resultado < 0:
                    print("resultado negativo no tiene sentido.........>:(")
                    continue
                
                print(f'el resultado fue: {resultado}') #O(1)

            except:
                print("el calculo fue tan grande que el pc no agunto sjajsdjasjdjsd")
            
            if Menu.repetirmenu() == False: break #O(1)

    def ejecutarPruebas():
        Pruebas.ejecuacionPruebas() #O(1)


        
