from nturl2path import url2pathname
import requests
import re

url = 'https://solyd.com.br/contato/'
requisicao = requests.get(url)

padrao = re.findall(r'[\w\.-_]+@[\w\.-_]+\.[\w\.-_]+', requisicao.text)


if padrao:
    print(padrao)
else:
    print('Padrao nao encontrado')