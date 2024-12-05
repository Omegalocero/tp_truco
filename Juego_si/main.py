from os import system
system("cls")
from Elements.auxiliares import*
from Elements.partida import*
from Elements.historial import*

juego = True
while juego == True:
    opcion = menu()
    match opcion:
        case "1":
            iniciar_partida()
        case "2":
            nombre = input("Ingrese el nombre del jugador: ")
            mostrar_historial_personal(nombre)
        case "3":
            print("Vuelve pronto si quieres perder")
            juego = False