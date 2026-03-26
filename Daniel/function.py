import json
#menu
def menu():
    print('----------------------------------------------------')
    print('                Agenda de Contactos                | ')
    print('----------------------------------------------------')
    print('1. Ingresa 1 para Agregar Contacto')
    print('-------------------------')
    print('2. Ingresa 2 para Mostrar tus Contactatos')
    print('-----------------------------------------')
    print('3. Ingresa 3 para Buscar Contactatos')
    print('-----------------------------------------')
    print('4. Ingresa 4 para Filtro Busqueda por Grupo')
    print('-----------------------------------------')
    print('5. Ingresa 5 para Editar Contactos')
    print('-----------------------------------------')
    print('6. Ingresa 6 para Eliminar Contacto')
    print('-----------------------------------------')
    print('7. Ingresa 7 para Salir')
    print('-----------------------')

#cargar archivos
def cargar_contactos ():
    try:
        with open("contactos.json", "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

#guardar contactos
def guardar(contactos):
    with open('contactos.json', 'w') as archivo:
         json.dump(contactos, archivo, indent=4)

#registro de contactos
def registro():
    contactos = cargar_contactos()
    nombre = input('Ingrese el nombre: ').lower().strip()
    try:
        telefono = int(input('Ingrese Numero Telefonico: ').strip())
    except ValueError:
        print('Ingresa solo numeros')
        return

    while True:
     correo = input('Ingresa Correo : ').lower().strip()   
     if '@'in correo and '.' in correo:
         break
     else:
        print('Formato de correo no Valido')

    while True:    
        try:
            grupo = int(input('Asigna un Grupo: 1. Familia | 2. Amigos | 3. Trabajo: '))
        except ValueError:
            print('Error: Ingresa un Numero')   
            continue
        match grupo:
         case 1 :
            grupo = 'familia'
            break
         case 2:
            grupo = 'amigos'
            break
         case 3:
            grupo = 'trabajo'
            break
         case _:
            print('opcion fuera de rango')

    nuevo_contacto = {
        'nombre' : nombre,
        'telefono': telefono,
        'correo': correo,
        'grupo': grupo
    }
    contactos.append(nuevo_contacto)
    guardar(contactos)
    print('Contacto Guardado Exitosamente')

#mostrar contactos
def listar ():
    contactos = cargar_contactos()
    
    if not contactos:
        print('No hay contactos registrados')
        return
        
    contactos.sort(key=lambda c : c.get('nombre', ''))
    print('--lISTA DE CONTACTOS--')
    for c in contactos:
        print(f'Nombre : {c.get("nombre").title()}')
        print(f'Telefono : {c.get("telefono")}')
        print(f'Correo electronico : {c.get("correo")}')
        print(f'Grupo: {c.get("grupo")}')
        print('-----------------------------------------')
        
#buscar contactos  
def buscar():
    contactos = cargar_contactos()
    buscar_contacto = input('A quien deseas buscar?: ').strip().lower()
    encontrado= False
    for c in contactos:
      name = c.get('nombre').lower()
      if name.startswith(buscar_contacto):
         print(f'lista de Nombres : {c.get("nombre")} | {c.get("telefono")}  | {c.get("correo")}')
         encontrado= True
    if not encontrado:
        print('Este contacto no existe en tu agenda')


#cargar contactos 
#print grupos
#input
# list comprehencion nueva_lista = [elemento for elemento in tu_lista_original if condicion]
# itero
#muestro resultados 

#filtro grupos
def filtro_grupo():
    contacto= cargar_contactos()
    print('Grupos: Familia | Amigos | Trabajo')
    filtrar_contacto = input('Escribe el Grupo: ').strip().lower()
    filtro = [c for c in  contacto if filtrar_contacto == c.get('grupo') ]
    for c in filtro:
        print(f' {c.get("nombre")} | {c.get("telefono")}  | {c.get("correo")} | {c.get("grupo")}')

     
#editar contactos
 # cargar contonactos
 # input que contacto desea modifiicar
 #validar si esta el contacto
 #si el nombre esta. 
  # modificar numero
  #correo
  #guardar
 #sino 
   #no existe

def editar ():
    contactos = cargar_contactos()
    editar_contacto = input('Ingresa Nombre del Contacto que Desea Editar: ').strip().lower()
    encontrado= False
    for c in contactos:
      name = c.get('nombre').lower()
      if name == editar_contacto:
        nuevo_nombre = input('Nuevo Nombre: ').strip().lower()
        try:
            nuevo_telefono = int(input('Nuevo Numero de telefono: '))
        except  ValueError:
            print('Ingresa solo numeros')
            return
        while True:
            nuevo_correo = input('Nuevo Numero Correo: ')
            if '@' in nuevo_correo and '.' in nuevo_correo:
                break
            else:
                print('Formato de correo no Valido')
        c['nombre'] = nuevo_nombre
        c['telefono'] = nuevo_telefono
        c['correo'] = nuevo_correo
        encontrado= True
        print(f'El contacto: {nuevo_nombre} fue editado Correctamente ')
        guardar(contactos)
        return
    if not encontrado:
        print('Este contacto no existe en tu agenda')
  
#eliminar contactos
  # cargar contacto
  #input que contacto desea eliminar
  # recorrer
    # validacion de nombre
    # si esta 
     # preguntar para seguridad s/n
     # se elimina
     # guardar
     #salgo del for
    #si no
     # return menu
    #si no 
     #no existe

def eliminar():
    contactos = cargar_contactos()
    contacto_eliminar = input('Ingresa Nombre del Contacto a eliminar: ').strip().lower()
    encontrado= False
    for c in contactos:
      name = c.get('nombre').lower()
      if name == contacto_eliminar:
        seguridad= input(f'Estas seguro de eliminar a {name} | {c["telefono"]} | {c["correo"]} ?  S/N: ').strip().lower()
        if seguridad == 's':
         contactos.remove(c)
         encontrado = True
         print(f'{name} Borrado de tus contactos exitosamente')
         guardar(contactos)
         return
        else:
            return
        
    else:
        print('Nombre no encontrado')