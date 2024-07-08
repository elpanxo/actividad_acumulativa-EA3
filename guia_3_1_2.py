# Ejercicio 1
nombres = []
for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)

nombre_mas_largo = ""
for nombre in nombres:
    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre

print(f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}")


# Ejercicio 2
nombres = []
apellidos = []

for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    apellido = input(f"Ingrese el apellido {i+1}: ")
    nombres.append(nombre)
    apellidos.append(apellido)

print("\nNombres y apellidos ingresados:")
for i in range(3):
    print(f"{nombres[i]} {apellidos[i]}")


# Ejercicio 3
nombres = []

while True:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    
    respuesta = input("¿Desea agregar otro nombre? (sí/no): ")
    if respuesta.lower() == "no":
        break

nombre_menor_caracteres = nombres[0]
for nombre in nombres:
    if len(nombre) < len(nombre_menor_caracteres):
        nombre_menor_caracteres = nombre

nombres.remove(nombre_menor_caracteres)

print("\nLista de nombres actualizada:")
for nombre in nombres:
    print(nombre)


# Ejercicio 4
usuarios = {}

def iniciar_sesion():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso!")
    else:
        print("Usuario o contraseña incorrectos.")

def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    if usuario in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[usuario] = contraseña
        print("Usuario registrado correctamente.")

def eliminar_usuario():
    usuario = input("Ingrese el nombre de usuario que desea eliminar: ")
    contraseña = input("Ingrese la contraseña para confirmar la eliminación: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        del usuarios[usuario]
        print("Usuario eliminado correctamente.")
    else:
        print("Usuario o contraseña incorrectos.")

while True:
    print("\nMenú:")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        iniciar_sesion()
    elif opcion == '2':
        registrar_usuario()
    elif opcion == '3':
        eliminar_usuario()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-4).")


# Ejercicio 5
productos = {
    '1': {'nombre': 'Leche', 'precio': 1000},
    '2': {'nombre': 'Pan', 'precio': 500},
    '3': {'nombre': 'Huevos', 'precio': 2500},
    '4': {'nombre': 'Arroz', 'precio': 1500},
    '5': {'nombre': 'Aceite', 'precio': 2000}
}

carro_compras = []

def agregar_producto():
    print("\nProductos disponibles:")
    for clave, producto in productos.items():
        print(f"{clave}. {producto['nombre']} - ${producto['precio']}")

    seleccion = input("Seleccione el número de producto que desea agregar al carro (1-5): ")
    if seleccion in productos:
        carro_compras.append(productos[seleccion])
        print(f"{productos[seleccion]['nombre']} agregado al carro de compras.")
    else:
        print("Producto no válido.")

def ver_canasta():
    print("\nCarro de compras:")
    if carro_compras:
        for producto in carro_compras:
            print(f"{producto['nombre']} - ${producto['precio']}")
    else:
        print("El carro de compras está vacío.")

def ver_total():
    total = sum(producto['precio'] for producto in carro_compras)
    print(f"\nTotal a pagar: ${total}")

while True:
    print("\nMenú:")
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        ver_canasta()
    elif opcion == '3':
        ver_total()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-4).")