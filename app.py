from harpo import *

#Make dir of each user from Harpo class
def HarpoDirs():
    username = "RELC040721HASYPHA4"
    password = '1234532'
    gestor = Harpo(nomUsuario=username, passUser=password)
    gestor.mkdiruser()
    gestor.hashPassword(password)








if __name__ == "__main__":
    HarpoDirs()