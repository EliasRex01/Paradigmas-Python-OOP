
#!/usr/bin/env python3

from abc import ABC, abstractmethod

#-------------------------------------------------------------------------------

class Credito(ABC):
    """
    Clase abstracta que define la estructura base de un crédito.
    """
    def __init__(self, monto, tasa_anual, plazo_meses):
        """
        Constructor base para inicializar los atributos comunes de un crédito.
        
        :param monto: Monto del préstamo.
        :param tasa_anual: Tasa de interés anual.
        :param plazo_meses: Plazo del crédito en meses.
        """
        self.monto = monto
        self.tasa_mensual = tasa_anual / 12
        self.plazo_meses = plazo_meses

    @abstractmethod
    def amortizacion(self):
        """
        Método abstracto que debe ser implementado por las clases derivadas
        para calcular la amortización.
        """
        pass

    def __str__(self):
        return f'Monto: {self.monto}, Tasa Anual: {self.tasa_mensual * 12}, Plazo: {self.plazo_meses}'

#-------------------------------------------------------------------------------

class CreditoFrances(Credito):
    def amortizacion(self) -> float:
        """
        Calcula la cuota fija mensual de acuerdo al sistema francés de amortización.

        :return: Cuota mensual fija.
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
        Calcula las cuotas mensuales de acuerdo al sistema alemán de amortización.

        :return: Lista de cuotas mensuales decrecientes.
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
    Función principal que ejecuta los cálculos de amortización para diferentes
    tipos de créditos y muestra los resultados.
    """
    creditos = []

    creditos.append(CreditoFrances(120000000, 0.12, 60))
    creditos.append(CreditoAleman(120000000, 0.12, 60))

    for credito in creditos:
        print(credito)
        print("Amortización:", credito.amortizacion())
        print()

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()


