import function

while True:
    function.menu()

    try:
        option = int(input('Ingresa una opcion: '))
    except ValueError:
        print('Debe ingresar un Numero')
        continue
        
    match option:
        case 1:
            function.registro()
        case 2:
            function.listar()
        case 3:
            function.buscar()
        case 4:
            function.editar()
        case 5:
            function.eliminar()
        case 6:
            print('Fin del programa')
            break
            