from truco.Valores import*

def calcular_envido(mano: list) -> int:
    """
    Calcula el puntaje de envido para una mano.
    Retorna el puntaje máximo considerando cartas del mismo palo.
    """
    cartas_por_palo = {}
    
    # Agrupar las cartas por palo
    for carta in mano:
        palo = carta["palo"]
        valor = carta["valor"]
        
        if valor <= 7:  
            if palo not in cartas_por_palo:
                cartas_por_palo[palo] = []
            cartas_por_palo[palo].append(valor)
        
    # Calcular el puntaje máximo de los grupos de cartas
    puntos_maximos = 0
    for valores in cartas_por_palo.values():
        if len(valores) > 1:  
            valores_ordenados = sorted(valores, reverse=True)  
            dos_mayores = valores_ordenados[:2]  
            suma = sum(dos_mayores)
            puntos = suma + 20
            if puntos > puntos_maximos:
                puntos_maximos = puntos
                
    return puntos_maximos

def calcular_envido_combinado(mano: list) -> int:
    """
    Calcula los puntos de envido para una mano, combinando ambas estrategias.
    """
    # Filtrar combinaciones de cartas del mismo palo
    envido_pares = [
        (carta1, carta2)
        for i, carta1 in enumerate(mano)
        for carta2 in mano[i + 1:]
        if carta1["palo"] == carta2["palo"]
    ]

    if envido_pares:
        # Sumar los valores de envido de las dos cartas del mismo palo más 20 puntos
        puntos_envido_pares = max(
            carta1["valor_envido"] + carta2["valor_envido"] + 20
            for carta1, carta2 in envido_pares
        )
    else:
        puntos_envido_pares = 0

    # Calcular el envido usando la estrategia original
    puntos_envido_original = calcular_envido(mano)

    # Retornar el puntaje máximo
    return max(puntos_envido_pares, puntos_envido_original)

def calcular_real_envido(mano: list) -> int:
    """Calcula el puntaje del real envido."""
    real_envido = calcular_envido_combinado(mano) + 3
    return  real_envido

#def calcular_falta_envido(puntos_jugador: int, modo_juego: int) -> int:
#    falta_envido = calcular_puntos_restantes(puntos_jugador, modo_juego)
#    return falta_envido
