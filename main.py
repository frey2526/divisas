import json
from datetime import datetime
from pathlib import Path

import requests

API = "https://api.frankfurter.dev/v1/latest"
ARCHIVO = Path(__file__).parent / "historial.json"
MONEDAS = ["USD", "GBP", "JPY"]


def obtener_tipos(base="EUR"):
    """Pide a la API los tipos de cambio desde 'base'."""
    try:
        respuesta = requests.get(
            API,
            params={"base": base, "symbols": ",".join(MONEDAS)},
            timeout=10,
        )
        respuesta.raise_for_status()
    except requests.RequestException as error:
        print(f"Error al consultar la API: {error}")
        return None
    return respuesta.json()


def cargar_historial():
    if not ARCHIVO.exists():
        return []
    with ARCHIVO.open(encoding="utf-8") as f:
        return json.load(f)


def guardar_historial(historial):
    with ARCHIVO.open("w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)


def consultar(historial):
    datos = obtener_tipos()
    if datos is None:
        return

    fecha = datos["date"]
    print(f"\n[{fecha}] Tipos de cambio desde {datos['base']}:")
    for moneda, valor in datos["rates"].items():
        print(f"  1 {datos['base']} = {valor} {moneda}")

    historial.append({"fecha": fecha, "base": datos["base"], "rates": datos["rates"]})
    guardar_historial(historial)


def convertir():
    datos = obtener_tipos()
    if datos is None:
        return

    origen = datos["base"]
    moneda = input(f"Moneda destino ({', '.join(MONEDAS)}): ").strip().upper()
    if moneda not in datos["rates"]:
        print("Moneda no disponible.")
        return

    try:
        cantidad = float(input(f"Cantidad en {origen}: "))
    except ValueError:
        print("Eso no es un número.")
        return

    resultado = cantidad * datos["rates"][moneda]
    print(f"{cantidad} {origen} = {resultado:.2f} {moneda}")


def ver_historial(historial):
    if not historial:
        print("Todavía no hay consultas guardadas.")
        return
    for consulta in historial:
        partes = [f"{m} {v}" for m, v in consulta["rates"].items()]
        print(f"{consulta['fecha']}  base {consulta['base']}: {' | '.join(partes)}")


def main():
    historial = cargar_historial()
    print("=== TIPOS DE CAMBIO (divisas) ===")

    while True:
        opcion = input("Opción: 1 consultar, 2 convertir, 3 historial, salir: ").strip().lower()

        if opcion == "salir":
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            consultar(historial)
        elif opcion == "2":
            convertir()
        elif opcion == "3":
            ver_historial(historial)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
