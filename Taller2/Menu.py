import inquirer

class Menu: #O(n)

    def orden(): #O(1)
        question = [
            inquirer.List('respuesta',
                        message="¿Importa el orden?",
                        choices=['Sí', 'No'],
                    ),
        ]  # O(1)

        answer = inquirer.prompt(question) # O(1)

        print("Respuesta:", answer['respuesta']) # O(1)


        if answer['respuesta'] == 'Sí':  # O(1)
            return True  # O(1)
        else:
            return False  # O(1)
        
        
    def intervencion(): #O(1)
        question = [
            inquirer.List('respuesta',
                        message="¿Intervienen todos los elementos?",
                        choices=['Sí', 'No'],
                    ),
        ] # O(1)

        answer = inquirer.prompt(question)  # O(1)

        print("Respuesta:", answer['respuesta']) # O(1)


        if answer['respuesta'] == 'Sí':  # O(1)
            return True  # O(1)
        else:
            return False  # O(1)

    def repeticion(): #O(1)
        question = [
            inquirer.List('respuesta',
                        message="¿se repiten elementos?",
                        choices=['Sí', 'No'],
                    ),
        ]  # O(1)

        answer = inquirer.prompt(question) # O(1)

        print("Respuesta:", answer['respuesta']) # O(1)


        if answer['respuesta'] == 'Sí': # O(1)
            return True # O(1)
        else:
            return False # O(1)
    
    def repetirmenu(): #O(1)
        question = [
            inquirer.List('respuesta',
                        message="¿desea hacer otra operacion?",
                        choices=['Sí', 'No'],
                    ),
        ] # O(1)

        answer = inquirer.prompt(question) # O(1)

        print("Respuesta:", answer['respuesta']) # O(1)


        if answer['respuesta'] == 'Sí': # O(1)
            return True # O(1)
        else:
            return False # O(1)
        
    def valorM(): #O(n)
        while True: #O(n)
            try:
                valor = int(input("ingresa el numero total de elementos: "))  #O(1)
                return valor #O(1)
            except ValueError: #O(1)
                print("ingresa un numero valido graveeeeeeeeeee") #O(1)
        
    def valorN(): #O(n)
        while True: #O(n)
            try:
                valor = int(input("ingresa el numero de elementos que se seleccionaran: ")) #O(1)
                return valor #O(1)
            except ValueError: #O(1)
                print("ingresa un numero valido graveeeeeeeeeee") #O(1)
            
    def ingresarRepetidos(): #O(n)
        lista_numeros = [] #O(1)
        
        while True: #O(n)
            valor_str = input("Por favor, ingresa la cantidad de veces que se repite algo (\nsi ya los ingresaste todos digita 'fin' para terminar): ") #O(1)
            
            if valor_str.lower() == 'fin': #O(1)
                break
            
            try:
                valor = int(valor_str) #O(1)
                lista_numeros.append(valor) #O(1)
            except ValueError: #O(1)
                print("Eso no parece ser un número entero válido graveeeeeeeeeeeeeeee") #O(1)
        
        return lista_numeros #O(1)
    
    def intro(): #O(1)
        introduccion = (
            "Introducción a los Principios de Conteo: \n\n"
            "Los Principios de Conteo son reglas básicas utilizadas en combinatoria para contar el número "
            "de posibles resultados en un experimento o evento. Son fundamentales para determinar la "
            "cantidad de formas en que se puede realizar una tarea o evento en particular.\n\n"
            "Los dos principales principios son:\n\n"
            "1. Principio de la Multiplicación:\n"
            "   Este principio establece que si una tarea se puede realizar en 'm' formas diferentes y otra tarea "
            "independiente se puede realizar en 'n' formas diferentes, entonces ambas tareas combinadas se pueden "
            "realizar en 'm * n' formas diferentes.\n\n"
            "2. Principio de la Adición:\n"
            "   Este principio se aplica cuando una tarea se puede realizar de 'm' formas diferentes o de 'n' formas "
            "diferentes. La cantidad total de formas diferentes para que ocurra al menos una de estas tareas es 'm + n'.\n\n"
        )  #O(1)

        print(introduccion) #O(1) 