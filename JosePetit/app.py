import function as rs

def app_restaurante():
    print("Restaurant App")
    print()
    print("1. Registrar Reserva")
    print()
    print("2. Listar Reservas")
    print()
    print("3. Buscar Reservas")
    print()
    print("4. Modificar Reserva (fecha y/o hora)")
    print()
    print("5. Eliminar Reservas")
    print()
    print("6. Salir")
    print()

while True: 

    app_restaurante()
    option = int(input("Seleccione una opción"))

    if option == 1:
        rs.registrar_reserva()
    elif option == 2:
        rs.listar_reserva()
    elif option == 3:
        rs.buscar_reserva()
    elif option == 4:
        rs.modificar_reserva()
    elif option == 5:
        rs.eliminar_reserva()
    elif option == 6:
        print("Perfecto, le deseo un buen día")
        break
    else:
        print("elija una de las 6 opciones, no se haga wei :p")

