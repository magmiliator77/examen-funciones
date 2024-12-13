# 2. Cortar una cadena (2 puntos): Crear un programa que pida al usuario una frase. Además pedirá una posición de inicio y una posición de fin. El programa deberá sacar por pantalla la parte de la frase que va desde la posición de inicio hasta la posición de fin. Es necesario controlar que la posición de inicio y la de fin sean válidas (en caso contrario, se debe dar error, mostrar un mensaje explicativo y volver a preguntar al usuario). Se debe dar la posibilidad de reiniciar todo el proceso o salir del programa.


repetir = 's'

while repetir == 's':

    # Pedimos la frase al usuario

    print("Introduce una frase:")

    frase = input()



    # Validamos posición de inicio

    inicio_valido = False

    while inicio_valido == False:

        print("Introduce la posición de inicio:")

        inicio = input()

        if inicio.isnumeric():

            #isnumeric --> #Devuelve Verdadero si la cadena es numérica, Falso en caso contrario.

            inicio = int(inicio)

            if 0 <= inicio < len(frase):

                inicio_valido = True


            else:
                print(f"Por favor, introduce un número entre 0 y {len(frase) - 1}.")
        
        else:
            print("Por favor, introduce un número entero.")


    # Validamos posición de fin
    fin_valido = False

    while fin_valido == False:

        print("Introduce la posición de fin:")

        fin = input()

        if fin.isnumeric():

            #isnumeric --> #Devuelve Verdadero si la cadena es numérica, Falso en caso contrario.


            fin = int(fin)

            if inicio < fin <= len(frase):


                fin_valido = True

            else:

                print(f"Por favor, introduce un número mayor que {inicio} y menor o igual a {len(frase)}.")

        else:
            print("Por favor, introduce un número entero.")

    # Mostramos la parte seleccionada de la frase

    print(f"La parte seleccionada de la frase es: {frase[inicio:fin]}")

    #aqui he utilizado un tecnica llamada slicing, en Python sirve para manipular y extraer partes de secuencias (como cadenas, listas o tuplas) de manera flexible. De esta manera se puede extraer datos más rapidamente y eficientemente


    # Preguntamos si desea reiniciar
    print("¿Quieres repetir el proceso? (s/n):")
    repetir = input().strip().lower()

print("¡Hasta luego máquina!")
