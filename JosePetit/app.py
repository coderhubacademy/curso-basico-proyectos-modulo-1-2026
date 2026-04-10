import function as rs
import time

mis_reservas = rs.cargar_datos()
user_rg = rs.cargar_usuarios() 
usuario_activo = None

def user_menu():
    global user_rg 
    print(" BIENVENIDO A BOOKIT ")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    
    opcion = input("Seleccione opcion: ")

    if opcion == "2":
        print("Cargando opciones...")
        time.sleep(3)
        u = input("Crea tu usuario: ")
        p = input("Crea tu clave: ")
        user_rg[u] = p
        rs.guardar_usuarios(user_rg)
        print("Espere...")
        time.sleep(4)
        print()
        print("MISIÓN CUMPLIDA: Usuario guardado con éxito (hurray xd)")
    elif opcion == "1":
        print("LOG-IN(necesario?)")
    
        user = input("Usuario: ")
        pas = input("Clave: ")

        if user in user_rg and user_rg[user] == pas and user != "":
          print(f"Bienvenido {user}, en un momento le asignamos")
          return user
        else:
          print("Eso que, ¿sé come?.")

def mostrar_menu():
    print("Cargando menu...")
    time.sleep(3)
    print(" Bookit : APP RESERVAS")
    print("1. Registrar") 
    print("2. Listar")
    print("3. Buscar")
    print("4. Modificar")
    print("5. Eliminar") 
    print("6. Salir")

          

if __name__ == "__main__":
    user_menu()
    while True: 
            print()
            mostrar_menu()
            option = int(input("\n¿Que opcion desea elegir?: "))
            time.sleep(3)

            if option == 1:
                print("Cargando...")
                time.sleep(3)
                rs.registrar_reserva(mis_reservas)
            elif option == 2:
                print("Cargando lista...")
                time.sleep(2)
                rs.listar_reserva(mis_reservas)
            elif option == 3:
                print("Espere...")
                time.sleep(2)
                rs.buscar_reserva(mis_reservas)
            elif option == 4:
                print("Cargando Lista...")
                time.sleep(2)
                rs.modificar_reserva(mis_reservas)
            elif option == 5:
                print("Cargando Lista...")
                time.sleep(2)
                rs.eliminar_reserva(mis_reservas)
                print("\nFelicidades logró eliminar su reserva")
            elif option == 6:
                print("Saliendo del sistema...")
                time.sleep(2)
                break
            else:
                print("Opción no válida (ponga num del 1 al 6)")

