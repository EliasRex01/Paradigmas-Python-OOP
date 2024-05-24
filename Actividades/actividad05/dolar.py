#!/usr/bin/env python3
'''
Dolar - Retorna la cotización del dólar a la fecha.
        (Ejemplo de uso del módulo cotiz)
'''

import sys
from cotiz import cotiz_dolar

valor = '' if len(sys.argv) <= 1 else sys.argv[1]

if valor:
    print(round(cotiz_dolar() * float(valor)), "Gs.")
else:
    print(round(cotiz_dolar()), "Gs.")
