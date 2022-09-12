import requests
import json
import acesso

cidade = input('Escreva sua cidade: ')
api = acesso.clima_key

url = 'https://api.openweathermap.org/data/2.5/weather?q='+ cidade + '&appid=' + api
requisicao = requests.get(url)
tempo = json.loads(requisicao.text)
temperatura = float(tempo['main']['temp']) - 273.15

print('Condição do tempo: ', tempo['weather'][0]['main'])
print(f'Temperatura: {temperatura:,.2f}°C' )