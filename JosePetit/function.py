import json

def cargar_usuarios():
    try:
        with open("JosePetit/datos/usuarios.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No hay usuarios registrados. Iniciando base de datos...")
        return {}
    
    # esto es para el registro, por eso hay otro archivo, try/ except (aquí lo hago en llaves, descripciones en app.md)

def guardar_usuarios(datos):
    with open("JosePetit/datos/usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos():
      try:
        with open("JosePetit/datos/datos.json", "r", encoding="utf-8") as archivo:
            print("Datos cargados correctamente.")
            return json.load(archivo)
      except FileNotFoundError:
        print("Archivo no encontrado. Iniciando con lista vacía...")
        return [] 
       

       # misma funcion pero cambiandole por el try/except (felicidaes hice algo útil xd)

def guardar_datos(lista):
    with open("JosePetit/datos/datos.json", "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
        print("Datos guardados correctamente.")

        # lo que hace ensure_ascii es simplemente que los acentos se puedan ver en el .json
        # sin ensure_ascii, salen como en la primera reserva que intenté (vease en el .txt :/)
        # indent = 4 (4 espacios de identación)
        # encoding = "utf-8", estandar, pa que se puedan ver los acentos y tu nombre no salga como en los que ves en .txt

def registrar_reserva(lista):
      usuarios_registraos = cargar_usuarios()
      print("\n NUEVA RESERVA")
      while True:
           cliente = input("Ingrese su nombre de usuario:")

           if cliente in usuarios_registraos:
              print("Bienvenido Usuario {cliente}")
              fecha = input("Fecha (D/M): ")
              hora = input("Hora (H:M): ")
              descripcion = input("Descripción del evento:")

    
              nueva = {"cliente": cliente, "fecha": fecha, "hora": hora, "descripcion": descripcion}
              lista.append(nueva)
    
              guardar_datos(lista)
              print(f"Reserva de {cliente} registrada.")
              return lista
          
           else:
              print("Usuario no existente")

def listar_reserva(lista):
    if not lista:
        print("\nNo hay reservas en el sistema.")
    else:
        print("\n LISTADO DE RESERVAS ")

        n = 1
        
        for r in lista:
            print()
            print(f"{n} Cliente: {r['cliente']} | Fecha: {r['fecha']} | Hora: {r['hora']}")

            n = n + 1
            

def eliminar_reserva(lista):
    if not lista:
        print("\nLa lista está vacía, nada que eliminar.")
        return lista

    listar_reserva(lista)
    
    
    opcion = int(input("\n¿Qué número de reserva deseas eliminar? "))
    indice = opcion - 1
        
    if indice >= 0 and indice < len(lista):
        eliminada = lista.pop(indice)
        guardar_datos(lista)
        print(f"Reserva de {eliminada['cliente']} eliminada (lo lograste eeee).")
    else:
        print("Ese número no está en la lista.")

    return lista

def buscar_reserva(lista):
    nombre = input("Usuario a buscar: ").lower()
    encontrado = False  
    for r in lista:
        if nombre in r['cliente'].lower():
            print(f"Encontrado: {r['cliente']} - {r['fecha']} a las {r['hora']}")
            encontrado = True
    
    if not encontrado:
        print("Busque bien (no mentira, no está).")

def modificar_reserva(lista):
    if not lista:
        print("\nNada que modificar.")
        return lista 

    listar_reserva(lista)

    opcion = int(input("Número de reserva a modificar: "))
    indice = opcion - 1 
    
    if indice >= 0 and indice < len(lista):
           print(f"Editando a: {lista[indice]['cliente']}")
           lista[indice]['cliente'] = input("Nuevo nombre: ")
           lista[indice]['fecha'] = input("Nueva fecha: ")
           lista[indice]['hora'] = input("Nueva hora: ")
           lista[indice]['descripcion'] = input("Alguna descripción?")
           guardar_datos(lista)
           print("Reserva actualizada.")
    else:
           print("Número inválido.")

    
    return lista

