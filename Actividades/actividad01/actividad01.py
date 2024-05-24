#!/usr/bin/env python3
'''
Adivina un número (versión estructurada)
Programado por Carlos Zayas <czayas@pol.una.py>
Febrero, 2019
'''

import sys
import random

# ------
# Inicio
# ------

titulo = "Adivina mi número"

print(titulo + "\n" + "-" * len(titulo) + "\n")

limite = intentos = 0

# ---------------------
# Captura de parámetros
# ---------------------

args = sys.argv[1:3]  # Sólo toma los dos primeros parámetros

if args:
    limite = int(args.pop(0))
    if args:
        intentos = int(args.pop(0))

if not limite:
    try:
        limite = int(input("Número límite para elegir [100]: ") or 100) or 100
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sys.exit(0)

if not intentos:
    try:
        intentos = int(input("Cantidad máxima de intentos [10]: ") or 10) or 10
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sys.exit(0)

# ---------------
# Ciclo principal
# ---------------

repetir = "s"

while repetir == "s":

    secreto = random.randint(1, limite)
    apuesta = 0
    intento = 0

    print("Estoy pensando en un número del 1 al {}.".format(limite))
    print("Te doy", intentos, "oportunidades para adivinarlo.")

    # ----------------
    # Ciclo de partida
    # ----------------

    while (secreto != apuesta) and (intento < intentos):
        try:
            apuesta = int(input("¿Cuál crees que es? ") or 0)
        except KeyboardInterrupt:
            print("\nSaliendo...")
            sys.exit(0)
        intento += 1
        if secreto != apuesta:
            if secreto > apuesta:
                print("Mi número es mayor.")
            else:
                print("Mi número es menor.")
            print("Ese fue tu intento número", intento)

    # ----------------
    # Final de partida
    # ----------------

    if intento < intentos:
        print("¡Felicidades! Lo conseguiste en", intento, "intentos.")
    else:
        print("Lo siento, perdiste.")

    repetir = input("¿Querés jugar otra vez? (S/N) ").lower()

print("Fue un placer jugar contigo. ¡Hasta pronto!")
