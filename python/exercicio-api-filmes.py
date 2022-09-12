from glob import escape
import requests
import json
import acesso

api = acesso.filme_key

def existeFilmes(titulo):
    quant = 0
    
    try:
        req = requests.get('http://www.omdbapi.com/?apikey='+ api +'&s=' + titulo + '&type=movie')
        resposta = json.loads(req.text)
    except:
        print('Conexão falhou')

    if resposta['Response'] == 'True':
        quant = resposta['totalResults']
    return quant

def listaFilmes(titulo):
    lista = []

    for i in range(1,101):
        try:
            url = 'http://www.omdbapi.com/?apikey='+ api +'&s=' + titulo + '&type=movie&page=' + str(i)
            req = requests.get(url)
            resposta = json.loads(req.text)

            if resposta['Response'] == 'False':
                break
            else:
                for filme in resposta['Search']:
                    title = filme['Title']
                    ano = filme['Year']
                    string = title + ' (' + ano + ')'
                    lista.append(string)

        except:
            print('Conexão falhou')
    return lista

sair = False
while not sair:
    opcao = input('Pesquise por um filme ou digite SAIR: ')
    opcao.lower()

    if opcao == 'sair':
        sair = True
    else:
        lista_de_filmes = listaFilmes(opcao)
        print('Filmes encontrados: ', len(lista_de_filmes))

        for filme in lista_de_filmes:
            print(filme)



    