from colorama import Fore, Style
import random
import time


valores = ["J" ,"Q" ,"K" , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_casa = []
simbolos_casa = []
valores_jugador = []
simbolos_jugador = []
simbolos = ["Picas", "Corazones", "Diamantes", "Treboles"]


def Sumar_listas(lista):
    contador = 0
    posicion = 0

    while posicion in range(len(lista)):
        try:
            contador += lista[posicion] 
            posicion +=1
        except :
            contador += 10
            posicion +=1

    return contador 


def Bienvenida():

    bienvenida = "Bienvenido a Blackjack"
    print((Fore.CYAN + Style.BRIGHT + bienvenida).center(121))
    print((Fore.WHITE + Style.BRIGHT + "Repartiendo cartas").center(121, "/"))


def agregar_jugador():

    valores_jugador.append(random.choice(valores))
    simbolos_jugador.append(random.choice(simbolos))
    return valores_jugador


def agregar_casa():

    valores_casa.append(random.choice(valores))
    simbolos_casa.append(random.choice(simbolos))
    return valores_casa


def Repartir():

    agregar_casa()
    agregar_casa()
    agregar_jugador()
    agregar_jugador()

    print(
        "Sus cartas son : {} de {} y {} de {}".format(
            valores_jugador[0],
            simbolos_jugador[0],
            valores_jugador[1],
            simbolos_jugador[1],
        )
    )
    print(
        "\nLa carta descubierta de la casa es {} de {}".format(
            valores_casa[0], simbolos_casa[0]
        )
    )



def Inicio_Juego():

    while True:
        suma_casa = Sumar_listas(valores_casa)
        suma_jugador = Sumar_listas(valores_jugador)

        if suma_casa > 21 or suma_jugador > 21:
            break
        else:
            seleccion = input("\n¿Que deseas hacer?\n-pasar\n-pedir\n")
            if seleccion == "pedir":
                agregar_jugador()
                print(
                    "\nSe ha agregado {} de {} a tu mano".format(
                        valores_jugador[-1], simbolos_jugador[-1]
                    )
                )
                suma_jugador = Sumar_listas(valores_jugador)
                time.sleep(0.5)
                print("\nActualmente la suma de tus cartas es {}".format(suma_jugador))

            elif seleccion == "pasar":
                time.sleep(0.5)
                print(
                    "\nLas cartas de la casa son {} de {} y {} de {}".format(
                        valores_casa[0],
                        simbolos_casa[1],
                        valores_casa[1],
                        simbolos_casa[1],
                    )
                )

                while suma_casa <= 16:
                    agregar_casa()
                    time.sleep(0.5)
                    print(
                        "\nSe ha agregado {} de {} a la mano de la casa".format(
                            valores_casa[-1], simbolos_casa[-1]
                        )
                    )
                    suma_casa = Sumar_listas(valores_casa)
                break
            else:
                print("Ingrese correctamente los datos")


def Ganador():

    suma_casa = Sumar_listas(valores_casa)
    suma_jugador = Sumar_listas(valores_jugador)
    time.sleep(0.5)
    if suma_jugador > 21 and suma_casa <= 21:
        print("\nLa casa ha ganado")
    elif suma_jugador <= 21 and suma_casa > 21:
        print("\nEl jugador ha ganado")
    elif suma_casa and suma_jugador > 21:
        print("\nNadie Gana")
    elif suma_casa < suma_jugador:
        print("\nEl jugador ha ganado")
    elif suma_jugador < suma_casa:
        print("\nLa casa ha ganado")
