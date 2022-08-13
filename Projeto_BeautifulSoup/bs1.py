from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000/teste1.html")
exibirObjeto = BeautifulSoup(html.read(), "html.parser")

# print(exibirObjeto.h1)
# print(exibirObjeto.title)
print(exibirObjeto.find_all("h1"))
