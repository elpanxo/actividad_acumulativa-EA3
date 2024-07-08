import csv
import json

def es_run_ganador(run):
    terminaciones_ganadoras = ['92', '95', '84']
    for terminacion in terminaciones_ganadoras:
        if run.endswith(terminacion):
            return True
    return False

archivo_csv = "listadoRun.csv"
archivo_json = "ganadores.json"

ganadores = []

try:
    with open(archivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            run = row['run']
            nombre = row['nombre']

            if es_run_ganador(run):
                ganador = {
                    'run': run,
                    'nombre': nombre
                }
                ganadores.append(ganador)

    with open(archivo_json, mode='w', encoding='utf-8') as file:
        json.dump(ganadores, file, ensure_ascii=False, indent=4)

    print(f"Se han almacenado los RUT ganadores en el archivo '{archivo_json}' correctamente.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_csv}'. Verifica la ruta y el nombre del archivo.")
except Exception as e:
    print(f"Error inesperado: {e}")