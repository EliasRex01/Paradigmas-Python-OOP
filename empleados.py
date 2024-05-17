#!/usr/bin/env python3

'''
Empleados - Ejemplo de ejercicio con clases abstractas

Una compañía paga a sus empleados por semana.

Los empleados son de cuatro tipos:

- Empleados asalariados, que reciben un salario semanal fijo, sin importar el
  número de horas trabajadas.

- Empleados por horas, que reciben un sueldo por hora y pago por tiempo extra,
  por todas las horas trabajadas que excedan a 40 horas.

- Empleados por comisión, que reciben un porcentaje de sus ventas.

- Empleados asalariados por comisión, que reciben un salario base más un
  porcentaje de sus ventas.

Para este periodo de pago, la compañía ha decidido recompensar a los empleados
asalariados por comisión, agregando un 10% a sus salarios base.

La compañía desea implementar una aplicación en python que realice sus cálculos
de nómina en forma polimórfica.
'''

from abc import ABC, abstractmethod # ABC: Abstract Base Classes

#-------------------------------------------------------------------------------

class Empleado(ABC):
    ...
    Hola
    ...
  
    cantidad = 0 # Total de empleados

    def __init__(self, nombre, apellido):
      #doc_string es la de abajo
        ...
        Metodo constructor.
          
        nombre   : string
        apellido : string
        ...
      
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = 0
        Empleado.cantidad += 1

    def __str__(self):
        return self.__apellido + ', ' + self.__nombre + ': ' + str(self.sueldo())

    @abstractmethod
    def sueldo(self):
        pass

    @staticmethod
    def total():
        return Empleado.cantidad

#-------------------------------------------------------------------------------

class EmpleadoAsalariado(Empleado):

    def __init__(self, salario, *args):
        super().__init__(*args)
        self.__sueldo = salario

    def sueldo(self):
        return self.__sueldo

#-------------------------------------------------------------------------------

class EmpleadoHoras(Empleado):

    xhora = 30000 # Monto por hora
    extra = 20000 # Monto por hora que exceda las 40

    def __init__(self, horas, *args):
        super().__init__(*args)
        self.__horas = horas

    def sueldo(self):
        self.__sueldo = self.__horas * EmpleadoHoras.xhora
        if self.__horas > 40:
            self.__sueldo += (self.__horas - 40) * EmpleadoHoras.extra
        return self.__sueldo

#-------------------------------------------------------------------------------

class EmpleadoComision(Empleado):

    def __init__(self, ventas, porcentaje, *args):
        super().__init__(*args)
        self.__ventas = ventas
        self.__porcentaje = porcentaje

    def sueldo(self):
        self.__sueldo = self.__ventas * (self.__porcentaje / 100)
        return self.__sueldo

#-------------------------------------------------------------------------------

class EmpleadoAsalariadoComision(EmpleadoAsalariado, EmpleadoComision):

    def __init__(self, porcentaje_aumento, *args):
        super().__init__(*args)
        self.__porcentaje_aumento = porcentaje_aumento / 100

    def sueldo(self):
        self.__sueldo_asalariado = super().sueldo()
        self.__sueldo_comision = EmpleadoComision.sueldo(self)
        self.__aumento = self.__sueldo_asalariado * self.__porcentaje_aumento
        self.__sueldo = self.__sueldo_asalariado + self.__aumento + self.__sueldo_comision
        return self.__sueldo

#-------------------------------------------------------------------------------

def main():

    empleados = []

    try:
        empleados.append(Empleado('Empleado', 'Estandar'))
    except Exception as mensaje:
        print("Error:", mensaje)

    # No se puede instanciar una clase abstracta

    empleados.append(EmpleadoAsalariado(3000000, 'Empleado', 'Asalariado'))
    empleados.append(EmpleadoHoras(50, 'Empleado', 'Horas'))
    empleados.append(EmpleadoComision(8000000, 20, 'Empleado', 'Comision'))
    empleados.append(EmpleadoAsalariadoComision(10, 3000000, 6000000, 20, 'Empleado', 'AsalariadoComision'))

    for empleado in empleados:
        print(empleado)

    print('Total:', Empleado.total())

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
