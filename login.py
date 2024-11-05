# Diccionario (guardado de datos)
usuarios = {}

# Registrar usuario
def registro():
    usuario = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    usuarios[usuario] = contrasena
    print("Registrado!")

# Mostrar todos los usuarios registrados
def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(f"- {usuario}")

# Funcion Login
def login():
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuarios.get(usuario) == contrasena:
        print(f"Bienvenido/a {usuario}")
    else:
        print("Usuario o contraseña incorrecto/s.")

# Menú principal
while True:
    print("\n1. Registrar usuario\n2. Mostrar usuarios\n3. Login\n4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registro()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        login()
    elif opcion == "4":
        print("Chau!")
        break
    else:
        print("Opción no válida :(")
