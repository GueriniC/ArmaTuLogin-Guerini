class Cliente:
    def __init__(self, nombre, correo, edad, intereses):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.intereses = intereses

    def __str__(self):
        return f"Se creó el cliente: {self.nombre}."

    def comprar(self, producto, tienda):
        print(f"El cliente {self.nombre} compró {producto} en {tienda}.")
