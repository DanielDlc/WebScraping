from urllib.error import HTTPError, URLError
from urllib.request import urlopen

html = urlopen("http://www.udemy.com")
print(f"Html 1: {html}")

try:
    html = urlopen("http://udemy.com/erro")
except HTTPError as erro:
    print(erro)

try:
    html = urlopen("http://www.paginadexpto")  # não existe esse endereço
except URLError as erro:
    print(erro)
