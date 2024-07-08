matriz_3d = [
    [
        ["amarillo", "rojo", "naranja"],
        ["verde", "blanco", "rojo"],
        ["amarillo", "blanco", "naranja"]
    ],
    [
        ["verde", "blanco", "amarillo"],
        ["rojo", "naranja", "verde"],
        ["blanco", "amarillo", "rojo"]
    ],
    [
        ["naranja", "verde", "blanco"],
        ["amarillo", "rojo", "Naranja"],
        ["Verde", "Blanco", "amarillo"]
    ]
] 

elemento = {
    "amarillo": 0,
    "rojo": 0,
    "naranja": 0,
    "verde": 0,
    "blanco": 0
    }

for matriz in matriz_3d:
    for fila in matriz:
        for color in fila:
            if color == "amarillo":
                elemento["amarillo"] += 1
            elif color == "rojo":
                elemento["rojo"] += 1
            elif color == "naranja":
                elemento["naranja"] += 1
            elif color == "verde":
                elemento["verde"] += 1
            elif color == "blanco":
                elemento["blanco"] += 1

print("Número de elementos 'amarillo':", elemento["amarillo"])
print("Número de elementos 'rojo':", elemento["rojo"])
print("Número de elementos 'naranja':", elemento["naranja"])
print("Número de elementos 'verde':", elemento["verde"])
print("Número de elementos 'blanco':", elemento["blanco"])