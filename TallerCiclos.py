# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:44:45 2021

@author: laura
"""

# 1. El departamento de Seguridad de Transito de Barranquilla, desea saber de
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

# 2. Un Zoólogo pretende determinar el porcentaje de animales que hay en las
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

# 3. Una empresa se requiere calcular el salario semanal de cada uno de los n
# obreros que laboran en ella. El salario se obtiene de la siguiente forma:
# a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
# b. Si trabaja mas de 40 horas se le paga $20 por cada una de las primeras
# 40 horas y $25 por cada hora extra.


def salarioObreros():
    n = int(input("Ingresa el número de obreros: "))
    cont = 1

    while cont <= n:
        horas = float(input("Ingrese las horas trabajadas en la semana: "))
        if horas <= 40:
            salario = horas*20
        else:
            extra = horas - 40
            salario = 40 * 20 + (extra*25)
        print(f"El salario del obrero {cont} es de: ${salario}")
        cont += 1

# 4. Calcular el promedio de edades de hombres, mujeres y de todo un grupo
# de alumnos.


def promedioEdad():
    n = int(input("Ingrese número de alumnos: "))
    edadM = 0
    edadH = 0
    mujer = 0
    hombre = 0
    grupo = 0

    for i in range(n):
        genero = input("Ingrese el género del alumno (mujer - hombre): ")
        if genero == "mujer":
            edadM += int(input("Ingrese edad de la mujer: "))
            mujer += 1
        elif genero == "hombre":
            edadH += int(input("Ingrese edad del hombre: "))
            hombre += 1
    promM = edadM / mujer
    promH = edadH / hombre
    grupo = edadM + edadH
    promGrupo = grupo / n
    print(f"El promedio de edades de mujeres es: {promM} años")
    print(f"El promedio de edades de hombres es: {promH} años")
    print(f"El promedio de edades del grupo es: {promGrupo} años")

# 5. Encontrar el menor valor de un conjunto de n números dados


def valorMenor():
    n = int(input("Ingrese cantidad de números: "))
    num = []
    for i in range(n):
        num.append(float(input(f"Ingrese el número {i+1}: ")))
    menor = min(num)
    print(f"El número menor de los números ingresados es: {menor}")

# 6. Cinco miembros de un club contra la obesidad desean saber cuanto han
# bajado o subido de peso desde la última vez que se reunieron. Para esto se
# debe realizar un ritual de pesaje en donde cada uno se pesa en diez
# básculas distintas para así tener el pormedio mas exacto de su peso. Si
# existe diferencia positiva entre este promedio de peso y el peso de la última
# vez que se reunieron, significa que subieron de peso. Pero si la diferencia
# es negativa, significa que bajaron. Lo que el problema requere es que por
# cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
# cantidad de kilos que subió o bajó de peso


def peso():
    for i in range(5):
        peso = float(input(f"Ingrese el peso previo de la persona {i+1}: "))
        pActual = 0
        for j in range(10):
            pActual += float(input(f"Ingrese peso actual de la báscula #{j+1}: "))

        prom_peso = pActual / 10
        if prom_peso == peso:
            print(f"La persona {i+1} se MANTIENE en el peso con {peso} kg")
        elif prom_peso > peso:
            print(f"Tiene un promedio de: {prom_peso} kg")
            print(f"La persona {i+1} SUBIÓ de peso con {prom_peso-peso} kg")
        else:
            print(f"Tiene un promedio de: {prom_peso} kg")
            print(f"La persona {i+1} BAJÓ de peso con {peso-prom_peso} kg")

# 7. En un supermercado una ama de casa pone en su carrito los artículos que
# va tomando de los estantes. La señora quiere asegurarse de que el cajero
# le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
# artóculo anota su precio junto con la cantidad de artículos iguales que ha
# tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
# que irá gastando en los demás artículos, hasta que decide que ya tomó
# todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
# compra.


def calcularCompra():
    compra = True
    total = 0

    while compra:
        cant = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio por producto: "))
        total += cant * precio

        resp = input("¿Desea finalizar su compra? (si o no): ")
        if resp == "si":
            compra = False
    print(f"El total a pagar es de: ${total:,}")

# 8. Un teatro otorga descuentos según la edad del cliente, determinar la
# cantidad del dinero que el teatro deja de percibir por cada ua de las
# categorias. Tomar en cuenta que los niños menores de 5 años no pueden
# entrar al teatro y que existe un precio único en los asientos. Los descuentos
# se hacen tomando en cuenta el siguiente cuadro:
# Edad % - Descuento
# 5 – 14 -  35%
# 15-19 -   25%
# 20 – 45 - 10%
# 46 – 65 - 25%
# 66 en Adelante - 35%


def calcularDescuentos():
    cat1 = 0
    cat2 = 0
    cat3 = 0
    cat4 = 0
    cat5 = 0
    precio = float(input("Ingrese el precio del boleto: $"))
    abierto = True
    total = 0

    while abierto:
        edad = int(input("Ingrese edad: "))
        if edad < 5:
            print("No se permite la entrada de menores a 5 años")
        elif edad <= 14:
            descuento = precio * 0.35
            cat1 += descuento
        elif edad <= 19:
            descuento = precio * 0.25
            cat2 += descuento
        elif edad <= 45:
            descuento = precio * 0.1
            cat3 += descuento
        elif edad <= 65:
            descuento = precio * 0.25
            cat4 += descuento
        else:
            descuento = precio * 0.35
            cat5 += descuento
        print(f"El descuento es de: ${descuento:,}")
        total += descuento

        resp = input("¿Desea cerrar? (si o no): ")
        if resp == "si":
            abierto = False

    print(f"Por la categoria 1, el descuento aplicado total es de: ${cat1:,}")
    print(f"Por la categoria 2, el descuento aplicado total es de: ${cat2:,}")
    print(f"Por la categoria 3, el descuento aplicado total es de: ${cat3:,}")
    print(f"Por la categoria 4, el descuento aplicado total es de: ${cat4:,}")
    print(f"Por la categoria 5, el descuento aplicado total es de: ${cat5:,}")
    print(f"El total de descuentos: ${total:,}")

# 9. Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
# siguiente tabla:
# Valor vendido - Comisión
# Menor o igual que 20 Millones - 10%
# Mayor de 20 Millones y menor de 40 Millones - 15%
# Mayor o igual de 40 Millones y menor de 80 Millones - 20%
# Mayor o igual de 80 millones y menor de 160 Millones - 25%
# De 160 Millones en adelante - 30%
# Realice un método que diga cuanto vendió y la comisión de los 100 vendedores
# que tiene la empresa.


def calcularComision():
    for i in range(100):
        venta = float(input(f"Ingrese el valor vendido por {i+1} empleado: "))
        if venta <= 20000000:
            comision = venta * 1.1
        elif venta > 20000000 and venta < 40000000:
            comision = venta * 1.15
        elif venta >= 40000000 and venta < 80000000:
            comision = venta * 1.2
        elif venta >= 80000000 and venta < 160000000:
            comision = venta * 1.25
        else:
            comision = venta * 1.3
        print(f"El vendedor {i+1} vendió: ${venta:,}")
        print(f"La comisión es de: ${comision-venta:,}")
        print(f"El vendedor {i+1} recibe en total con comisión: ${comision:,}")

# 10. La empresa Encuestas S.A desea crear una función que les permita
# conocer de los 50.000 votos obtenidos por 3 candidatos, cual de estos fue
# el ganador o indicar si hubo empate y la cantidad de votos obtenidos.


def calcularVotos():
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0

    for i in range(50000):
        print("1 - candidato 1,  2 - candidato 2,  3 - candidato 3")
        voto = int(input(f"Ingrese a qué candidato fue el voto de {i+1}: "))

        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1

    if candidato1 > candidato2 and candidato1 > candidato3:
        print("GANÓ el candidato 1")
        print(f"Votos candidato 1: {candidato1}")
    elif candidato2 > candidato1 and candidato2 > candidato3:
        print("GANÓ el candidato 2")
        print(f"Votos candidato 2: {candidato2}")
    elif candidato3 > candidato1 and candidato3 > candidato1:
        print("GANÓ el candidato 3")
        print(f"Votos candidato 3: {candidato3}")
    elif candidato1 == candidato2:
        print("Hay empate entre candidato 1 y 2")
        print(f"Votos candidato 1: {candidato1} - candidato 2: {candidato2}")
    elif candidato1 == candidato3:
        print("Hay empate entre candidato 1 y 3")
        print(f"Votos candidato 1: {candidato1} - candidato 3: {candidato3}")
    elif candidato2 == candidato3:
        print("Hay empate entre candidato 2 y 3")
        print(f"Votos candidato 2: {candidato2} - candidato 3: {candidato3}")
