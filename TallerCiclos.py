# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:44:45 2021

@author: laura
"""

# El departamento de Seguridad de Transito de Barranquilla, desea saber de
# los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
# color. Conociendo el último digito de la placa de cada automóvil se puede
# determinar el color de la calcomanía utilizando la siguiente relación:
# DIGITO -  COLOR
# 1 o 2 - Amarilla
# 3 o 4 - Rosa
# 5 o 6 - Roja
# 7 u 8 - Verde
# 9 o 0 - Azul


def nCarros():
    aux = True
    amarilla = 0
    rosa = 0
    roja = 0
    verde = 0
    azul = 0
    contador = 0

    while(aux):
        placa = int(input("Ingrese la placa del automóvil: "))
        contador = contador + 1

        if(placa % 10 == 1 or placa % 10 == 2):
            amarilla = amarilla + 1
        elif(placa % 10 == 3 or placa % 10 == 4):
            rosa = rosa + 1
        elif(placa % 10 == 5 or placa % 10 == 6):
            roja = roja + 1
        elif(placa % 10 == 7 or placa % 10 == 8):
            verde = verde + 1
        elif(placa % 10 == 9 or placa % 10 == 0):
            azul = azul + 1

        fin = input("¿Desea detener y conocer los datos (si o no): ")
        if fin == "si":
            aux = False

    print(f"A la ciudad de Barranquilla entraron {contador} automóviles")
    print(f"Entran {amarilla} automóviles con calcomanía amarilla")
    print(f"Entran {rosa} automóviles con calcomanía rosa")
    print(f"Entran {roja} automóviles con calcomanía roja")
    print(f"Entran {verde} automóviles con calcomanía verde")
    print(f"Entran {azul} automóviles con calcomanía azul")
