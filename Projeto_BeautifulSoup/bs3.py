from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.globo.com")
exibindoLinks = BeautifulSoup(html.read(), "html.parser")

print(exibindoLinks.find_all("a"))
for link in exibindoLinks.find_all("a"):
    print(link.get("href"))
