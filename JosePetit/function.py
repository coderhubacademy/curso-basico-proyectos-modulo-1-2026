import json

RUTA = "JosePetit/data/datos.json"

def registrar_reserva(lista):
    print("\n--- NUEVA RESERVA ---")
    cliente = input("Nombre del cliente: ")
    fecha = input("Fecha (DD/MM): ")
    hora = input("Hora (HH:MM): ")

    lista = []
    
    nueva = {"cliente": cliente, "fecha": fecha, "hora": hora}


    lista.append(nueva)
    
    guardar_datos(lista)
    
    print(f"Reserva de {cliente} registrada con éxito.")
    return lista

def guardar_datos(lista):
    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)
    print(">>> Datos guardados en el JSON.")

def eliminar_reserva(lista):
    print("--- LISTA DE RESERVAS ---")
   
    for i in len(lista):
        reserva = lista[i]
        print(f"{i}. Cliente: {reserva['cliente']} - Fecha: {reserva['fecha']}")
    
    
    indice = int(input("Ingresa el número de la reserva a eliminar: "))
    
    
    eliminada = lista.pop(indice)
    
    guardar_datos(lista)
    
    print(f"Reserva de {eliminada['cliente']} eliminada correctamente.")
    return lista

def listar_reserva():
    print("tu mami we")

def buscar_reserva():
    print("tumba la casa mami")

def modificar_reserva():
    print("no tengo batería")


