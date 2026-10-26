
from Carro import Carro
from Empleado import Empleado
from Maquina import Maquina


# Crear los objetos
carro = Carro("Chevrolet", "Onix")
empleado = Empleado("Camilo", "Operario")
maquina = Maquina("Brazo robotico")


# Menu principal
while True:

    print("\n===== FABRICA CAMILO =====")
    print("1. Mostrar carro")
    print("2. Mostrar empleado")
    print("3. Encender maquina")
    print("4. Trabajar en la fabrica")
    print("5. Apagar maquina")
    print("6. Salir")

    opcion = input("Digite una opcion: ")

    # Mostrar informacion del carro
    if opcion == "1":
        carro.mostrar()

    # Mostrar informacion del empleado
    elif opcion == "2":
        empleado.mostrar()

    # Encender la maquina
    elif opcion == "3":
        maquina.encender()

    # Iniciar el trabajo
    elif opcion == "4":

        empleado.trabajar()
        maquina.trabajar(carro)

    # Apagar la maquina
    elif opcion == "5":
        maquina.apagar()

    # Salir del programa
    elif opcion == "6":
        print("Programa terminado")
        break

    else:
        print("Opcion incorrecta")
