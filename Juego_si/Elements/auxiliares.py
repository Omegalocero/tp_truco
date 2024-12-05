def calcular_puntos_restantes(puntos_jugador: int, modo_juego: int) -> int:
    #Calcula los puntos restantes para ganar
    modos_validos = [15, 30]
    if modo_juego not in modos_validos:
        return 0  
    puntos_restantes = modo_juego - puntos_jugador
    
    if puntos_restantes <= 0:
        return 0
    return puntos_restantes 

def menu() -> str:
    opcion = input("""
        TRUCO ARGENTINO
    =====================
    1. Jugar partida
    2. Historial del jugador
    3. Salir 
    Seleccione una opcion: """)
    return opcion