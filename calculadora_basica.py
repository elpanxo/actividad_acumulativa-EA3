def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    else:
        return a / b

try:
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    print("\nOpciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        print(f"Resultado de sumar {num1} y {num2}: {sumar(num1, num2)}")
    elif opcion == 2:
        print(f"Resultado de restar {num1} y {num2}: {restar(num1, num2)}")
    elif opcion == 3:
        print(f"Resultado de multiplicar {num1} y {num2}: {multiplicar(num1, num2)}")
    elif opcion == 4:
        resultado_division = dividir(num1, num2)
        print(resultado_division)
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

except ValueError:
    print("Error: Ingrese solamente números enteros.")
except Exception:
    print("Error inesperado.")
