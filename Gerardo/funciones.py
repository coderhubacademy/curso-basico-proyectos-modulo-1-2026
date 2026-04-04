import os
import json

# Esto detecta la carpeta "Gerardo" sin importar dónde estés parado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DATA = os.path.join(BASE_DIR, "data", "data.json")

def cargar_datos():
    if not os.path.exists(RUTA_DATA):
        return []
    try:
        with open(RUTA_DATA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_datos(lista):
    # Si por alguna razón borras la carpeta 'data', esto la vuelve a crear
    carpeta = os.path.dirname(RUTA_DATA)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        
    with open(RUTA_DATA, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
#----------
#   APP
#----------

#registrar evento 

def registrar_evento(lista):
    print("Ingresar Datos del Nuevo Evento")
    print("-"*30)
    nombre = input("ingresar nombre del evento: ")
    fecha = input("ingresar fecha del evento: ")
    descripcion= input("ingresar descripcion del evento: ")

    nueva = {"nombre": nombre, "fecha": fecha, "descripcion": descripcion}
    lista.append(nueva)

    guardar_datos(lista)
    print(F"El Evento, {nombre} ha sido resgitrado")
    return lista

def listar_eventos(lista):
    
    if not lista:
        print("\n-----no hay  eventos")
    else:
        print("\n--- LISTA DE EVENTOS ---")

        for i, evento in enumerate(lista):
            print(f"{i+1}. Evento:{evento['nombre']}, ")
            print(f"   Fecha:  {evento['fecha']}")
            print(f"   Info:   {evento['descripcion']}")
            print("-" * 20)
        return lista

def buscar_eventos(lista):
    nombre = input("ingresar nombre del evento a buscar: ")
    encontrado = False
    for evento in lista:
        if evento['nombre'].lower() == nombre.lower():
            print(f"Evento encontrado: {evento['nombre']} - {evento['fecha']} - {evento['descripcion']}  ")
            encontrado = True
            break
    if not encontrado:
        print("no se encontro el evento")
        return lista

def eliminar_eventos(lista):
    if not lista:
        print("no hay eventos para eliminar")
        return lista
    listar_eventos(lista)

    try:
        opcion = int(input("ingrese el numero del evento a eliminar:"))
        indice = opcion - 1

        if 0 <= indice < len(lista):
            eliminada = lista.pop(indice)
            guardar_datos(lista)
            print(f"el evento {eliminada['nombre']} ha sido eliminado con exito")
        else:
            print("opcion invalida ese evento n oesta en al lista")
    except ValueError:
        print("error")

    return lista