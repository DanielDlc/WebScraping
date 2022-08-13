from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def getTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print(f"Ocorreu um erro HTTP: {erro}")
        return None
    except URLError as erro:
        print(f"Ocorreu um erro de URL: {erro}")
        return None
    except:
        print("Ocorreu um erro na página")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        titulo = bsObj.body.h1
    except AttributeError as erro:
        print(f"Ocorreu um erro as acessar a tag h1: {erro}")
        return None
    except:
        print("Ocorreu um erro ao acessar o conteúdo da página")
        return None

    return titulo


novoTitulo = getTitulo(input("Informe a URL completa: "))

if novoTitulo is not None:
    print(novoTitulo)
else:
    ("Título não encontrado")
