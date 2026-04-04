
import funciones

def app():
    venta = funciones.cargar_venta()  # ← Cargar lista de ventas

    while True:
        funciones.mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
          funciones.registrar_venta(venta)
        elif opcion == "2":
          funciones.listar_venta(venta)
        elif opcion == "3":
          funciones.ingresos_venta(venta)
        elif opcion == "4":
          funciones.buscar_venta(venta)
        elif opcion == "5":
          funciones.buscar_venta_entre_fecha(venta)
        elif opcion == "6":
          funciones.eliminar_venta(venta)
        elif opcion == "7":
          print("\n Hasta una nueva venta.")
          break
        else:
          print(" Opción no válida.")
if __name__ == "__main__":
    app()
