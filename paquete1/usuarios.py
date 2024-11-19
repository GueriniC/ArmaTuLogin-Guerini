# Diccionario (guardado de datos)
usuarios = {}

# Registrar usuario
def registro():
    usuario = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    usuarios[usuario] = contrasena
    print("¡Usuario registrado exitosamente!")

# Mostrar todos los usuarios registrados
def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(f"- {usuario}")

# Función Login
def login():
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuarios.get(usuario) == contrasena:
        print(f"Bienvenido/a {usuario}")
    else:
        print("Usuario o contraseña incorrecto/s.")
