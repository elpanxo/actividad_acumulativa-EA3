def validar_lista_numeros(input_str):
    try:
        numeros = [int(num) for num in input_str.split()]
        return numeros
    except ValueError:
        return None

while True:
    numeros_input = input("Ingrese una lista de números enteros separados por espacios: ")
    numeros = validar_lista_numeros(numeros_input)
    if numeros is not None:
        break
    print("Error: Ingrese solamente números enteros separados por espacios.")

numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]

print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")