# -*- coding: utf-8 -*-

import requests
import json
import datetime
import time

while True:
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    requisicao = requests.get(url)

    cotacao = json.loads(requisicao.text)

    print('')
    print('#### COTAÇÃO ####', datetime.datetime.now())
    print(cotacao['USDBRL']['name'], ': R$', cotacao['USDBRL']['high'])
    print(cotacao['EURBRL']['name'], ': R$', cotacao['EURBRL']['high'])
    print(cotacao['BTCBRL']['name'], ': R$', cotacao['BTCBRL']['high'])
    time.sleep(30)