
from Objeto import Objeto


# Clase para el empleado
class Empleado(Objeto):

    def __init__(self, nombre, cargo):
        super().__init__("Empleado")
        self.nombre = nombre
        self.cargo = cargo

    # Mostrar los datos del empleado
    def mostrar(self):
        print("Nombre del empleado:", self.nombre)
        print("Cargo:", self.cargo)

    # Funcion para trabajar
    def trabajar(self):
        print(self.nombre, "esta trabajando en la fabrica")
