
#1. Múltiplos de 3 (2,25 puntos): Crear un programa que pida 1 número al usuario e indique si dicho número es múltiplo de 3. Para ello, debemos crear una función llamada "esMultiplode3" que devuelva true si el número que se pase como argumento es múltiplo de 3 y false si no. Utilizarla en el programa para mostrar un mensaje u otro al usuario. Al finalizar preguntará si quiere iniciar proceso de nuevo o salir.


# Definimos la función para verificar si un número es múltiplo de 3
def esMultiplode3(numero):
    return numero % 3 == 0



# Programa principal
repetir = 's'


while repetir == 's':

    print("Introduce un número para verificar si es múltiplo de 3:")

    numero_valido = False

    while numero_valido == False:

        numero = input()

        es_numero = True  # Suponemos que es un número

        i = 0

        while i < len(numero):

            if numero[i] < '0' or numero[i] > '9':  

            # Verificamos si no es un dígito
                es_numero = False

            i += 1

        if es_numero and len(numero) > 0:

            numero = int(numero)

            numero_valido = True

        else:

            print("Por favor, introduce un número válido:")

    # Verificamos si es múltiplo de 3
    if esMultiplode3(numero):

        print(f"El número {numero} es múltiplo de 3.")

    else:

        print(f"El número {numero} no es múltiplo de 3.")

    # Preguntar si desea repetir el proceso
    print("¿Quieres verificar otro número? (s/n):")
    repetir = input().strip().lower()

print("¡Hasta luego mastodonte!")
