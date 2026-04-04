import json
import os

DATA_FILE = 'data/datos.json'

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def guardar_datos(inventario):
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    with open(DATA_FILE, 'w') as f:
        json.dump(inventario, f, indent=4)

def registrar_producto(inventario, nombre, cantidad, precio):
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    print(f"Producto '{nombre}' registrado.")

def listar_inventario(inventario):
    print("\nInventario actual:")
    if inventario:
        for nombre, datos in inventario.items():
            print(f"{nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")
    else:
        print("El inventario está vacio.")

def buscar_producto(inventario, nombre):
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"{nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")
    else:
        print("Producto no encontrado.")

def actualizar_producto(inventario, nombre, cantidad, precio):
    if nombre in inventario:
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print(f"Producto '{nombre}' actualizado.")
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado.")
    else:
        print("Producto no encontrado.")