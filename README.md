# WebScraping

Conteúdo educacional de Web Scraping

### Recomendado instalar uma virtualenv para isolar o ambiente de trabalho

```bash
python3 -m venv venv
```

### Identificando Tecnologias utilizadas no Website

##### iremos instalar a biblioteca builtwith

```bash
pip install builtwith
```

- Utilizar o interpretador do python

```bash
python3
```

- inicialmente precisamos importar a biblioteca builtwith

```bash
import builtwith
```

- utilizando o método parse e informando a url do site que queremos identificar

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

- importar a biblioteca whois

```bash
import whois
```

- obtendo informações de um website

```bash
print(whois.whois('globo.com'))
```
