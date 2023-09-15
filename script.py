import hashlib

# tabla de usuarios (diccionario)
tabla_usuarios = {}

def encriptar_pswd(pswd):
#Encripta la contraseña usando SHA-256 utilizando la libreria hashlib
    sha256 = hashlib.sha256()
    #Toma la contraseña y la encripta
    sha256.update(pswd.encode('utf-8'))
    #Nos retorna la contraseña encriptada
    return sha256.hexdigest()

def registrar_usuario():
    #Registra un usuario y su contraseña encriptada en la tabla de usuarios.
    usuario = input("Ingrese un nuevo nombre de usuario: ")
    pswd = input("Ingrese una nueva contraseñ: ")
    pswd_encriptada = encriptar_pswd(pswd)
    tabla_usuarios[usuario] = {
        'pswd': pswd,
        'sha256_pswd': pswd_encriptada
    }
    print("Usuario registrado con éxito!")

def mostrar_tabla_usuarios():
    #Muestra el contenido de la tabla de usuarios con formato para tener mejor visibilidad
    #de los datos
    print("Contenido de la tabla de usuarios:")
    print("{:<15} {:<20} {:<50}".format("Usuario", "Contraseña", "SHA-256 Contraseña"))
    for usuario, info in tabla_usuarios.items():
        print("{:<15} {:<20} {:<50}".format(usuario, info['pswd'], info['sha256_pswd']))

def verificar_credenciales():
    #Verifica las credenciales al intentar iniciar sesión.
    usuario = input("Ingrese el nombre de usuario: ")
    pswd = input("Ingrese la contraseña: ")
    if usuario in tabla_usuarios:
        pswd_encriptada = encriptar_pswd(pswd)
        if tabla_usuarios[usuario]['sha256_pswd'] == pswd_encriptada:
            print("Inicio de sesión exitoso para el usuario:", usuario)
        else:
            print("Credenciales incorrectas para el usuario:", usuario)
    else:
        print("Usuario no encontrado.")

if __name__ == "__main__":
    while True:
        print("1. Registrar un nuevo usuario")
        print("2. Verificar credenciales")
        print("3. Mostrar tabla de usuarios")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            verificar_credenciales()
        elif opcion == '3':
            mostrar_tabla_usuarios()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
