eventos = []

def registrar_evento():
    nombre = input("ingresar nombre del evento: ")
    fecha = input("ingresar fecha del evento: ")
    descripcion= input("ingresar descripcion del evento: ")

def listar_eventos():
    print("eventos")
    for evento in eventos:
        print(evento)

def buscar_eventos():
    print(f"buscando evento")
    