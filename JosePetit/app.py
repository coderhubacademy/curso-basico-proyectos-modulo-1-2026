import function as rs
import time


mis_reservas = rs.cargar_datos()

def mostrar_menu():
    print("\n Bookit :APP RESERVAS")
    print()
    print("1. Registrar")
    print()
    print("2. Listar")
    print()
    print("3. Buscar")
    print()
    print("4. Modificar")
    print()
    print("5. Eliminar")
    print()
    print("6. Salir")

while True: 
    mostrar_menu()
    option = int(input("\nSeleccione opción: "))

    if option == 1:
        print("Cargando...")
        time.sleep(5)
        rs.registrar_reserva(mis_reservas)
    elif option == 2:
        print("Cargando lista...")
        time.sleep(5)
        rs.listar_reserva(mis_reservas)
    elif option == 3:
        print("Espere...")
        time.sleep(5)
        rs.buscar_reserva(mis_reservas)
    elif option == 4:
         print("Cargando Lista...")
         time.sleep(5)
         rs.modificar_reserva(mis_reservas)
    elif option == 5:
         print("CCargando Lista...")
         time.sleep(5)
         rs.eliminar_reserva(mis_reservas)
         print()
         print("Felicidades logró eliminar su reserva")
    elif option == 6:
        break
    else:
        print("Opción no válida (ponga num del 1 al 6)")

if __name__ == "__main__":
    mostrar_menu()