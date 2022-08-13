# WebScraping

Conteúdo educacional de Web Scraping

### Recomendado instalar uma virtualenv para isolar o ambiente de trabalho

```bash
python3 -m venv venv
```

### Identificando Tecnologias utilizadas no Website

##### iremos instalar a biblioteca `builtwith`

```bash
pip install builtwith
```

- Utilizar o interpretador do python

```bash
python3
```

- inicialmente precisamos importar a biblioteca `builtwith`

```bash
import builtwith
```

- utilizando o método `parse` e informando a url do site que queremos identificar

```bash
builtwith.parse('https://www.facebook.com')
```

### Identificando proprietário de um website

##### utilizar a biblioteca Whois

```bash
pip install python-whois
```

- Utilizar o interpretador do python

```bash
python3
```

- importar a biblioteca `whois`

```bash
import whois
```

- obtendo informações de um website

```bash
print(whois.whois('globo.com'))
```

### Carregando páginas web

##### utilizando requests através da biblioteca `urllib`

```bash

from urllib.request import urlopen
html = urlopen("http://www.google.com")
print(html.read())
```

### pegar informações das páginas web

##### instalando a biblioteca `BeautifulSoup`

- com a `virtualenv` ativa, vamos instalar a biblioteca:

```bash
pip install beautifulsoup4
```

- Utilizar o interpretador do python

```bash
python3
```

##### utilizando a biblioteca `BeautifulSoup`

```bash
from bs4 import BeautifulSoup
```

### Iniciar um servidor web

##### recomendado criar um diretório `mkdir #nomeDoDiretório`

- executar comando dentro do diretório

```bash
python -m http.server
```
