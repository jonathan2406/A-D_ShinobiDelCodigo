from tabulate import tabulate
import pandas as pd
from Operaciones import Operaciones

#clase encargada de hacer todas las pruebas con ejercicios especificos
class Pruebas: #O(n)

    def ejecuacionPruebas(): #O(n)
        resultados = [] #O(1)

        # Permutaciones ordinarias
        resultados.append(Pruebas.permutacioneOrdinarias1()) #O(1)
        resultados.append(Pruebas.permutacionesOrdinarias2()) #O(1)
        resultados.append(Pruebas.permutacionesOrdinarias3()) #O(1)

        # Permutaciones repetidas
        resultados.append(Pruebas.permutacionsRepetidas1()) #O(1)
        resultados.append(Pruebas.permutacionsRepetidas2()) #O(1)

        # Combinaciones ordinarias
        resultados.append(Pruebas.combinacionOrdinaria1()) #O(1)
        resultados.append(Pruebas.combinacionOrdinaria2()) #O(1)

        # Combinaciones repeticiones
        resultados.append(Pruebas.combinacionRepeticion1()) #O(1)
        resultados.append(Pruebas.combinacionRepeticion2()) #O(1)

        # Variaciones ordinarias
        resultados.append(Pruebas.variacionOrdinaria1()) #O(1)
        resultados.append(Pruebas.variacionOrdinaria2()) #O(1)

        # Variaciones repetidas
        resultados.append(Pruebas.variacionRepetida1()) #O(1)
        resultados.append(Pruebas.variacionRepetida2()) #O(1)

        # Crear DataFrame
        headers = ["Categoría", "Problema", "Resultado"]
        data = [] #O(n)
        for categoria, prueba in resultados:
            data.append([categoria, prueba[0], prueba[1]])

        df = pd.DataFrame(data, columns=headers) #O(n)
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False)) #O(n)

    # Permutaciones ordinarias
    def permutacioneOrdinarias1(): #O(n)
        categoria = "Permutaciones Ordinarias" #O(1)
        enunciado = "Contar el número de formas de ordenar los 5 libros en un estante." #O(1)
        resultado = Operaciones.permutacionOrdinaria(5) #O(n)
        assert resultado == 120, f"Error en {enunciado}: El resultado esperado es 120" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def permutacionesOrdinarias2(): #O(n)
        categoria = "Permutaciones Ordinarias" #O(1)
        enunciado = "En una competencia de atletismo, ¿de cuántas formas diferentes pueden llegar 8 corredores a la línea de meta?" #O(1)
        resultado = Operaciones.permutacionOrdinaria(8) #O(n)
        assert resultado == 40320, f"Error en {enunciado}: El resultado esperado es 40320" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def permutacionesOrdinarias3(): #O(n)
        categoria = "Permutaciones Ordinarias" #O(1)
        enunciado = "Calcular el número de formas de ordenar 5 colores diferentes en una fila." #O(1)
        resultado = Operaciones.permutacionOrdinaria(5) #O(n)
        assert resultado == 120, f"Error en {enunciado}: El resultado esperado es 120" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    # Permutaciones repetidas
    def permutacionsRepetidas1(): #O(n)
        categoria = "Permutaciones Repetidas" #O(1)
        enunciado = "¿Cuántas maneras hay de ordenar 9 bolos si 3 son rojos, 4 son azules y 2 son verdes?" #O(1)
        resultado = Operaciones.permutacionRepeticion(9, [3, 4, 2]) #O(n)
        assert resultado == 1260, f"Error en {enunciado}: El resultado esperado es 1260" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def permutacionsRepetidas2(): #O(n)
        categoria = "Permutaciones Repetidas" #O(1)
        enunciado = "En una reunión, hay 5 hombres, 2 mujeres y 3 niños. ¿De cuántas maneras pueden sentarse en una fila?" #O(1)
        resultado = Operaciones.permutacionRepeticion(10, [5, 2, 3]) #O(n)
        assert resultado == 2520, f"Error en {enunciado}: El resultado esperado es 2520" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    # Combinaciones ordinarias
    def combinacionOrdinaria1(): #O(1)
        categoria = "Combinaciones Ordinarias" #O(1)
        enunciado = "En una lotería, se eligen 6 números de un total de 49. ¿Cuántas combinaciones posibles hay?" #O(1)
        resultado = Operaciones.combinacionOrdinaria(49, 6) #O(1)
        assert resultado == 13983816, f"Error en {enunciado}: El resultado esperado es 13983816" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def combinacionOrdinaria2(): #O(1)
        categoria = "Combinaciones Ordinarias" #O(1)
        enunciado = "En un grupo de 7 personas, ¿de cuántas maneras diferentes se pueden elegir 3 para formar un equipo?" #O(1)
        resultado = Operaciones.combinacionOrdinaria(7, 3) #O(1)
        assert resultado == 35, f"Error en {enunciado}: El resultado esperado es 35" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    # Combinaciones repeticiones
    def combinacionRepeticion1(): #O(1)
        categoria = "Combinaciones Repeticiones" #O(1)
        enunciado = "En un juego de dados, ¿de cuántas formas se puede obtener una suma de 3 al lanzar 3 dados?" #O(1)
        resultado = Operaciones.combinacionRepeticion(3, 3) #O(1)
        assert resultado == 10, f"Error en {enunciado}: El resultado esperado es 10" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def combinacionRepeticion2(): #O(1)
        categoria = "Combinaciones Repeticiones" #O(1)
        enunciado = "En un menú, hay 5 opciones de plato principal y se pueden elegir 4. ¿De cuántas maneras se pueden hacer las elecciones?" #O(1)
        resultado = Operaciones.combinacionRepeticion(5, 4) #O(1)
        assert resultado == 70, f"Error en {enunciado}: El resultado esperado es 70" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    # Variaciones ordinarias
    def variacionOrdinaria1(): #O(n)
        categoria = "Variaciones Ordinarias" #O(1)
        enunciado = "En un concurso de canto, 5 participantes cantarán 3 canciones. ¿Cuántas formas diferentes hay de organizar las canciones?" #O(1)
        resultado = Operaciones.variacionOrdinaria(5, 3) #O(n)
        assert resultado == 60, f"Error en {enunciado}: El resultado esperado es 60" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def variacionOrdinaria2(): #O(n)
        categoria = "Variaciones Ordinarias" #O(1)
        enunciado = "Se tienen 4 tarjetas de invitación y se deben elegir 2 para enviar. ¿Cuántas combinaciones diferentes de invitaciones se pueden hacer?"
        resultado = Operaciones.variacionOrdinaria(4, 2) #O(n)
        assert resultado == 12, f"Error en {enunciado}: El resultado esperado es 12" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    # Variaciones repetidas
    def variacionRepetida1(): #O(n)
        categoria = "Variaciones Repetidas" #O(1)
        enunciado = "Un dado de 6 caras se lanza 3 veces. ¿Cuántas formas diferentes hay de obtener el número 5?" #O(1)
        resultado = Operaciones.variacionRepeticion(5, 3) #O(n)
        assert resultado == 125, f"Error en {enunciado}: El resultado esperado es 125" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def variacionRepetida2(): #O(n)
        categoria = "Variaciones Repetidas" #O(1)
        enunciado = "En una competencia de natación, hay 3 estilos de nado y cada nadador debe realizar 5 estilos. ¿Cuántas formas diferentes hay de completar la competencia?" #O(1)
        resultado = Operaciones.variacionRepeticion(3, 5) #O(n)
        assert resultado == 243, f"Error en {enunciado}: El resultado esperado es 243" #O(1)
        return [categoria, [Pruebas.format_text(enunciado), resultado]] #O(1)

    def format_text(text): #O(n)
        max_width = 40 #O(1)
        lines = [text[i:i + max_width] for i in range(0, len(text), max_width)] #O(n)
        return '\n'.join(lines) #O(1)

