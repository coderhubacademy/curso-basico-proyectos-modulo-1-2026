import json
import os

#Con esto permitira tener la ruta donde se guarda el programa en la carpeta principal, es decir mi carpeta del proyecto "Andres"
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

#Se crea una ruta para guardar la carpeta datos dentro de la carpeta principal "Andres"
CARPETA_DATOS = os.path.join(DIRECTORIO_ACTUAL, 'datos')

#Se crea una ruta para que se guarde el archivo json dentro de la carpeta datos
DATOS_DE_ESTUDIANTES = os.path.join(CARPETA_DATOS, 'datos.json')

#Si existe carpeta la carpeta datos, se creara una para almacenar la informacion.
def asegurar_carpeta_existe():
    if not os.path.exists(CARPETA_DATOS):
        os.makedirs(CARPETA_DATOS)
        print(f"Carpeta '{CARPETA_DATOS}' creada.")
        
 #Se cargara los datos del archivo JSON si existe, de lo contrario devuelve un diccionario vacío.
def cargar_datos():
    if os.path.exists(DATOS_DE_ESTUDIANTES):
        with open(DATOS_DE_ESTUDIANTES, 'r', encoding='utf-8') as informacion:
            return json.load(informacion)
    return []

#Guarda el diccionario de datos en un archivo JSON.
def guardar_datos(datos):
    asegurar_carpeta_existe()
    with open(DATOS_DE_ESTUDIANTES, 'w', encoding='utf-8') as informacion:
        json.dump(datos, informacion, indent=4)
        
#Se calcula el promedio de las notas de los estudiantes.
def calcular_promedio(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

#RegistrO de los estudiantes
def registrar_estudiante(datos):
    nombre = input("Por favor ingresa el nombre del estudiante: ").strip()
    for estudiante in datos:
     if estudiante ['nombre'] == nombre:
        print("Este estudiante ya fue registrado anteriormente. Por favor eliga otra opcion.")
        return

    entrada_notas = input("Por favor ingresa las calificaciones y que esten separadas por espacios (ej. 15 18): ")
    try:
        notas = [float(n) for n in entrada_notas.split()]
        promedio = calcular_promedio(notas)
     
        nuevo_registro = {
            'nombre': nombre,
            'notas': notas,
            'promedio': promedio
        }
        datos.append(nuevo_registro)
        guardar_datos(datos)
        
        print(f"El estudiante '{nombre}' fue registrado con éxito.")
    except ValueError:
        print("Error en el formato de notas.")
           
#Lista de estudiantes registrados           
def listar_estudiantes(datos):
    if not datos:
        print("No hay estudiantes registrados.")
        return

    print("\n/// Lista de Estudiantes ///")
    for estudiante in datos:
        nombre = estudiante['nombre']
        notas = estudiante['notas']
        
        # Muestra el promedio del estudiante
        promedio = estudiante['promedio'] 
        notas_str = ", ".join(map(str, notas))
        print(f"Nombre: {nombre} | Notas: [{notas_str}] | Promedio: {promedio:.2f}")
    print("/-----------------------------------------------------------------------/")

#editar notas de estudiantes registrados
def editar_notas(datos):
    
    #Se muestra la lista para que el usuario pueda visualizar a quien modificar
    print("\n/// Lista de Estudiantes para editar ///")
    for estudiante in datos:
        nombre = estudiante['nombre']
        notas = estudiante['notas']
        
        # Muestra el promedio del estudiante
        promedio = estudiante['promedio'] 
        notas_str = ", ".join(map(str, notas))
        print(f"Nombre: {nombre} | Notas: [{notas_str}] | Promedio: {promedio:.2f}")
    print("/-----------------------------------------------------------------------/")
    
    nombre = input("Por favor ingrese el nombre del estudiante que desea editar sus notas: ").strip()
    
    estudiante_encontrado = None
    for estudiante in datos:
        if estudiante['nombre'] == nombre:
            estudiante_encontrado = estudiante
            break

    if not estudiante_encontrado:
        print("Este estudiante no existe, por favor revise que este bien escrito.")
        return

    entrada = input(f"Notas actuales {estudiante_encontrado['notas']}. Nuevas notas: ")
    try:
        nuevas_notas = [float(n) for n in entrada.split()]
        
        # Actualizamos las notas
        estudiante_encontrado['notas'] = nuevas_notas
        # Debemos recalcular el promedio y actualizarlo también
        estudiante_encontrado['promedio'] = calcular_promedio(nuevas_notas)
        
        guardar_datos(datos)
        print(f"La nota del estudiante '{nombre}'a sido actualizada.")
    except ValueError:
        print("Error en las notas.")

#Eliminar registro de estudiante
def eliminar_estudiante(datos):
    
    print("\n/// Lista de Estudiantes que desea borrar///")
    for estudiante in datos:
        nombre = estudiante['nombre']
        notas = estudiante['notas']
        
        # Leemos el promedio directamente de los datos guardados
        promedio = estudiante['promedio'] 
        notas_str = ", ".join(map(str, notas))
        print(f"Nombre: {nombre} | Notas: [{notas_str}] | Promedio: {promedio:.2f}")
    print("/-----------------------------------------------------------------------/")
    
    nombre = input("Por favor ingresa el nombre del estudiante: ").strip()
    
    #Con enumerate me permite saber la ubicacion del estudiante en el registro con el fin que pueda ser borrado
    for indice, estudiante in enumerate(datos):
     if estudiante['nombre'] == nombre:
        del datos[indice]
        guardar_datos(datos)
        print(f"Estudiante '{nombre}' fue borrado correctamente.")
        return
    
    print("El estudiante no existe, por favor revise que este bien escrito.")
        
