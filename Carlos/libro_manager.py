import json
from pathlib import Path

DATA_FOLDER = Path("datos_libros")
DB_PATH = DATA_FOLDER / "libros.json"


def asegurar_carpeta():
    DATA_FOLDER.mkdir(parents=True, exist_ok=True)


def cargar_libros():
    asegurar_carpeta()
    if not DB_PATH.exists():
        return []
    try:
        with DB_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Advertencia: no se pudo leer el archivo de datos. Se iniciara una coleccion vacia.")
        return []


def guardar_libros(libros):
    asegurar_carpeta()
    try:
        with DB_PATH.open("w", encoding="utf-8") as f:
            json.dump(libros, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Error guardando los datos: {e}")


def siguiente_id(libros):
    if not libros:
        return 1
    return max(book["id"] for book in libros) + 1


def agregar_libro(libros):
    titulo = input("Titulo: ").strip()
    if not titulo:
        print("El titulo no puede estar vacio.")
        return

    autor = input("Autor: ").strip()
    anio = input("Anio de publicacion (opcional): ").strip()
    leido = input("¿Leiste el libro? (s/n): ").strip().lower() == "s"

    libro = {
        "id": siguiente_id(libros),
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "leido": leido,
    }
    libros.append(libro)
    guardar_libros(libros)
    print(f"Libro agregado (ID {libro['id']}): {titulo} - {autor}")


def listar_libros(libros, filtro=None):
    if not libros:
        print("No hay libros en la coleccion.")
        return

    filtrado = libros
    if filtro is not None:
        filtrado = [libro for libro in libros if libro["leido"] == filtro]

    if not filtrado:
        print("No se encontraron libros con el criterio seleccionado.")
        return

    headers = ["ID", "Titulo", "Autor", "Anio", "Leido"]
    rows = []
    for libro in filtrado:
        leido = "Si" if libro["leido"] else "No"
        rows.append([
            str(libro.get("id", "")),
            str(libro.get("titulo", "")),
            str(libro.get("autor", "")),
            str(libro.get("anio", "")),
            leido,
        ])

    col_widths = [
        max(len(headers[i]), *(len(row[i]) for row in rows))
        for i in range(len(headers))
    ]

    border = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    header_row = "| " + " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))) + " |"

    print(border)
    print(header_row)
    print(border)

    for row in rows:
        line = "| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(len(row))) + " |"
        print(line)

    print(border)


def buscar_libros(libros):
    criterio = input("Buscar por titulo o autor: ").strip().lower()
    if not criterio:
        print("Debe ingresar texto para buscar.")
        return

    resultados = [libro for libro in libros if criterio in libro["titulo"].lower() or criterio in libro["autor"].lower()]
    if not resultados:
        print("No se encontraron libros que coincidan con la busqueda.")
        return

    listar_libros(resultados)


def eliminar_libro(libros):
    id_str = input("ID del libro a eliminar: ").strip()
    if not id_str.isdigit():
        print("ID invalido.")
        return

    id_libro = int(id_str)
    antes = len(libros)
    libros[:] = [libro for libro in libros if libro["id"] != id_libro]
    if len(libros) == antes:
        print(f"No se encontro el libro con ID {id_libro}.")
    else:
        guardar_libros(libros)
        print(f"Libro ID {id_libro} eliminado.")


def cambiar_estado_leido(libros):
    id_str = input("ID del libro: ").strip()
    if not id_str.isdigit():
        print("ID invalido.")
        return

    id_libro = int(id_str)
    for libro in libros:
        if libro["id"] == id_libro:
            libro["leido"] = not libro["leido"]
            guardar_libros(libros)
            estado = "leido" if libro["leido"] else "no leido"
            print(f"Libro ID {id_libro} ahora esta marcado como {estado}.")
            return

    print(f"No se encontro el libro con ID {id_libro}.")
