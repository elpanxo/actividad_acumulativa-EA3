filas = 3
columnas = 4

arreglo = [[0] * columnas for _ in range(filas)]

print("Ingrese los elementos del arreglo (separados por espacio):")
for i in range(filas):
    for j in range(columnas):
        arreglo[i][j] = int(input(f"Elemento [{i}][{j}]: "))

print("\nMatriz ingresada:")
for i in range(filas):
    for j in range(columnas):
        print(arreglo[i][j], end=' ')
    print()