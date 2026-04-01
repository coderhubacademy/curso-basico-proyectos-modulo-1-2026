from libro_manager import cargar_libros, agregar_libro, listar_libros, buscar_libros, eliminar_libro, cambiar_estado_leido


def menu():
    print("\nGestor de colección de libros")
    print("1) Agregar libro")
    print("2) Listar todos los libros")
    print("3) Listar libros leídos")
    print("4) Listar libros no leídos")
    print("5) Buscar libro")
    print("6) Marcar leído/no leído")
    print("7) Eliminar libro")
    print("8) Salir")


def main():
    libros = cargar_libros()

    while True:
        menu()
        opcion = input("Selecciona una opción: ").strip()

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
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
