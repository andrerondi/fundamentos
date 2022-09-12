import requests
import json
import acesso

api = acesso.filme_key

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=' + api + '&t=' + titulo + '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def imprimir_detalhes(filme):
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Premios:', filme['Awards'])
    print('Poster:', filme['Poster'])
    print('')

sair = False
while not sair:
    op = input('Escreva o  nome de um filme ou SAIR para Fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            imprimir_detalhes(filme)
