
from Objeto import Objeto


# Clase para el carro
class Carro(Objeto):

    def __init__(self, marca, modelo):
        super().__init__("Carro")
        self.marca = marca
        self.modelo = modelo
        self.ensamblado = False

    # Mostrar los datos del carro
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)

        if self.ensamblado:
            print("Estado: Ensamblado")
        else:
            print("Estado: Sin ensamblar")

    # Funcion para ensamblar el carro
    def ensamblar(self):
        self.ensamblado = True
        print("El carro fue ensamblado")
