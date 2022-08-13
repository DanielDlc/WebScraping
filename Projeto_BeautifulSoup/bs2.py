from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000/teste2.html")
exibindoLinks = BeautifulSoup(html.read(), "html.parser")

print(exibindoLinks.find_all("a"))
for link in exibindoLinks.find_all("a"):
    print(link.get("href"))
