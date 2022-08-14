from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re


req = Request("http://www.tudogostoso.com.br",
              headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll("a", {"href": re.compile("/categorias/*")})

for link in links:
    print(link["href"])
