from funciones import (
    cargar_datos,
    registrar_estudiante,
    listar_estudiantes,
    editar_notas,
    eliminar_estudiante,
    
)

#Menu del sistema
def mostrar_menu():
    print("\n=== SISTEMA DE NOTAS Y PROMEDIO ESTUDIANTIL ===")
    print(" ")
    print("1. Registrar estudiante y calificaciones")
    print("2. Listar estudiantes y promedios")
    print("3. Editar notas de un estudiante")
    print("4. Eliminar registro de un estudiante")
    print("5. Salir")
    print(" ")
    return input("Por favor selecciona una de las opciones (1-5): ")

def main():
    datos = cargar_datos()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            registrar_estudiante(datos)
        elif opcion == '2':
            listar_estudiantes(datos)
        elif opcion == '3':
            editar_notas(datos)
        elif opcion == '4':
            eliminar_estudiante(datos)
        elif opcion == '5':
            print("Cerrando sistema de notas y promedio estudiantil, hasta la proxima")
            break
        else:
            print("Esta opción es invalida. Por favor, ingrese un numero dentro de la opciones (1-5).")

if __name__ == "__main__":
    main()