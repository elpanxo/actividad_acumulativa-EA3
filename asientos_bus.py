filas = 10
columnas = 4

asientos = [[0] * columnas for _ in range(filas)]

numero_asiento = 1
for i in range(filas):
    for j in range(columnas):
        asientos[i][j] = numero_asiento
        numero_asiento += 1

for i in range(filas):
    for j in range(columnas):
        print(asientos[i][j], end=' ')
    print()
