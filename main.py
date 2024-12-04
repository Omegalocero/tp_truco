from os import system
from truco.Menu import menu
from truco.Historial import mostrar_historial, mostrar_historial_jugador
from truco.Bots import crear_bot_estrategico
from truco.Valores import crear_mazo, repartir_cartas
system("cls")

# Inicia el juego
juego = True
while juego:
    opcion = menu()
    match opcion:
        case "1":
            mazo = crear_mazo()  # Genera el mazo
            jugador1, jugador2 = repartir_cartas(mazo)  # Reparte cartas
            
            jugador = {"nombre": input("Ingrese su nombre: "), "cartas": jugador1, "puntos": 0}
            bot = crear_bot_estrategico("Bot Estratega")
            bot["cartas"] = jugador2

            print(f"\nTus cartas: {jugador['cartas']}")
            
            # Turno único
            carta_jugador = jugador["cartas"].pop(int(input("Selecciona una carta (1-3): ")) - 1)
            carta_bot = bot["cartas"].pop(0)
            print(f"Jugaste: {carta_jugador}, El bot juega: {carta_bot}")

            if carta_jugador["jerarquia"] > carta_bot["jerarquia"]:
                jugador["puntos"] += 1
                print("¡Ganaste el turno!")
            else:
                bot["puntos"] += 1
                print("El bot ganó el turno.")
        case "2":
            mostrar_historial()  # Muestra el historial general
        case "3":
            nombre = input("Ingrese el nombre del jugador: ")
            mostrar_historial_jugador(nombre)  # Muestra el historial de un jugador
        case "4":
            print("Gracias por jugar!!!.")
            juego = False
