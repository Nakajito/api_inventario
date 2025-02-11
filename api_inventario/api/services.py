from django.db import connection

# === USUARIOS ===
def insertar_usuario(username, password_hash):
    with connection.cursor() as cursor:
        cursor.callproc("InsertarUsuario", [username, password_hash])
        
def actualizar_usuario(id_usuario, username, password_hash):
    with connection.cursor() as cursor:
        cursor.callproc("ActualizarUsuario", [id_usuario, username, password_hash])
        
def eliminar_usuario(id_usuario):
    with connection.cursor() as cursor:
        cursor.callproc("EliminarUsuario", [id_usuario])
        
def obtener_usuarios():
    with connection.cursor() as cursor:
        cursor.callproc("ObtenerUsuarios")
        return dictfetchall(cursor)
    

# === Categoria ===

def insertar_categoria(nombre):
    with connection.cursos() as cursor:
        cursor.callproc("InsertarCategoria", [nombre])
        
def actualizar_categoria(id_categoria, nombre):
    with connection.cursor() as cursor:
        cursor.callproc("ActualizarCategoria", [id_categoria, nombre])

def eliminar_categoria(id_categoria):
    with connection.cursor() as cursor:
        cursor.callproc("EliminarCategoria", [id_categoria])

def obtener_categorias():
    with connection.cursor() as cursor:
        cursor.callproc("ObtenerCategorias")
        return dictfetchall(cursor)
    

# === Producto ===
def insertar_producto(nombre, id_categoria, precio, cantidad):
    with connection.cursor() as cursor:
        cursor.callproc("InsertarProducto", [nombre, id_categoria, precio, cantidad])
        
def actualizar_producto(id_producto, nombre, id_categoria, precio, cantidad):
    with connection.cursor() as cursor:
        cursor.callproc("ActualizarProducto", [id_producto, nombre, id_categoria, precio, cantidad])
        
def eliminar_producto(id_producto):
    with connection.cursor() as cursor:
        cursor.callproc("EliminarProducto", [id_producto])
        
def obtener_productos():
    with connection.cursor() as cursor:
        cursor.callproc("ObtenerProductos")
        return dictfetchall(cursor)
    
# === Método para convertir los resultados en diccionarios ===
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]