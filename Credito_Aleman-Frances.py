
#!/usr/bin/env python3

from abc import ABC, abstractmethod

#-------------------------------------------------------------------------------

class Credito(ABC):
    """
    Clase abstracta que define la estructura base de un credito
    """
    def __init__(self, monto, tasa_anual, plazo_meses):
        """
        Constructor base para inicializar los atributos comunes de un credito
        
        :param monto: Monto del prestamo
        :param tasa_anual: Tasa de interes anual
        :param plazo_meses: Plazo del credito en meses
        """
        self.monto = monto
        self.tasa_mensual = tasa_anual / 12
        self.plazo_meses = plazo_meses

    @abstractmethod
    def amortizacion(self):
        """
        Metodo abstracto que debe ser implementado por las clases derivadas
        para calcular la amortizacion
        """
        pass

    def __str__(self):
        return f'Monto: {self.monto}, Tasa Anual: {self.tasa_mensual * 12}, Plazo: {self.plazo_meses}'

#-------------------------------------------------------------------------------

class CreditoFrances(Credito):
    def amortizacion(self) -> float:
        """
        Calcula la cuota fija mensual de acuerdo al sistema frances de amortizacion

        :return: Cuota mensual fija
        """
        P = self.monto
        T = self.tasa_mensual
        N = self.plazo_meses
        cuota = (P * T) / (1 - (1 + T) ** -N)
        return round(cuota)

#-------------------------------------------------------------------------------

class CreditoAleman(Credito):
    def amortizacion(self) -> list:
        """
        Calcula las cuotas mensuales de acuerdo al sistema aleman de amortizacion

        :return: Lista de cuotas mensuales decrecientes
        """
        P = self.monto
        T = self.tasa_mensual
        N = self.plazo_meses
        cuota_capital = P / N
        cuotas = [(cuota_capital + (P - i * cuota_capital) * T) for i in range(N)]
        return [round(cuota) for cuota in cuotas]

#-------------------------------------------------------------------------------

def main():
    """
    Funcion principal que ejecuta los calculos de amortizacion para diferentes
    tipos de creditos y muestra los resultados
    """
    creditos = []

    creditos.append(CreditoFrances(120000000, 0.12, 60))
    creditos.append(CreditoAleman(120000000, 0.12, 60))

    for credito in creditos:
        print(credito)
        print("Amortizacion:", credito.amortizacion())
        print()

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()


