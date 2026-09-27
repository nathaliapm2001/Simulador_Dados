# importacion de la libreria para usar el aleatorio
import random

# Constantes de los tipos de dados
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20

# variable de resultados, acumula los resultados de los dados
acumulador = 0

# Inicio y breve funcionalidad del programa para el usuario
print("BIENVENIDO AL SIMULADOR DE DADOS")
print("podras elegir entre los diferentes dados y mostraremos cuanto haz sacado")

# Menu de opciones
while True:

    print("---MENU---")
    print("1. Lanzar dados")
    print("2. Ver resultados")
    print("3. Analitica")
    print("4. Salir")

    opcion = input("elige una opcion: ")

    match opcion:

# Opcion donde escoges el tipo de dado y la cantidad de lanzadas del mismo
        case "1":
    
            print("Que dado quieres lanzar?")
            print("1. D4 ")
            print("2. D6 ")
            print("3. D8")
            print( "4. D10 ")
            print("5. D12 ")
            print("6. D20")

            opcionDado = input()

# Logica de la seleccion de dados a traves de un submenu 
            match opcionDado:
                case "1":
                    print("Seleccionaste el D4")
                    caras = D4
                    cantidad=int(input("cunatos dados lanzaras?"))          

                case "2":
                    print("Seleccionaste el D6")
                    caras = D6
                    cantidad=int(input("cunatos dados lanzaras?"))

                case "3":
                    print("Seleccionaste el D8")
                    caras = D8
                    cantidad=int(input("cunatos dados lanzaras?"))

                case "4":
                    print("Seleccionaste el D10")
                    caras = D10
                    cantidad=int(input("cunatos dados lanzaras?"))

                case "5":
                    print("Seleccionaste el D12")
                    caras = D12
                    cantidad=int(input("cunatos dados lanzaras?"))      

                case "6":
                    print("Seleccionaste el D20")
                    caras = D20
                    cantidad=int(input("cunatos dados lanzaras?"))

# Logica de los resultados de los dados y su media                    
        case "2":
            print("Resultados de los dados")

# Ampliacion de futuro del programa sobre analitica 
        case "3": 
            pass

        case "4":
            print("Fin del simulador")
            break

        case _:
            print("opcion no valida")
       





