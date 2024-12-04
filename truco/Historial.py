import csv

def guardar_historial(resultado: dict, archivo: str = "historial.csv") -> None:
    """Guarda el resultado de la partida en un archivo CSV."""
    with open(archivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([resultado["jugador"], resultado["oponente"], resultado["puntos_jugador"], resultado["puntos_oponente"]])

def leer_historial(archivo: str = "historial.csv") -> list:
    """Lee el historial completo de un archivo CSV."""
    historial = []
    with open(archivo, mode="r") as file:
        reader = csv.reader(file)
        for fila in reader:
            historial.append({
                "jugador": fila[0],
                "oponente": fila[1],
                "puntos_jugador": int(fila[2]),
                "puntos_oponente": int(fila[3]),
            })
    return historial

def formatear_partida(partida: dict) -> str:
    """Devuelve un formato compacto de una partida."""
    ganador = partida["jugador"] if partida["puntos_jugador"] > partida["puntos_oponente"] else partida["oponente"]
    return (f"{partida['jugador']} ({partida['puntos_jugador']} pts) vs {partida['oponente']} ({partida['puntos_oponente']} pts). "
            f"Ganador: {ganador}")

def mostrar_historial() -> None:
    """Muestra el historial completo de partidas."""
    historial = leer_historial()
    if historial:
        print("\nHistorial de partidas:")
        for partida in historial:
            print(formatear_partida(partida))
    else:
        print("\nNo hay partidas registradas.")

def mostrar_historial_jugador(nombre_jugador: str) -> None:
    """Muestra el historial de un jugador específico."""
    historial = leer_historial()
    partidas_jugador = [p for p in historial if p["jugador"] == nombre_jugador]
    
    if partidas_jugador:
        print(f"\nHistorial de partidas de {nombre_jugador}:")
        for partida in partidas_jugador:
            print(formatear_partida(partida))
        
        ultima = partidas_jugador[-1]
        print("\nÚltima partida jugada:")
        print(formatear_partida(ultima))
    else:
        print(f"\nNo se encontraron partidas para {nombre_jugador}.")
