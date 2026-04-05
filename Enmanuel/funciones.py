import json
import os  # importamos os porque nos ayuda a buscar archivos y carpetas en nuestra computadora

RUTA_DATOS = os.path.join(os.path.dirname(__file__), "data", "inventario.json")
# __file__ es donde esta el archivo app.py
# dirname es la carpeta donde esta el archivo app.py
# join es para unir las carpetas
# data es la carpeta donde esta el archivo inventario.json


def cargar_inventario():
    # muestra los datos del archivo json
    if os.path.exists(RUTA_DATOS):
        # abrimos el archivo en modo lectura
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                return []
            return json.loads(contenido)

    return (
        []
    )  # si el archivo no existe o no hay datos entonces empezamos con una lista vacia


def guardar_inventario(inventario):
    # esta funcion toma nuestro inventario y lo guarda en el archivo
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        # modo escritura
        json.dump(inventario, archivo, ensure_ascii=False)
        # ensure_ascii=False es para que el nombre del producto no salga asi EJ: "café" y no "caf\u00e9"


def generar_codigo(inventario):
    # esta funcion crea un codigo unico para cada producto nuevo EJ: PROD-005

    if len(inventario) == 0:
        return "PROD-001"

    numero_mayor = 0
    for producto in inventario:
        # tomamos el ID del producto actual EJ: PROD-003
        ID = producto.get("ID", "PROD-000")
        try:
            # cortamos el texto por el guion "-" y nos quedamos con el numero: "003" y lo volvemos numero
            numero = int(ID.split("-")[1])
            if numero > numero_mayor:
                numero_mayor = numero
        except:
            pass

    nuevo_numero = numero_mayor + 1
    # juntamos la palabra "PROD-" y el numero nuevo con ceros a la izquierda 004, 015, etc
    return f"PROD-{nuevo_numero:03d}"


def buscar_por_nombre_o_codigo(inventario, termino):
    # esta funcion es para buscar un producto en nuestro inventario

    termino = termino.strip().upper()

    for producto in inventario:
        nombre_upper = producto["nombre"].upper()
        ID_upper = producto["ID"].upper()

        # si la palabra que buscamos esta dentro del nombre, o es exactamente igual al codigo...
        if termino in nombre_upper or termino == ID_upper:
            return producto

    return None


def registrar_producto(inventario):
    # regristra un nuevo producto en el inventario
    print("\n REGISTRAR NUEVO PRODUCTO ")

    nombre = input("  Nombre del producto : ").strip()
    categoria = input("  Categoría        : ").strip()

    try:
        precio = float(input("  Precio ($)          : "))
        cantidad = int(input("  Cantidad en stock   : "))
    except ValueError:
        print("Error: el precio y la cantidad deben ser numeros validos.")
        return

    # esta funcion es para buscar un producto por su nombre o codigo
    if buscar_por_nombre_o_codigo(inventario, nombre):
        print(f" Ya existe un producto con el nombre '{nombre}'.")
        return

    ID = generar_codigo(inventario)

    nuevo_producto = {
        "ID": ID,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
    }

    inventario.append(nuevo_producto)

    guardar_inventario(inventario)
    print(f"Producto '{nombre}' registrado con ID {ID}.")


def listar_productos(inventario):
    # esta funcion nos muestra todos los productos que tenemos en el inventario
    print("\n INVENTARIO COMPLETO")

    if len(inventario) == 0:
        print("No hay productos registrados aun.")
        return

    # estetica
    print(
        f"\n  {'#':<4} {'Código':<10} {'Nombre':<20} {'Precio':>10} {'Stock':>6} {'Categoría':<15}"
    )
    print("  " + "─" * 68)

    # enumerate nos ayuda a llevar un conteo facil de que numero de lista es
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
    # funcion para buscar producto por nombre o codigo y mostrar los detalles del prodcuti
    print("\n BUSCAR PRODUCTO ")

    termino = input("  Nombre o codigo a buscar: ").strip()
    producto = buscar_por_nombre_o_codigo(
        inventario, termino
    )  # usa otra vez a nuestra funcion buscadora

    if producto is None:
        print(f"No se encontro ningun producto con '{termino}'.")
        return

    mostrar_detalle_producto(producto)


def actualizar_producto(inventario):
    # esta funcion es para cambiar el nombre de un producto y todo lo demas
    print("\n ACTUALIZAR PRODUCTO ")

    termino = input("  Nombre o codigo del producto a actualizar: ").strip()
    producto = buscar_por_nombre_o_codigo(inventario, termino)

    if producto is None:
        print(f" No se encontro ningun producto con '{termino}'.")
        return

    print("\n  Datos actuales (esto es lo que hay guardado antes de que cambies nada):")
    mostrar_detalle_producto(producto)

    # un menu para elegir que modificsr
    print("\n  ¿Que dato deseas actualizar?")
    print("    [1] Nombre")
    print("    [2] Precio")
    print("    [3] Cantidad")
    print("    [4] Categoría")
    print("    [0] Cancelar y salir")

    opcion = input("Elige una opcion: ").strip()

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

    guardar_inventario(inventario)
    print(" ¡El producto ha sido actualizado de manera correcta!")


def eliminar_producto(inventario):
    # ya me da ladilla explicar cada funcion aklsdjajsd
    print("\n ELIMINAR PRODUCTO ")

    termino = input(" Nombre o codigo del producto a eliminar: ").strip()
    producto = buscar_por_nombre_o_codigo(inventario, termino)

    if producto is None:
        print(f" No se encontro ningun producto con '{termino}'.")
        return

    print(f"\n Producto encontrado: {producto['nombre']} (ID: {producto['ID']})")

    confirmacion = (
        input(" ¿Estas seguro de que deseas eliminar permanentemente esto? (s/n): ")
        .strip()
        .lower()
    )

    if confirmacion == "s":
        inventario.remove(producto)
        guardar_inventario(inventario)
        print(" Producto eliminado correctamente.")
    else:
        print(" Operacion cancelada. No borramos nada.")


def mostrar_detalle_producto(producto):
    # ya sabes que hace xd
    print()
    print(f"   ID        : {producto['ID']}")
    print(f"   Nombre    : {producto['nombre']}")
    print(f"   Precio    : ${producto['precio']:.2f}")
    print(f"   Stock     : {producto['cantidad']} unidades")
    print(f"   Categoría : {producto['categoria']}")
    print()
