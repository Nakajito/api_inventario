from django.db import connection

# === USUARIOS ===
def insertar_usuario(username, password_hash):
    with connection.cursor() as cursor:
        cursor.callproc("insertar_usuario", [username, password_hash])