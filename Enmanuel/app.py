from funciones import (
    cargar_inventario,
    registrar_producto,
    listar_productos,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
)


def mostrar_menu():
    print(" [1]  Registrar producto                 ")
    print(" [2]  Listar productos                   ")
    print(" [3]  Buscar producto                    ")
    print(" [4]  Actualizar producto                ")
    print(" [5]  Eliminar producto                  ")
    print(" [6]  Salir                              ")


def main():
    print("Bienvenido al Sistema de Inventario ")
    print("Cargando datos...")

    inventario = cargar_inventario()
    print(f"{len(inventario)} producto(s) cargado(s) desde inventario.json")

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-6): ").strip()

        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            print("\n Hasta pronto Los datos han sido guardados.")
            break
        else:
            print("Opcion no valida. Por favor elige un numero del 1 al 6.")


if __name__ == "__main__":
    main()
