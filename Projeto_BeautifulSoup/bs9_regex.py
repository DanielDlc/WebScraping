"""
Regex para "\.{2}/img/gifts/img\d*\.jpg"
\.   -> Representa o caractere "." ponto literalmente
{2}  -> Indica duas ocorrências do caractere anterior ( o ponto no caso)
/img/gift/img  -> esse img faz parte do nome do arquivo (String literal)
\d   -> Representa o dígito de zero a nove
*    -> Indica zero ou mais ocorrências do caractere anterior 0 a 9
\.jpg -> Ponto literal e a string jpg
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen("https://pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, "html.parser")

imagens = soup("img", {"src": re.compile("\.{2}/img.gifts/img\d*\.jpg")})

for imagem in imagens:
    print(imagem["src"])
