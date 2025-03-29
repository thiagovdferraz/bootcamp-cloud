from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os
from pprint import pprint
import schedule
import time

load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'symbol': 'BTC', # identifica bitcoin pelo simbolo
    'convert': 'BRL' # converte a cotacao para real
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY'), # obter a chave do .ENV
}

session = Session()
session.headers.update(headers)

def consultar_cotacao_bitcoin():
    try:
        response = session.get(url=url, params=parameters)
        data = json.loads(response.text) # transforma a resposta em um dicionario

        if 'data' in data and 'BTC' in data['data']:
            bitcoin_data = data['data']['BTC'] # acessa o dicionario e pega os dados do bitcoin
            brl_quote = bitcoin_data['quote']['BRL'] # acessa o dicionario e pega a cotacao em real

            # pprint(brl_quote) # imprime o dicionario inteiro
            print(f"Última cotação do Bitcoin: ${brl_quote['price']:.2f} BRL")
            print(f"Volume 24h: ${brl_quote['volume_24h']:.2f} BRL")
            print(f"Market Cap: ${brl_quote['market_cap']:.2f} BRL")
            print(f"Última atualização: {brl_quote['last_updated']}")
        else:
            print("Dados do Bitcoin não encontrados na resposta: ", data['status'].get('error_message', 'Erro desconhecido'))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro na requisição: {e}")

consultar_cotacao_bitcoin()

schedule.every(15).seconds.do(consultar_cotacao_bitcoin) # rodar a cada 15 segundos

print('Iniciando o agendador...')

while True:
    schedule.run_pending()
    time.sleep(1)