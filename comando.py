#!/usr/bin/env python3
'''
Nombre:      Comando
Descripción: Ejemplo de implementación de un comando de consola.
Autor:       Carlos Augusto Zayas Guggiari
Fecha:       23/5/2024

sys.argv es un objeto de tipo lista que almacena los valores de los argumentos
(parámetros, atributos) de la línea de comandos que se usó para arrancar el
programa, incluido y empezando por el nombre de éste (índice 0).
'''

import sys

def main():
    '''
    Función principal.
    '''

    args = sys.argv[1:]  # Excluye el nombre del archivo.

    if args:

        while args:
            arg = args.pop(0)  # Extrae un argumento desde el inicio de la lista.
            # Acá se procesan los argumentos.
            print(arg)

    else:

        print('<Breve explicación de lo que hace el programa.>')
        print('"__main__" (trayectoria al archivo de programa ejecutado):\n', __file__)
        print('Sintaxis:', __name__, '[argumento1] [argumento2] ... [argumentoN]')
        print('\nEjemplo:\n<Ejemplo de llamada.>')


if __name__ == '__main__':
    main()
