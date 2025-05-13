import os
import bcrypt

# Definir ruta Padre
#donde se almacena su archivo env
#logs de boton y de inicios de sesion...
PATH_DIR = os.path.join(os.path.dirname(__file__), "usrs")

class Harpo:

    def __init__(self, nomUsuario, passUser):
        self.nomUsuario = nomUsuario
        self.passUser = passUser

    #make directorys of each user in who sign in in the app
    def mkdiruser(self):
        diruserPath = os.path.join(self.PATH_DIR, self.nomUsuario)
        nameFile = "venv.env"
        filePath = os.path.join(diruserPath, nameFile)
        try:
            os.makedirs(diruserPath, exist_ok=True)
            
            with open(filePath, "w") as f: 
                f.write("USER = " + self.nomUsuario + "\n")
            print("lol")
        except Exception as e:
            print('lolnt')

    #Hash the user password before insert in to the data base, then 
    #the check_hashing verify the integrity of the data
    def hashPassword(self, passUser):
        passwordBytes = passUser.encode('utf-8')
        #salt to write in venv.env
        print(passUser)

        #Write salt on venv.env
        diruserPath = os.path.join(self.PATH_DIR, self.nomUsuario, "venv.env")

        salt = bcrypt.gensalt()
        print(salt)

        #Write data on env file
        with open(diruserPath, "a") as f: 
            f.write("SALT = " + salt.decode() + "\n")

        passHashing = bcrypt.hashpw(passwordBytes, salt)
        print(passHashing)
        return passHashing

#gestor =Harpo(nomUsuario='RELC040721HASYPHA4', passUser='1234abcde')
#gestor.mkdiruser()
#gestor.hashPassword('12345678990')