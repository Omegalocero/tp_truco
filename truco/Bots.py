
import random
from Valores import calcular_envido

NOMBRES_MAQUINA = [
    
    "Po Clalo", 
    "Pepe",
    "Mono dedo",
    "No sabe mentir",
    "Terminator",
    "tu Cuñao",
    "La Casa"
]
nombre = random.choice(NOMBRES_MAQUINA)

# Bot Aleatorio
def crear_bot_aleatorio(nombre: str) -> dict:
    """Crea un bot aleatorio con un nombre y puntos iniciales. -> dict"""
    return {"nombre": nombre, "puntos": 0, "cartas": []}

def decidir_envido_aleatorio(mano: list, envido_cantado: bool) -> str:
    """Decide si cantar envido basándose en la mano del jugador aleatorio. -> str"""
    palos = [carta["palo"] for carta in mano]
    puntos_envido = calcular_envido(mano)

    if not envido_cantado:
        if puntos_envido > 30:
            return "falta envido"
        elif len(set(palos)) < 3:  # Dos cartas del mismo palo
            return "envido"
    return "paso"

def jugar_carta_aleatoria(mano: list) -> dict:
    """Juega una carta aleatoria. -> dict"""
    carta_jugada = random.choice(mano)
    mano.remove(carta_jugada)
    return carta_jugada


# Bot Estratégico
def crear_bot_estrategico(nombre: str) -> dict:
    """
    Crea un bot estratégico con un nombre y puntos iniciales.
    """
    return {
        "nombre": nombre,
        "puntos": 0,
        "cartas": [],
    }

def decidir_envido_estrategico(mano: list) -> str:
    """
    Decide si cantar envido para el bot estratégico.
    """
    puntos_envido = calcular_envido(mano)
    if puntos_envido > 27:
        return "envido"
    return "paso"

def jugar_carta_estrategica(mano: list, carta_contraria: dict = None) -> dict:
    """
    Juega una carta estratégica:
    - Si juega primero: carta más alta.
    - Si juega segundo:
        - Emparda o gana con la más baja posible.
        - Si no puede, juega la más baja.
    """
    if carta_contraria:
        jugables = [carta for carta in mano if carta["jerarquia"] >= carta_contraria["jerarquia"]]
        if jugables:
            carta_jugada = min(jugables, key=lambda x: x["jerarquia"])
        else:
            carta_jugada = min(mano, key=lambda x: x["jerarquia"])
    else:
        carta_jugada = max(mano, key=lambda x: x["jerarquia"])

    mano.remove(carta_jugada)
    return carta_jugada