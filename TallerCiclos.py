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

# Un Zoólogo pretende determinar el porcentaje de animales que hay en las
# siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
# de 3 o mas años. El zoológico todavía no está seguro del animal que va
# estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
# si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
# 40.


def porcentajeAnimales():
    categoria1 = 0
    categoria2 = 0
    categoria3 = 0

    animal = input("Escoja un animal (elefantes - jirafas - chimpancés): ")
    if (animal == "elefantes" or animal == "jirafas" or animal == "chimpancés" or animal == "chimpances"):
        if animal == "elefantes":
            muestra = 20
        elif animal == "jirafas":
            muestra = 15
        elif animal == "chimpancés" or animal == "chimpances":
            muestra = 40

        for i in range(muestra):
            edad = int(input("Ingrese la edad: "))

            if edad >= 0 and edad <= 1:
                categoria1 = categoria1 + 1
            elif edad > 1 and edad < 3:
                categoria2 = categoria2 + 1
            elif edad > 3:
                categoria3 = categoria3 + 1

        print(f"El porcentaje de edad del animal {animal} es: ")
        print(f"De 0 a 1 año: {(categoria1/muestra)*100}% ")
        print(f"De más de 1 y menos de 3 años: {(categoria2/muestra)*100}% ")
        print(f"De más de 3 años: {(categoria3/muestra)*100}% ")
    else:
        print("Escoja algún animal de los detallados")
