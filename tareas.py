from abc import ABC, abstractmethod
import pickle

class Persona(ABC):
    """
    Clase diferida que abstrae
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Tarea(ABC):
    """
    Clase diferida
    """
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        return f"{self.descripcion} - {'Completada' if self.completada else 'Pendiente'}"

    @abstractmethod
    def ejecutar_tarea(self):
        """
        operacion que
        """
        pass

class LimpiarJardin(Tarea):
    """
    Clase que abstrae la limpieza de jardin
    """
    def __init__(self):
        super().__init__("Limpiar el jardín")

    def ejecutar_tarea(self):
        print(f"Ejecutando tarea: {self.descripcion}")

class LavarRopa(Tarea):
    def __init__(self):
        super().__init__("Lavar la ropa")

    def ejecutar_tarea(self):
        print(f"Ejecutando tarea: {self.descripcion}")

class RealizarCompra(Tarea):
    def __init__(self):
        super().__init__("Realizar la compra")

    def ejecutar_tarea(self):
        print(f"Ejecutando tarea: {self.descripcion}")

class Integrante(Persona):
    """
    Clase que abstrae a un integrante
    """
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tareas_asignadas = []

    def asignar_tarea(self, tarea, integrante):
        integrante.recibir_tarea(tarea)

    def elegir_tarea(self, tarea):
        self.tareas_asignadas.append(tarea)

    def recibir_tarea(self, tarea):
        """
        Recibe una tarea asignada por otro integrante.
        """
        self.tareas_asignadas.append(tarea)

    def completar_tarea(self, tarea):
        """
        arca tarea como completa
        """
        if tarea in self.tareas_asignadas:
            tarea.marcar_completada()
            tarea.ejecutar_tarea()

    def __str__(self):
        tareas_str = ", ".join([str(tarea) for tarea in self.tareas_asignadas])
        return f"{self.nombre}: {tareas_str}"

class SistemaTareas:
    """
    Clase que abstrae el sistema de distribucion de tareas en el hogar
    """
    def __init__(self):
        self.integrantes = []

    def agregar_integrante(self, integrante):
        """
        Agrega un integrante al sistema.
        """
        self.integrantes.append(integrante)

    def buscar_integrante(self, nombre):
        """
        Busca un integrante por su nombre
        """
        for integrante in self.integrantes:
            if integrante.nombre == nombre:
                return integrante
        return None

    def guardar_datos(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def cargar_datos(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

def main():
    """
    Funciin principal 
    """
    # Crear el sistema de tareas
    sistema = SistemaTareas()

    # Crear integrantes
    juan = Integrante("Juan")
    maria = Integrante("Maria")
    sistema.agregar_integrante(juan)
    sistema.agregar_integrante(maria)

    # crear tareas
    tarea1 = LimpiarJardin()
    tarea2 = LavarRopa()
    tarea3 = RealizarCompra()
    juan.elegir_tarea(tarea1)
    maria.elegir_tarea(tarea2)
    juan.asignar_tarea(tarea3, maria)
    print(juan)
    print(maria)
    maria.completar_tarea(tarea3)
    print(juan)
    print(maria)
    sistema.guardar_datos('sistema_tareas.pkl')

    # cargar sistema
    nuevo_sistema = SistemaTareas.cargar_datos('sistema_tareas.pkl')
    for integrante in nuevo_sistema.integrantes:
        print(integrante)

if __name__ == "__main__":
    main()
