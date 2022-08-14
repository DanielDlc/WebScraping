from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000/teste3.html")
soup = BeautifulSoup(html, "html.parser")

print("Veja o conteúdo com o prettify")
print(soup.prettify())

print("")
print("Título do documento:")
print(soup.title)

print("")
print("Node da tag pai da tag title:")
print(soup.title.parent.name)

print("Primeira tag 'p' do texto:")
print(soup.p['class'])

print("")
print("Primeira ocorrência da tag 'a':")
print(soup.a)
