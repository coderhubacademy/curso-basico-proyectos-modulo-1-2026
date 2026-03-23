import json

RUTA = "JosePetit/data/datos.json"

def registrar_reserva(lista):
    print("--- NUEVA RESERVA ")
    cliente = input("Nombre del cliente: ")
    fecha = input("Fecha (D/M): ")
    hora = input("Hora (H:M): ")

    lista = []
    
    nueva = {"cliente": cliente, "fecha": fecha, "hora": hora}


    lista.append(nueva)
    
    guardar_datos(lista)
    
    print(f"Reserva de {cliente} registrada con éxito.")
    return lista

def guardar_datos(lista):
    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(lista, f)
    print(" Datos guardados en el JSON.")

def eliminar_reserva(lista):
    print(" LISTA DE RESERVAS: ")
   
    for i in range(len(lista)):
        reserva = lista[i]
        print(f"{i+1}. Cliente: {reserva['cliente']} - Fecha: {reserva['fecha']}")
    
    
    indice = int(input("Ingresa el número de la reserva a eliminar: "))
    
    
    eliminada = lista.pop(indice - 1)
    
    guardar_datos(lista)
    
    print(f"Reserva de {eliminada['cliente']} eliminada correctamente.")
    return lista

#def listar_reserva(lista):
    
    
def buscar_reserva(lista):
    nombre = input("Ingresa el nombre del cliente a buscar").lower()


   

#def modificar_reserva():

