from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://udemy.com")
bs = BeautifulSoup(html.read(), "html.parser")

try:
    resultado = bs.html.tag_nao_existente.tag_vai_dar_erro
    print(resultado)
except AttributeError as erro:
    print(f"Erro: {erro}")
