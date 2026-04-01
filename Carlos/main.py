from libro_manager import cargar_libros, agregar_libro, listar_libros, buscar_libros, eliminar_libro, cambiar_estado_leido


def menu():
    print("\nGestor de coleccion de libros")
    print("1) Agregar libro")
    print("2) Listar todos los libros")
    print("3) Listar libros leidos")
    print("4) Listar libros no leidos")
    print("5) Buscar libro")
    print("6) Marcar leido/no leido")
    print("7) Eliminar libro")
    print("8) Salir")


def main():
    libros = cargar_libros()

    while True:
        menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            agregar_libro(libros)
        elif opcion == "2":
            listar_libros(libros)
        elif opcion == "3":
            listar_libros(libros, filtro=True)
        elif opcion == "4":
            listar_libros(libros, filtro=False)
        elif opcion == "5":
            buscar_libros(libros)
        elif opcion == "6":
            cambiar_estado_leido(libros)
        elif opcion == "7":
            eliminar_libro(libros)
        elif opcion == "8":
            print("Saliendo. Hasta luego!")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
