import os

# Definir rutas
carpeta_padre = "usrs"




#Crea un directorio para el usuario donde se almacena su archivo env
#logs de boton y de inicios de sesion...
def regisForm():
    nomUser = input('nomUsuario: ')
    carpeta_hija = os.path.join(carpeta_padre, nomUser)
    archivo = os.path.join(carpeta_hija, "envUser.venv")  # Puedes cambiar la extensión

    # Crear carpetas si no existen
    os.makedirs(carpeta_hija, exist_ok=True)
    secrets = 'SECRET_SALT=' + '123456789'

    # Crear archivo dentro de la carpeta hija
    with open(archivo, "w") as f:
        f.write(secrets)

regisForm()