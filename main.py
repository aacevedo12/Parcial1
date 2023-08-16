import sqlite3

# Conecta a la base de datos
conn = sqlite3.connect('inventario.db')
c = conn.cursor()

# Crea la tabla si aún no existe
c.execute('''CREATE TABLE IF NOT EXISTS inventario
             (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, cantidad INTEGER)''')

# Funciones para interactuar con la base de datos
def agregar_articulo(nombre, descripcion, cantidad):
    c.execute("INSERT INTO inventario (nombre, descripcion, cantidad) VALUES (?, ?, ?)", (nombre, descripcion, cantidad))
    conn.commit()
    print(f"Se ha agregado el artículo '{nombre}' al inventario.")

def buscar_articulo(nombre):
    c.execute("SELECT * FROM inventario WHERE nombre=?", (nombre,))
    resultado = c.fetchone()
    if resultado:
        print(f"Nombre: {resultado[1]}\nDescripción: {resultado[2]}\nCantidad: {resultado[3]}")
    else:
        print(f"No se encontró el artículo '{nombre}' en el inventario.")

def editar_articulo(nombre, nueva_cantidad):
    c.execute("UPDATE inventario SET cantidad=? WHERE nombre=?", (nueva_cantidad, nombre))
    conn.commit()
    print(f"Se ha actualizado la cantidad del artículo '{nombre}' a {nueva_cantidad}.")

def eliminar_articulo(nombre):
    c.execute("DELETE FROM inventario WHERE nombre=?", (nombre,))
    conn.commit()
    print(f"Se ha eliminado el artículo '{nombre}' del inventario.")

# Menú principal de la aplicación
while True:
    print("\n1. Agregar artículo\n2. Buscar artículo\n3. Editar cantidad de artículo\n4. Eliminar artículo\n5. Salir")
    opcion = input("Ingrese una opción (1-5): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del artículo: ")
        descripcion = input("Ingrese la descripción del artículo: ")
        cantidad = int(input("Ingrese la cantidad del artículo: "))
        agregar_articulo(nombre, descripcion, cantidad)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del artículo: ")
        buscar_articulo(nombre)

    elif opcion == "3":
        nombre = input("Ingrese el nombre del artículo: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad del artículo: "))
        editar_articulo(nombre, nueva_cantidad)

    elif opcion == "4":
        nombre = input("Ingrese el nombre del artículo: ")
        eliminar_articulo(nombre)

    elif opcion == "5":
        break

    else:
        print("Opción no válida. Intente de nuevo.")

