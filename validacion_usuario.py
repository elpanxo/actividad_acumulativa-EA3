import csv

def crear_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"archivo CSV: {nombre_archivo} creado exitosamente") 

def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return list(csv.reader(archivo))
    
datos_csv = [
    ["Nombre", "Edad", "Comuna"],
    ["Juan", 21, "Puente Alto"],
    ["Maria", 30, "Concepcion"],
    ["Carlos", 22, "Viña del Mar"],
    ["Estela", 25, "Puerto Montt"]
]
crear_archivo_csv("datos.csv", datos_csv)
