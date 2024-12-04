from .Historial import mostrar_historial

from .player import jugador
def menu():
    print("Bienvenido al Truco")
    juego = True

    while juego:
        opcion = input("""
        =======================
        MENÚ PRINCIPAL
        =======================
        1. Jugar nueva partida.
        2. Ver historial general.
        3. Salir.
        Seleccione una opción: """)

        if opcion not in ["1", "2", "3"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            continue

        match opcion:
            case "1":
                nombre = input("Ingrese su nombre: ")
                player = nombre
                puntos_maximos = input("Ingrese los puntos máximos de la partida (15 o 30): ")
                while puntos_maximos not in ["15", "30"]:
                    print("Por favor, seleccione entre 15 o 30 puntos.")
                    puntos_maximos = input("Ingrese los puntos máximos de la partida (15 o 30): ")
                puntos_maximos = int(puntos_maximos)

                print("\nIniciando una nueva partida...")
                

            case "2":
                mostrar_historial()
                

            case "3":
                print("¡Gracias por jugar! Hasta pronto.")
                juego = False
    print("¡Gracias por jugar!")
    juego = False