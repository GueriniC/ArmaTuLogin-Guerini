from paquete1.usuarios import registro, mostrar_usuarios, login

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
