import requests as q
from bs4 import BeautifulSoup
def conta_palavra(url,palavra):
     cont=0
     pagina = q.get(url)
     conversor = pagina.text
     x = BeautifulSoup(conversor,features="html.parser")
     for word in x.findAll(palavra):
         cont=+1
         print(cont)

conta_palavra("https://pt.wikipedia.org/wiki/Anan%C3%A1s",'abacaxi')
