# Divisas (tipos de cambio)

Mini-proyecto para practicar **consumo de APIs con `requests`**. Usa
[Frankfurter](https://www.frankfurter.app/) — gratis, sin clave, datos del BCE.

## Qué hace

- **Consultar**: muestra los tipos de cambio EUR → USD/GBP/JPY y guarda el
  resultado en `historial.json`.
- **Convertir**: convierte una cantidad de EUR a la moneda destino usando los
  tipos de cambio actualizados.
- **Historial**: muestra las consultas guardadas.

## Cómo ejecutar

```bash
cd /home/freybert/Work/tries/divisas
source .venv/bin/activate  (si no está activo)
python main.py
```

## Aprendido con este proyecto

- Consumir una **API distinta** a `precio-btc` (leer estructura JSON: `date`,
  `base`, `rates`).
- `requests.get` con `params`, `timeout=10`, `raise_for_status()`.
- `try/except` para controlar errores de red/timeout.
- Guardar y leer **JSON** (`json.dump` / `json.load`) en un archivo local.
- `.gitignore` (no subir `.venv/`, datos ni `__pycache__/`).
- Buscar/documentarse: mirar la respuesta real de la API antes de codificar.

## Notas sobre la API

- Usa la URL: `https://api.frankfurter.dev/v1/latest`
- Parámetros: `base` y `symbols` (separados por coma)
- Respuesta incluye `date` (fecha de los tipos de cambio)
