#Constantes de los tipos de dados
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20

# Inicio y breve funcionalidad del programa para el usuario
print("BIENVENIDO AL SIMULADOR DE DADOS")
print("podras elegir entre los diferentes dados y mostraremos cuanto haz sacado")

# Menu de opciones
while True:

    print("---MENU---")
    print("1. Lanzar dados")
    print("2. Ver resultados")
    print("3. Salir")

    opcion = input("elige una opcion: ")

    match opcion:

        case "1":
            print("Que dado quieres lanzar?")
           

        case "2":
            print("Resultados de los dados")

        #Ampliacion de futuro programa
        case "3": 
            pass

        case "4":
            print("Fin del simulador")
            break

        case _:
            print("opcion no valida")
       





