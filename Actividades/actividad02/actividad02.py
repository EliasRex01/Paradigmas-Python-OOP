#!/usr/bin/env python3
'''
Actividad 02 - Ejercicios 1 y 2

Paradigmas de la Programación - Prof. Carlos Zayas
'''


def filtrar(objeto):
    '''
    Retorna listas de propiedades y métodos de un objeto.

    Filtra la lista de atributos y separa los llamables de los que no lo son.

    Parámetros:
        objeto      : cualquiera

    Retorna:
        propiedades : list
        metodos     : list
    '''
    propiedades, metodos = [], []

    for item in dir(objeto):
        atributo = getattr(objeto, item)
        if callable(atributo):
            metodos.append(item)
        else:
            propiedades.append(item)

    return propiedades, metodos


def tipo(objeto):
    '''
    Retorna descripción del tipo de dato del objeto recibido como parámetro.

    Usa la propiedad __name__ como clave para el diccionario de clases.

    Parámetros:
        objeto      : cualquiera

    Retorna:
        descripcion : str
    '''
    tipos = ['Numérico (escalar)', 'Alfanumérico (cadena)', 'Binario (bytes)',
             'Lógico (booleano)', 'Secuencia', 'Mapeo', 'Conjunto']

    clase = {'int':   tipos[0], 'float':     tipos[0], 'complex':    tipos[0],
             'str':   tipos[1],
             'bytes': tipos[2], 'bytearray': tipos[2], 'memoryview': tipos[2],
             'bool':  tipos[3],
             'list':  tipos[4], 'tuple':     tipos[4], 'range':      tipos[4],
             'dict':  tipos[5],
             'set':   tipos[6], 'frozenset': tipos[6]}

    try:
        descripcion = clase[type(objeto).__name__]
    except KeyError:
        descripcion = 'Desconocido'

    return descripcion


def main():
    '''
    Función principal.

    Se invoca automáticamente cuando este programa se ejecuta como principal.
    '''
    print('Ejercicio 1:\n')
    ejemplo = 'Algo'
    propiedades, metodos = filtrar(ejemplo)
    print('Tipo de objeto de ejemplo:', type(ejemplo).__name__)
    print('\nPropiedades:\n', propiedades, '\n\nMétodos:\n', metodos)

    print('\nEjercicio 2:\n')
    print(tipo(2.3))
    print(tipo('Hola'))
    print(tipo(b'00110100'))
    print(tipo(True))
    print(tipo([23, 'X']))
    print(tipo({'nombre': 'Carlos'}))
    print(tipo({'peras', 'naranjas', 'manzanas'}))
    print(tipo(None))  # NoneType


if __name__ == '__main__':
    main()
