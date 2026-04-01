import json
import os

# ─────────────────────────────────────────────
#  CONFIGURACIÓN DE LA RUTA DE JSON
# ─────────────────────────────────────────────

ARCHIVO_VENTA = "data/venta.json"

# ─────────────────────────────────────────────
#  ARCHIVOS PARA GUARDAR Y CARGAR VENTAS
# ─────────────────────────────────────────────

def cargar_venta():
  if os.path.exists(ARCHIVO_VENTA):
    with open(ARCHIVO_VENTA, "r", encoding="utf-8") as archivo:
      return json.load(archivo)
  return []

def guardar_venta(venta):
  with open(ARCHIVO_VENTA, "w", encoding="utf-8") as archivo:
    json.dump(venta, archivo, indent=4, ensure_ascii=False)



# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL DE LA APP
# ─────────────────────────────────────────────

def mostrar_menu():
  print("\n╔══════════════════════════════════════╗")
  print("  ║          SISTEMA DE VENTAS           ║")
  print("  ╠══════════════════════════════════════╣")
  print("  ║  [1] Registrar una nueva venta       ║")
  print("  ║  [2] Listar el historial de ventas   ║")
  print("  ║  [3] Mostrar el total de ingresos    ║")
  print("  ║  [4] Buscar ventas por fecha         ║")
  print("  ║  [5] Buscar ventas entre fecha       ║")
  print("  ║  [6] Eliminar una venta              ║")
  print("  ║  [7] Salir                           ║")
  print("  ╚══════════════════════════════════════╝")

# ─────────────────────────────────────────────
#  APP 
# ─────────────────────────────────────────────

def app():
  venta = cargar_venta()   # ← Cargar lista de ventas

  while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
      registrar_venta(venta)
    elif opcion == "2":
      listar_venta(venta)
    elif opcion == "3":
      ingresos_venta(venta)
    elif opcion == "4":
      buscar_venta(venta)
    elif opcion == "5":
      buscar_venta_entre_fecha(venta)
    elif opcion == "6":
      eliminar_venta(venta)
    elif opcion == "7":
      print("\n Hasta una nueva venta.")
      break
    else:
      print(" Opción no válida.")



# ─────────────────────────────────────────────
#  1. REGISTRAR VENTA
# ─────────────────────────────────────────────

def registrar_venta(venta):
  print("\n── REGISTRAR UNA NUEVA VENTA ──────────────────")
  fecha = input("Fecha (YYYY-MM-DD): ").strip()
  #validar fecha
  if not fecha:
    print("Error. La fecha no puede estar vacía.")
    return 
  if not fecha.count("-") == 2:
    print("Error. La fecha debe tener el formato YYYY-MM-DD.")
    return
  if not all(part.isdigit() for part in fecha.split("-")):
    print("Error. La fecha debe contener solo números y guiones.")
    return
  codigo_venta = input("Código de la venta: ").strip()
  #validar codigo de venta
  if codigo_venta in [v["codigo_venta"] for v in venta]:
    print("Error. El código de la venta ya existe.")
    return
  codigo = input("Código del Producto: ").strip()
  producto = input("Producto: ").strip()
  try:
    cantidad = int(input("Cantidad: ").strip())
    precio = float(input("Precio unitario: ").strip())
  except ValueError:
    print("Error. La cantidad y/o precio deben ser numéricos.")
    return
  total = cantidad * precio
  
  nueva_venta = {
    "fecha": fecha,
    "codigo": codigo,
    "codigo_venta": codigo_venta,
    "producto": producto, 
    "cantidad": cantidad,
    "precio": precio,
    "total": total
  }

  venta.append(nueva_venta)
  guardar_venta(venta)

  print(f" Venta cob el codigo de venta:'{codigo_venta}' registrada exitosamente.")


# ─────────────────────────────────────────────
#  2. LISTAR VENTAS
# ─────────────────────────────────────────────

def listar_venta(venta):
  print("\n── HISTORIAL DE VENTAS ───────────────────────")

  if not venta:
    print("No hay ventas registradas.")
    return

  for v in venta:
    print(f"Fecha: {v['fecha']} - Código de la venta: {v['codigo_venta']} - Código del Producto: {v['codigo']} - Descripcion de Producto: {v['producto']} - Cantidad: {v['cantidad']} - Total de Venta: ${v['total']}")


# ─────────────────────────────────────────────
#  3. TOTAL DE INGRESOS
# ─────────────────────────────────────────────

def ingresos_venta(venta):
  total = sum(v["total"] for v in venta)
  print(f"\n Total de ingresos por ventas: ${total}")

# ─────────────────────────────────────────────
#  4. BUSCAR VENTAS POR FECHA
# ─────────────────────────────────────────────

def buscar_venta(venta):
  print("\n── BUSCAR VENTAS POR FECHA ────────────────────")
  fecha_busqueda = input("Ingresa la fecha (YYYY-MM-DD): ").strip()
  #validar fecha
  if not fecha_busqueda:
    print("Error. La fecha no puede estar vacía.")
    return  
  if not fecha_busqueda.count("-") == 2:
    print("Error. La fecha debe tener el formato YYYY-MM-DD.")
    return
  if not all(part.isdigit() for part in fecha_busqueda.split("-")):
    print("Error. La fecha debe contener solo números y guiones.")
    return
  resultados = [v for v in venta if v.get("fecha") == fecha_busqueda]
  if not resultados:
    print("No hay ventas registradas en esa fecha.")
    return
  print(f"\nVentas del {fecha_busqueda}:")
  for v in resultados:
    print(f"Código de la venta: {v['codigo_venta']} - Código del Producto: {v['codigo']} - Descripcion de Producto: {v['producto']} - Cantidad: {v['cantidad']} - Total de Venta: ${v['total']}")

# ─────────────────────────────────────────────
#  5. BUSCAR VENTAS POR FECHA ENTRE FECHAS
# ─────────────────────────────────────────────
def buscar_venta_entre_fecha(venta):
    print("\n── BUSCAR VENTAS ENTRE FECHAS ────────────────────")
    fecha_inicio = input("Ingresa la fecha de inicio (YYYY-MM-DD): ").strip()
    #validar fecha inicio
    if not fecha_inicio:
      print("Error. La fecha de inicio no puede estar vacía.")
      return  
    if not fecha_inicio.count("-") == 2:
      print("Error. La fecha de inicio debe tener el formato YYYY-MM-DD.")
      return
    if not all(part.isdigit() for part in fecha_inicio.split("-")):
      print("Error. La fecha de inicio debe contener solo números y guiones.")
      return
    #validar fecha fin
    fecha_fin = input("Ingresa la fecha de fin (YYYY-MM-DD): ").strip()
    if not fecha_fin:
      print("Error. La fecha de fin no puede estar vacía.")
      return 
    if not fecha_fin.count("-") == 2:
      print("Error. La fecha de fin debe tener el formato YYYY-MM-DD.")
      return    
    if not all(part.isdigit() for part in fecha_fin.split("-")):
      print("Error. La fecha de fin debe contener solo números y guiones.")
      return
    resultados = [v for v in venta if fecha_inicio <= v.get("fecha", "") <= fecha_fin]
    if not resultados:
        print("No hay ventas registradas en ese rango de fechas.")
        return
    print(f"\nVentas entre {fecha_inicio} y {fecha_fin}:")
    for v in resultados:
        print(f"Fecha de venta: {v['fecha']} - Código de la venta: {v['codigo_venta']} - Código del Producto: {v['codigo']} - Descripción: {v['producto']} - Cantidad: {v['cantidad']} - Total: ${v['total']}")



# ─────────────────────────────────────────────
#  6. ELIMINAR VENTA
# ─────────────────────────────────────────────

def eliminar_venta(venta):
  codigo_venta = input("Código de la venta a eliminar: ").strip()
  for v in venta:
    if v["codigo_venta"] == codigo_venta:
      venta.remove(v)
      guardar_venta(venta)
      print(f"La venta con el código: '{v['codigo_venta']}' eliminada correctamente.")
      return
  print("No se encontró una venta con ese código.")

