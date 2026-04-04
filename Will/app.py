import json
from funciones import (
    registrar_producto, listar_inventario, buscar_producto,
    actualizar_producto, eliminar_producto, cargar_datos, guardar_datos
)

def main():
    
    inventario = cargar_datos()

    while True:
        print("\nSistema de Inventario")
        print("1. Registrar producto")
        print("2. Listar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Guardar cambios")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            registrar_producto(inventario, nombre, cantidad, precio)

        elif opcion == '2':
            listar_inventario(inventario)

        elif opcion == '3':
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(inventario, nombre)

        elif opcion == '4':
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            actualizar_producto(inventario, nombre, cantidad, precio)

        elif opcion == '5':
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == '6':
            guardar_datos(inventario)
            print("Cambios guardados.")

        elif opcion == '7':
            guardar_datos(inventario)
            print("Saliendo del programa.")
            break

        else:
            print("Opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    main()