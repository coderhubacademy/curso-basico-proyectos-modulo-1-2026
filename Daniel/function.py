import json
#menu
def menu():
    print('----------------------------------------------------')
    print('                Agenda de Contactos                | ')
    print('----------------------------------------------------')
    print('1. Ingresa 1 para agregar')
    print('-------------------------')
    print('2. Ingresa 2 para mostrar tus contactatos')
    print('-----------------------------------------')
    print('3. Ingresa 3 para Buscar contactatos')
    print('-----------------------------------------')
    print('4. Ingresa 4 para salir')
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
        print('Ingrese solo numeros')
        return
    while True:
     correo = input('Ingresa Correo : ').lower().strip()   
     if '@'in correo and '.' in correo:
         break
     else:
        print('Formato de correo no Valido')
    
    nuevo_contacto = {
        'nombre' : nombre,
        'telefono': telefono,
        'correo': correo
    }
    contactos.append(nuevo_contacto)
    guardar(contactos)
    print('Contacto Guardado Exitosamente')

#mostrar contactos
def listar ():
    contactos = cargar_contactos()
    
    if not contactos:
        print('No ha contactos registrados')
        return
    contactos.sort(key=lambda c : c.get('nombre', ''))
    print('--lISTA DE CONTACTOS--')
    for c in contactos:
        print(f'Nombre : {c.get("nombre").title()}')
        print(f'Telefono : {c.get("telefono")}')
        print(f'Correo electronico : {c.get("correo")}')
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
       

                
