import requests  # Beautiful Soup 4 BS4 pip install bs4

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com',

             }
meus_cookies = {'ultima-visita': '10-10-2020'}
dados = {
    'username': 'rondi',
    'password': 'rondi123'
}

texto = None

try:
    requisicao = requests.post('https://putsreq.com/7B4ilfcOs09aaPHNLqL0',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    texto = requisicao.text
except Exception as e:
    print('Requisição deu erro: ', e)

print(texto)
