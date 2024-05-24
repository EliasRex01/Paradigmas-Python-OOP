#!/usr/bin/env python3
"""
Cotizaciones - Ejemplo de urllib y json

Asignatura: Paradigmas de la Programación, LCIk (FP-UNA)
Autor: Prof. Carlos Zayas (czayas en gmail)
Fecha: 26/10/2019 (creación)
"""

import urllib.request
import urllib.parse
import json
import os, ssl

BCPCOTREF = 'https://www.bcp.gov.py/webapps/web/cotizacion/diaria'
MELIZECHE = "https://dolar.melizeche.com/api/1.0/"

def obtener(url):
    '''Obtiene del URL la información publicada en formato JSON.'''
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context
    try:
        HEADERS = {'User-Agent': 'Mozilla/5.0'}
        REQ = urllib.request.Request(url, headers=HEADERS)
        RESP = urllib.request.urlopen(REQ)
        RESPDATA = RESP.read().decode("utf-8")
        lista = json.loads(RESPDATA)
    except urllib.error.URLError:
        lista = []
    return lista

def listar(lista):
    '''Imprime la lista retornada por la función obtener.'''
    claves = [key for key in lista[0].keys()]
    for item in lista:
        for clave in claves:
            print(clave, end=': ')
            print(item[clave], end=', ')
        print()

def cotiz(JSON):
    '''Retorna un diccionario de cotizaciones en base al JSON del BCP.'''
    cotizacion = {}
    for item in JSON:
        cotizacion[item['abreviatura']] = {
            'compra': int(float(item['compraCotizacion'])),
            'moneda': item['moneda']
        }
    return cotizacion

def tabla(JSON):
    '''Imprime tabla de cotizaciones en base al JSON del BCP.'''
    for item in JSON:
        print(item['abreviatura'],
            int(float(item['compraCotizacion'])),
            "(" + item['moneda'] + ")")

def main():
    '''Función principal.'''
    def pausa(): input("\nPresione Enter para continuar.\n")
    JSON = obtener(BCPCOTREF)
    listar(JSON)
    pausa()
    print(cotiz(JSON))
    pausa()
    tabla(JSON)
    pausa()
    print(obtener(MELIZECHE))

if __name__ == "__main__":
    main()
