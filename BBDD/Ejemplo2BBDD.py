import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#### CREAR TABLA ################
miCursor.execute("""
                 CREATE TABLE PRODUCTOS (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
                     PRECIO INTEGER, 
                     SECCION VARCHAR(20))
                 """)

#### INTRODUCCION DE DATOS ################
variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería"),
    ("Pelota", 15, "Juguetería")
]


miCursor.executemany(
    "INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", variosProductos)
miConexion.commit()


miCursor.execute(
    "INSERT INTO PRODUCTOS VALUES (NULL, 'Martillo', 10, 'Bricolaje')")
miConexion.commit()


#### LLAMADA A LA TABLA ################
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos2 = miCursor.fetchall()  # Para ver la tabla de datos

print(variosProductos2)

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION ='Deportes'")

productoDeportes = miCursor.fetchall()

print(productoDeportes)


#### ACTUALIZAR DATOS DE LA TABLA ################

miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'Pelota'")

#### BORRAR UN DATO DE LA TABLA ##################

miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO = 'Martillo'")

miConexion.close()
