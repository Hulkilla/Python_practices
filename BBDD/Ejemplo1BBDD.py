import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

############################# CREAR LA BASE DE DATOS #################

# una vez que la tabla está crearla, pero si ya está creada, no tiene sentido volver a crearla.
miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

############################# Insertar un sólo producto ##############

miCursor.execute("INSERT INTO PRODUCT VALUES ('BALON', 15, 'DEPORTES')")
miConexion.commit()

############################# Insertar varios productos ##############
    
variosProductos = [    
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")
    ]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos) 
# Cuando tenemos varios productos en values ponemos los "?" tantos como los necesarios en la tabla y tenemos que poner la lista
miConexion.commit()

############################# Leer la bases de datos #################


miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos2 = miCursor.fetchall() # Para ver la tabla de datos 


print(variosProductos2)

for producto in variosProductos2:
    print("Nombre de producto: ", producto[0], "Sección: ", producto[2])

 #Esto sirve para registrar un cambio en la tabla. Hay que hacerlo después de meter un dato nuevo


miConexion.close()

