##Interagindo com o Sistema Operacional através de um import no Python
import os

##Limpa a tela do terminal.
os.system("clear")

##Mostra qual o diretório estamos usando naquele momento - WINDOWS.
os.getcwd()

##Cria uma pasta dentro do diretório informado.
##os.mkdir("Exemplo")

##Abre e organiza o HTMl de uma página para ser vista.
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://google.com.br")
bsbObj = BeautifulSoup(html.read())
print(bsbObj.h1)
