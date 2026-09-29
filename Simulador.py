"""
Simulador de dados.

Este programa permite al usuario seleccionar diferentes tipos de dados
(D4, D6, D8, D10, D12 y D20) y elegir cuántos quiere lanzar.

Cada dado realiza una animación de lanzamiento y muestra su resultado
con un color diferente según el valor obtenido. Al finalizar, se calcula
el total y el promedio de los resultados.
"""

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
console.print(f"[deep_pink3]---BIENVENIDO AL SIMULADOR DE DADOS---[/deep_pink3]")
print("podras elegir entre los diferentes dados y mostraremos cuanto haz sacado\n")

# Menu de opciones
while True:

    print(f"[medium_purple1]---MENU---[/medium_purple1]")
    print("1. Lanzar dados")
    print("2. Analitica")
    print("3. Salir \n")

    try:
        opcion = int(input("elige una opcion:"))
    except ValueError:
        print("Debes introducir un numero")
        continue

    match opcion:

# Opcion donde escoges el tipo de dado y la cantidad de lanzadas del mismo
        case 1:
    
            print("1. D4 ")
            print("2. D6 ")
            print("3. D8")
            print( "4. D10 ")
            print("5. D12 ")
            print("6. D20")

            try:
                opcionDado = int(input("Que dado quieres lanzar? \n"))
            except ValueError:
                print("Debes introducir una opcion de numero valida")
                continue

# Logica de la seleccion de dados a traves de un submenu 
            match opcionDado:
                case 1:
                    print("Seleccionaste el D4")
                    caras = D4                                             

                case 2:
                    print("Seleccionaste el D6")
                    caras = D6

                case 3:
                    print("Seleccionaste el D8")
                    caras = D8

                case 4:
                    print("Seleccionaste el D10")
                    caras = D10

                case 5:
                    print("Seleccionaste el D12")
                    caras = D12

                case 6:
                    print("Seleccionaste el D20")
                    caras = D20

                case _:
                    print("Dado inexistente")
                    continue

# Logica de tirada de dado aleatorio segun la cara elegida con total y su promedio
            while True:
                try:
                    cantidad=int(input("cunatos dados lanzaras?\n"))

                    if cantidad > 0:
                        break
                    else:
                        print("Debe ser un numero mayor a 0")

                except ValueError:
                    print("introduce una cantidad en numeros")

            total = 0  

            for i in range(cantidad):

    # Animaccion del lanzamiento
                with Live(console=console, refresh_per_second=20, transient=True) as live:
                    for j in range(15):
                        numeroAleatorio = random.randint(1,caras)
                        live.update(Panel.fit(f"[yellow]{numeroAleatorio}[/yellow]"))
                        time.sleep(0.08)

                resultado = random.randint(1,caras)

    # Colores de los dados 
                if resultado == 1 : 
                    console.print(Panel.fit(f"[red] {resultado}[/red]"))
                elif resultado == caras :
                    console.print(Panel.fit(f"[green] {resultado}[/green]"))
                else:
                    console.print(Panel.fit(f"[yellow] {resultado}[/yellow]"))
                          
                total = total + resultado

            print("Total de la tira: ", total)

            promedio = total / cantidad

            print("Promedio de la tirada: ", promedio)

# Ampliacion a futuro del programa sobre analitica 
        case 2: 
            print("No esta disponible, proximamente analitica")
            pass

        case 3:
            print("Fin del simulador")
            break

        case _:
            print("opcion no valida")
       





