
from Objeto import Objeto


# Clase para la maquina de la fabrica
class Maquina(Objeto):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.encendida = False

    # Encender la maquina
    def encender(self):
        self.encendida = True
        print(self.nombre, "esta encendida")

    # Apagar la maquina
    def apagar(self):
        self.encendida = False
        print(self.nombre, "esta apagada")

    # Trabajar con la maquina
    def trabajar(self, carro):

        if self.encendida:
            print("La maquina esta trabajando")
            carro.ensamblar()
        else:
            print("Primero debe encender la maquina")
