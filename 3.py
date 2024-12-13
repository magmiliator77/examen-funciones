# 3. Ochenteros (2,25 puntos): Crear un programa que genere 100 números aleatorios entre 1900 y 2000 (serán como años de nacimiento de personas en el siglo XX). Guardaremos dichos números en una lista. Posteriormente recorreremos esa lista y contaremos cuántos de esos años son de los 80 (entre 1980 y 1989, ambos incluidos). Sacaremos por pantalla un mensaje en el que indicaremos que hay x personas que nacieron en los 80.


import random

# Generamos 100 números aleatorios entre 1900 y 2000
anios_nacimiento = []
for i in range(100):
    anios_nacimiento.append(random.randint(1900, 2000))

# Contamos  cuántos son de los años 80
contar_ochenteros = 0
for anio in anios_nacimiento:
    if 1980 <= anio <= 1989:
        contar_ochenteros += 1

# Mostramos el resultado
print(f"Hay {contar_ochenteros} personas que nacieron en los años 80.")











"""

████████████████████████████████████████
████████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█████████
█████▀▀░░░░░░░░░░░░░░░░░░░░░░░░░▀███████
████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████
███▀░░░░░▄▄▄░░░░░░░░▄▄▀███▄▄░░░░░░░█████
██░░░░░░▀▀▀███▄▄░░░█▄▄█▀█▀▀▀▀░▀░▄▄░▀▀███
█░░▄▄░▄▄░▄░░░█▀░░░░░░░░░░▀▄▄▄█▀▀▄░▀█░░▀█
█░░░░▄░▀▀░░▄█▀░░░░░░▄▄░░░░░░░▄▄▀██▄░█░░█
██░░░██░░░▀▀█▄░░░▀▀▀▄▀░▄▄▄███▀░▄█░░░▀░▄█
██▄░██▀█▀▄▄▄▄▄█▄▄▄▄▄▀▀█▀░░▄███▀█▀░░░▄▄██
███░████▄█▄░░█░░▄█░░▄▄███▀▀▀█▄▀░░░░▄████
███░▀██████████████▀▀▀▀█░░░▄▀▀░░░░▄█████
███░░██▀█▀██▀█▀░░▀█░░░░█▄█▀░░░░░▄███████
███░░░░▀▀▀██▄██▄▄██▀▀▀▀▀░░░░░▄▄█████████
██▀░░░░░░░░░░░░░░░░░░░░░░▄▄▄████████████
██▄░░░░░░░░░░░░░░░░░░▄▄█████████████████
████▄░░░░░░░░░▄▄▄▄▄█████████████████████
███████████████████████████████████████

"""