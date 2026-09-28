# importacion de las librerias
import random
import time
from rich.panel import Panel
from rich.console import Console
from rich import print 
from rich.live import Live

# Constantes de los tipos de dados
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20


# variable de la cconsola de rich
console = Console()

# Inicio y breve funcionalidad del programa para el usuario
print("---BIENVENIDO AL SIMULADOR DE DADOS---")
print("podras elegir entre los diferentes dados y mostraremos cuanto haz sacado\n")

# Menu de opciones
while True:

    print("---MENU---")
    print("1. Lanzar dados")
    print("2. Analitica")
    print("3. Salir \n")

    opcion = input("elige una opcion:")

    match opcion:

# Opcion donde escoges el tipo de dado y la cantidad de lanzadas del mismo
        case "1":
    
            print("1. D4 ")
            print("2. D6 ")
            print("3. D8")
            print( "4. D10 ")
            print("5. D12 ")
            print("6. D20")

            opcionDado = input("Que dado quieres lanzar? \n")

# Logica de la seleccion de dados a traves de un submenu 
            match opcionDado:
                case "1":
                    print("Seleccionaste el D4")
                    caras = D4                                             

                case "2":
                    print("Seleccionaste el D6")
                    caras = D6

                case "3":
                    print("Seleccionaste el D8")
                    caras = D8

                case "4":
                    print("Seleccionaste el D10")
                    caras = D10

                case "5":
                    print("Seleccionaste el D12")
                    caras = D12

                case "6":
                    print("Seleccionaste el D20")
                    caras = D20
                 

                case _:
                    print("Dado inexistente")
                    continue

# Logica de tirada de dado aleatorio segun cara elegida con total y su promedio
            cantidad=int(input("cunatos dados lanzaras?\n"))

            total = 0  

            for i in range(cantidad):

# Animaccion del lanzamiento
                with Live(console=console, refresh_per_second=20) as live:
                    for j in range(15):
                        numeroAleatorio = random.randint(1,caras)
                        live.update(Panel(f"[yellow]{numeroAleatorio}[/yellow]"))
                        time.sleep(0.08)

                resultado = random.randint(1,caras)

# Colores de los dados 
                if resultado == 1 : 
                    console.print(Panel(f"[red] {resultado}[/red]"))
                elif resultado == caras :
                    console.print(Panel(f"[green] {resultado}[/green]"))
                else:
                    console.print(Panel(f"[yellow] {resultado}[/yellow]"))
                          
                total = total + resultado

            print("Total de la tira: ", total)

            promedio = total / cantidad

            print("Promedio de la tirada: ", promedio)

# Ampliacion de futuro del programa sobre analitica 
        case "2": 
            print("No esta disponible, proximamente analitica")
            pass

        case "3":
            print("Fin del simulador")
            break

        case _:
            print("opcion no valida")
       





