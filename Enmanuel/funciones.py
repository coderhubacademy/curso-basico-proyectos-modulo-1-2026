import json
import os  # importamos os porque nos ayuda a buscar archivos y carpetas en nuestra computadora


RUTA_DATOS = os.path.join(os.path.dirname(__file__), "data", "inventario.json")
# __file__ es donde esta el archivo app.py
# dirname es la carpeta donde esta el archivo app.py
# join es para unir las carpetas
# data es la carpeta donde esta el archivo inventario.json


def cargar_inventario():
    # muestra los datos del archivo json
    # primero vemos si el archivo existe
    if os.path.exists(RUTA_DATOS):
        # abrimos el archivo en modo lectura
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()  # leemos todo el texto
            if contenido.strip() == "":  # si esta vacio o en blanco
                return []  # devolvemos una lista vacia
            return json.loads(
                contenido
            )  # se utiliza para convertir una cadena de texto a un objeto de Python

    return (
        []
    )  # si el archivo no existe o no hay datos entonces empezamos con una lista vacia


def guardar_inventario(inventario):
    # esta funcion toma nuestro inventario y lo guarda en el archivo
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        # "W" escribir dentro del archivo
        json.dump(inventario, archivo, ensure_ascii=False)
        # ensure_ascii=False es para que el nombre del producto no salga asi EJ: "café" y no "caf\u00e9"


def generar_codigo(inventario):
    # esta funcion crea un codigo unico para cada producto nuevo EJ: PROD-005

    # si el inventario esta vacio, sera nuestro primer producto: PROD-001
    if len(inventario) == 0:
        return "PROD-001"

    # aqui buscamos cual es el numero mas grande que ya hemos usado en los codigos
    numero_mayor = 0
    for producto in inventario:
        # tomamos el ID del producto actual EJ: PROD-003
        ID = producto.get("ID", "PROD-000")
        try:
            # cortamos el texto por el guion "-" y nos quedamos con el numero: "003" y lo volvemos numero
            numero = int(ID.split("-")[1])
            if numero > numero_mayor:
                numero_mayor = numero  # actualizamos el numero mas grande guardado
        except:
            pass  # si pasa algun error raro con un codigo, lo ignoramos y seguimos

    # el nuevo numero sera el mayor de los que teniamos, mas 1
    nuevo_numero = numero_mayor + 1
    # juntamos la palabra "PROD-" y el numero nuevo con ceros a la izquierda 004, 015, etc
    return f"PROD-{nuevo_numero:03d}"


def buscar_por_nombre_o_codigo(inventario, termino):
    # esta funcion sirve para buscar un producto en nuestro inventario
    # puede ser buscando por su nombre "manzana" o por su codigo "PROD-002"

    termino = (
        termino.strip().upper()
    )  # convertimos la busqueda en mayusculas para que sea facil comparar
    for producto in inventario:
        nombre_upper = producto[
            "nombre"
        ].upper()  # el nombre del producto en mayusculas
        ID_upper = producto["ID"].upper()  # el codigo del producto en mayusculas

        # si la palabra que buscamos esta dentro del nombre, o es exactamente igual al codigo...
        if termino in nombre_upper or termino == ID_upper:
            return producto  # encontramos el producto, lo devolvemos para poder usarlo

    return None  # si revisamos toda la lista y no encontramos nada, retornamos none


def registrar_producto(inventario):
    # regristra un nuevo producto en el inventario
    print("\n REGISTRAR NUEVO PRODUCTO ")

    # pedimos el nombre y la categoria
    nombre = input("  Nombre del producto : ").strip()
    categoria = input("  Categoría        : ").strip()

    # pedimos el precio y la cantidad en stock
    try:
        precio = float(
            input("  Precio ($)          : ")
        )  # float para precio con decimales
        cantidad = int(input("  Cantidad en stock   : "))  # int para cantidad entera
    except ValueError:
        # si el usuario escribio letras en la pregunta del precio, le decimos que hay un error
        print("Error: el precio y la cantidad deben ser numeros validos.")
        return  # cancelamos la tarea

    # usamos nuestra otra funcion de buscar para asegurarnos de no tener productos con el mismo nombre repetido
    if buscar_por_nombre_o_codigo(inventario, nombre):
        print(f" Ya existe un producto con el nombre '{nombre}'.")
        return  # cancelamos para no tener prodcutos repetidos

    # generar ID para el nuevo producto
    ID = generar_codigo(inventario)

    # creamos un diccionario donde adentro ponemos toda la informacion del producto
    nuevo_producto = {
        "ID": ID,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
    }

    # .append para agregar nuestro nuevo producto al inventario
    inventario.append(nuevo_producto)

    # guardamos los cambios en el archivo
    guardar_inventario(inventario)
    print(f"Producto '{nombre}' registrado con ID {ID}.")


def listar_productos(inventario):
    # esta funcion nos muestra todos los productos que tenemos en el inventario
    print("\n INVENTARIO COMPLETO")

    # si revisamos la lista y no hay ningun producto, entonces mostramos un mensaje
    if len(inventario) == 0:
        print("No hay productos registrados aun.")
        return

    # coloco una linea separadora bonita repitiendo "─" 68 veces para el encabezado de los productos
    # vamos leyendo producto por producto para colocarlo
    print(
        f"\n  {'#':<4} {'Código':<10} {'Nombre':<20} {'Precio':>10} {'Stock':>6} {'Categoría':<15}"
    )
    print("  " + "─" * 68)

    # enumerate nos ayuda a llevar un conteo facil de que numero de lista es (1, 2, 3...etc)
    for numero, producto in enumerate(inventario, start=1):
        # acomodamos toda la información de nuestro diccionario adentro del texto, usando < > para alinear
        print(
            f"  {numero:<4} "
            f"{producto['ID']:<10} "
            f"{producto['nombre']:<20} "
            f"${producto['precio']:>9.2f} "  # .2f significa que muestra solo 2 numeros decimales del precio
            f"{producto['cantidad']:>6} "
            f"{producto['categoria']:<15}"
        )

    print(f"\n Total de productos: {len(inventario)}")


def buscar_producto(inventario):
    # le pide al usuario un producto por nombre o codigo y muestra su informacion detallada
    print("\n BUSCAR PRODUCTO ")

    termino = input("  Nombre o codigo a buscar: ").strip()
    producto = buscar_por_nombre_o_codigo(
        inventario, termino
    )  # usa otra vez a nuestra funcion buscadora

    if producto is None:  # si nos devuelve none no encontro nada
        print(f"No se encontro ningun producto con '{termino}'.")
        return

    # si lo encuentra, mandamos llamar a nuestra funcion de abajo que imprime bonito los datos
    mostrar_detalle_producto(producto)


def actualizar_producto(inventario):
    # esta funcion te deja modificar información de como cambiar el precio o la categoria de algo existente.
    print("\n ACTUALIZAR PRODUCTO ")

    termino = input("  Nombre o codigo del producto a actualizar: ").strip()
    producto = buscar_por_nombre_o_codigo(
        inventario, termino
    )  # primero debemos encontrarlo

    if producto is None:
        print(f" No se encontro ningun producto con '{termino}'.")
        return

    print("\n  Datos actuales (esto es lo que hay guardado antes de que cambies nada):")
    mostrar_detalle_producto(producto)

    # mostramos un menu para elegir que cosa exacta queremos modificar
    print("\n  ¿Qué dato deseas actualizar?")
    print("    [1] Nombre")
    print("    [2] Precio")
    print("    [3] Cantidad")
    print("    [4] Categoría")
    print("    [0] Cancelar y salir")

    opcion = input("Elige una opción: ").strip()

    try:
        # dependiendo del numero que escribio el usuario, cambiamos ese lado en el diccionario
        if opcion == "1":
            producto["nombre"] = input("  Nuevo nombre    : ").strip()
        elif opcion == "2":
            producto["precio"] = float(input("  Nuevo precio ($): "))
        elif opcion == "3":
            producto["cantidad"] = int(input("  Nueva cantidad  : "))
        elif opcion == "4":
            producto["categoria"] = input("  Nueva categoria : ").strip()
        elif opcion == "0":
            print("Operacion cancelada. Todo esta igual que antes.")
            return
        else:
            print("Opcion no valida. Debias escoger un numero del 0 al 4.")
            return
    except ValueError:
        print(
            "Error: escribiste un valor que no es texto o no es numero cuando debia serlo."
        )
        return

    # siempre que cambiamos algo en nuestra lista, debemos guardarlo en el archivo
    guardar_inventario(inventario)
    print(" ¡El producto ha sido actualizado de manera correcta!")
