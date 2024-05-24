#!/usr/bin/env python3
'''
Adivina un número (versión orientada a objetos)
Programado por Carlos Zayas <czayas@pol.una.py>
Febrero, 2019
'''

import random
import sys


class Adivina(object):
    def __init__(self, hasta=100, limite=10):
        """Constructor de la clase. Inicio del juego."""

        self.hasta    = hasta   # Valor tope para elegir número secreto
        self.limite   = limite  # Cantidad límite de intentos
        self._repetir = "s"     # Necesario para ingresar al ciclo while

        self.secreto  = random.randint(1, self.hasta)  # Número secreto
        self.apuesta  = 0                              # Intento del jugador
        self.intentos = self.limite                    # Intentos restantes

        titulo = "Adivina mi número"
        print(titulo + "\n" + "-" * len(titulo) + "\n")

        print("Estoy pensando en un número del 1 al {}.".format(self.hasta))
        print("Te doy", self.limite, "oportunidades para adivinarlo.")

    def apostar(self):
        """Ciclo principal del juego."""

        while self.puede:
            try:
                self.apuesta = int(input("¿Cuál creés que es? "))
                if 1 <= self.apuesta <= self.hasta:
                    self.intentos -= 1
                    if self.puede:
                        print(self.pista)
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, ingresa un número del 1 al {}.".format(self.hasta))
            except:
                sys.exit(0)

    def terminar(self):
        """Presenta el resultado de la partida."""

        if self.intentos:
            print("¡Felicidades!", end=" ")
            print("Lo conseguiste en", self.limite - self.intentos, "intentos.")
        else:
            print("Lo siento, perdiste.")

    @property
    def puede(self):
        """Retorna verdadero si se puede seguir intentando adivinar el número."""

        return (self.secreto != self.apuesta) and self.intentos

    @property
    def pista(self):
        """Retorna una pista para el jugador."""

        salida = "Mi número es "

        if self.secreto > self.apuesta:
            salida += "mayor"
        else:
            salida += "menor"

        return salida + ". Te quedan " + str(self.intentos) + " intentos."

    @property
    def repetir(self):
        """Getter: Devuelve verdadero si el jugador quiere repetir la partida."""

        return self._repetir == "s"

    @repetir.setter
    def repetir(self, opcion):
        """Setter: Almacena la opción del jugador (repetir o no la partida)."""

        self._repetir = opcion

    def __del__(self):
        """Destructor de la clase. Final del juego."""

        print("Fue un placer jugar contigo. ¡Hasta pronto!")


def parametros():
    """Captura y devuelve los parámetros numéricos de la línea de comandos."""

    return [int(x) for x in sys.argv[1:] if x.isdigit()]


def jugar(*args):
    """Función principal."""

    juego = Adivina(*args)

    while juego.repetir:
        juego.apostar()
        juego.terminar()
        juego.repetir = input("¿Querés jugar otra vez? (S/N) ").lower()


# ----------------
# Bloque principal
# ----------------

if __name__ == '__main__':
    jugar(*parametros())
