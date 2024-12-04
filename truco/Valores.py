import random

VALORES = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
PALOS = ["espada", "basto", "oro", "copa"]

def crear_mazo() -> list:
    """Genera el mazo completo con jerarquía de valores del Truco. -> list"""
    jerarquia = {
        "1 espada": 14, "1 basto": 13, "7 espada": 12, "7 oro": 11,
        "3 espada": 10, "3 oro": 10, "3 copa": 10, "3 basto": 10,
        "2 espada": 9, "2 oro": 9, "2 copa": 9, "2 basto": 9,
        "1 oro": 8, "1 copa": 8,
        "12 espada": 7, "12 oro": 7, "12 copa": 7, "12 basto": 7,
        "11 espada": 6, "11 oro": 6, "11 copa": 6, "11 basto": 6,
        "10 espada": 5, "10 oro": 5, "10 copa": 5, "10 basto": 5,
        "7 copa": 4, "7 basto": 4,
        "6 espada": 3, "6 oro": 3, "6 copa": 3, "6 basto": 3,
        "5 espada": 2, "5 oro": 2, "5 copa": 2, "5 basto": 2,
        "4 espada": 1, "4 oro": 1, "4 copa": 1, "4 basto": 1
    }

    mazo = []
    for palo in PALOS:
        for valor in VALORES:
            carta = {
                "palo": palo,
                "valor": valor,
                "jerarquia": jerarquia.get(f"{valor} {palo}", 0),
                "valor_envido": valor if valor < 10 else 0
            }
            mazo.append(carta)
    return mazo

def repartir_cartas(mazo: list) -> tuple:
    
    random.shuffle(mazo)
    cartas_jugador1 = mazo[:3]
    cartas_jugador2 = mazo[3:6]
    return cartas_jugador1, cartas_jugador2

def mostrar_jugada(nombre_jugador: str, carta: dict) -> None:
    print(f"{nombre_jugador} juega: {carta['valor']} de {carta['palo']}")



"""pruebas"""
## Crear el mazo
#mazo = crear_mazo(VALORES, PALOS)
#
## Imprimir el mazo
#print("Mazo generado:")
#for carta in mazo:
#    print(carta)
#
## Repartir las cartas
#mano1, mano2 = repartir_cartas(mazo)
#
## Mostrar las manos repartidas
#print("\nCartas del jugador 1:")
#for carta in mano1:
#    print(carta)
#
#print("\nCartas del jugador 2:")
#for carta in mano2:
#    print(carta)
