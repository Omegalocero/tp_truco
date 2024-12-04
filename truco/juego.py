from truco.player import *
from truco.Bots import *
from truco.Valores import *
from truco.envido import *
from truco.Historial import *
import random

# === Funciones de inicialización === #
def inicializar_jugadores() -> tuple:
    """Inicializa los jugadores y retorna una tupla con ambos."""
    nombre_jugador = input("Ingrese su nombre: ").strip()
    player = jugador (nombre_jugador)

    nombre_oponente = random.choice(NOMBRES_MAQUINA)
    oponente = crear_bot_aleatorio(nombre_oponente)
    
    return jugador, oponente

def seleccionar_modo_juego() -> int:
    """Permite al jugador seleccionar el modo de juego (15 o 30 puntos)."""
    opcion_puntos = {
        "1": 15,
        "2": 30
    }

    seleccion = input("""\nSeleccione un modo de juego:
    1. 15 puntos.
    2. 30 puntos. 
    Ingrese una opción (1 o 2): """)

    while seleccion not in opcion_puntos:
        seleccion = input("""Opción inválida. Ingrese una opción válida (1 o 2): """)
    return opcion_puntos[seleccion]

def determinar_mano() -> bool:
    """Determina aleatoriamente quién es mano."""
    return random.choice([True, False])

# === Funciones de envido === #
def turno_envido(jugador: dict, oponente: dict) -> None:
    """Maneja la ronda de envido entre jugador y oponente."""
    puntos_jugador = calcular_envido(jugador["cartas"])
    puntos_oponente = calcular_envido(oponente["cartas"])
    
    print(f"\nTu puntaje de envido: {puntos_jugador}")
    print(f"El puntaje de envido del oponente se calculará después del canto.")

    canto = decidir_canto()
    if canto == "nada":
        print("No se cantó envido.")
        return

    print(f"{jugador['nombre']} cantó {canto}")
    print(f"{oponente['nombre']} dice: ¡Quiero!")

    if puntos_jugador > puntos_oponente:
        print(f"{jugador['nombre']} gana el envido con {puntos_jugador} puntos.")
        actualizar_puntajes(jugador, 2)
    else:
        print(f"{oponente['nombre']} gana el envido con {puntos_oponente} puntos.")
        actualizar_puntajes(oponente, 2)

# === Funciones de rondas === #
def manejar_ronda(jugador: dict, oponente: dict, ronda: int, es_mano_jugador: bool) -> tuple:
    """Maneja una ronda completa de juego."""
    print(f"\n=== Ronda {ronda + 1} ===")
    
    if es_mano_jugador:
        carta_jugador = seleccionar_carta(jugador["cartas"])
        carta_oponente = jugar_carta_aleatoria(oponente["cartas"])
    else:
        carta_oponente = jugar_carta_aleatoria(oponente["cartas"])
        carta_jugador = seleccionar_carta(jugador["cartas"])
    
    mostrar_jugada(jugador["nombre"], carta_jugador)
    mostrar_jugada(oponente["nombre"], carta_oponente)
    
    return carta_jugador, carta_oponente

def determinar_ganador_ronda(carta_jugador: dict, carta_oponente: dict) -> int:
    """Determina el ganador de la ronda."""
    if carta_jugador["jerarquia"] > carta_oponente["jerarquia"]:
        return 1
    elif carta_jugador["jerarquia"] < carta_oponente["jerarquia"]:
        return -1
    return 0

def actualizar_puntajes(ganador: dict, puntos: int) -> None:
    """Actualiza los puntajes de los jugadores."""
    ganador["puntos"] += puntos
    print(f"{ganador['nombre']} gana {puntos} puntos.")

# === Función principal === #
def iniciar_partida() -> None:
    """Inicia y coordina una nueva partida de truco."""
    print("\n=== ¡Bienvenido al Truco! ===")
    
    guardar_historial()
    jugador, oponente = inicializar_jugadores()
    modo_juego = seleccionar_modo_juego()
    es_mano_jugador = determinar_mano()
    
    partida_activa = True
    
    while partida_activa:
        mazo = crear_mazo(VALORES, PALOS)
        cartas_jugador, cartas_oponente = repartir_cartas(mazo)
        jugador["cartas"] = cartas_jugador
        oponente["cartas"] = cartas_oponente
        
        print(f"Mano: {jugador['nombre'] if es_mano_jugador else oponente['nombre']}")
        print("Tus cartas:")
        for carta in cartas_jugador:
            print(f"{carta['valor']} de {carta['palo']}")
        
        # Fase de envido
        turno_envido(jugador, oponente)
        
        # Fase de juego
        resultados_rondas = []
        for ronda in range(3):
            carta_jugador, carta_oponente = manejar_ronda(jugador, oponente, ronda, es_mano_jugador)
            resultado = determinar_ganador_ronda(carta_jugador, carta_oponente)
            resultados_rondas.append(resultado)
            
            if resultado == 1:
                actualizar_puntajes(jugador, 1)
            elif resultado == -1:
                actualizar_puntajes(oponente, 1)
        
        if jugador["puntos"] >= modo_juego or oponente["puntos"] >= modo_juego:
            ganador = jugador if jugador["puntos"] >= modo_juego else oponente
            print(f"\n¡{ganador['nombre']} ha ganado la partida!")
            guardar_historial(jugador, oponente, modo_juego)
            partida_activa = False
        
        es_mano_jugador = not es_mano_jugador
