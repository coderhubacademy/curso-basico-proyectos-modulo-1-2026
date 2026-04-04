import funciones 

#menu de opciones :)
def mostrar_menu():
    print("\n--- MENU DE EVENTOS ---")
    print("-"*30)
    print("1. Registrar evento") #primera opcion muy improtante
    print("-"*30)
    print("2. Listar eventos") #segunda opcion mas improtante
    print("-"*30)
    print("3. Buscar eventos") #opcional!
    print("-"*30)
    print("4. Eliminar eventos") #tercera mas importante
    print("-"*30)
    print("5. Salir") #terminar bulce y salri del programa
    print("-"*30)

def ejecutar_programa():
    # Cargamos los datos una sola vez al inicio
    lista_eventos = funciones.cargar_datos()

    while True: 
        mostrar_menu()
        try:
            option = int(input("ingrese una opcion del menu(1-5):  "))
            match option:
                case 1:
                    # USAMOS SIEMPRE 'lista_eventos' con A
                    lista_eventos = funciones.registrar_evento(lista_eventos)
                case 2:
                    # Aquí llamamos a la función correctamente
                    funciones.listar_eventos(lista_eventos)
                case 3:
                    lista_eventos = funciones.buscar_eventos(lista_eventos)
                case 4:
                    lista_eventos = funciones.eliminar_eventos(lista_eventos)
                case 5:
                    funciones.guardar_datos(lista_eventos)
                    print("Gracias por usar el programa")
                    input("Presione enter para salir")
                    break 
                case _:
                    print("Opción no válida (por favor ingresa un número del 1 al 5)")
        except ValueError:
            print("Error, por favor intente ingresar una de las opciones numeradas")

if __name__ == "__main__":
    ejecutar_programa()