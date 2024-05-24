#!/usr/bin/env python3
'''
Cambio - Retorna cotización de monedas.
         (Ejemplo de uso del módulo cotiz)
'''

from cotiz import obtener, ficha, BCPCOTREF

cotiz_lista = obtener(BCPCOTREF)

if cotiz_lista:
    cambios = {}
    for dic in cotiz_lista:
        cambios[dic['abreviatura']] = dic['compraCotizacion']
    # Versión en comprensión de lista:
    # cambios = {dic['abreviatura']:dic['compraCotizacion']
    #            for dic in cotiz_lista}
    print(ficha(cambios, 0))
else:
    print("No se pudo obtener la tabla de cambios. ¿Hay conexión a Internet?")
