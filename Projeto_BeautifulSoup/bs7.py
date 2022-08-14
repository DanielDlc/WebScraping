from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org")
bs = BeautifulSoup(html, "html.parser")

print(bs.get_text())  # exibir todo conteúdo em texto
