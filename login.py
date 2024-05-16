import mysql.connector

# Configuración de la conexión a la base de datos
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'proyecto1.0'
}

def verificar_credenciales(usuario, contraseña):
    # Conectar a la base de datos
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        # Consultar la base de datos para verificar el usuario y contraseña
        query = "SELECT * FROM usuario WHERE usuario = %s AND contraseña = %s"
        valores = (usuario, contraseña)
        cursor.execute(query, valores)
        resultado = cursor.fetchone()

        if resultado:
            # Credenciales válidas
            return True
        else:
            # Credenciales inválidas
            return False

    except mysql.connector.Error as error:
        print("Error en la conexión a la base de datos:", error)
        return False

    finally:
        # Cerrar la conexión a la base de datos
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Ejemplo de uso
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

if verificar_credenciales(usuario, contraseña):
    print("Inicio de sesión exitoso")
else:
    print("Usuario o contraseña incorrectos")