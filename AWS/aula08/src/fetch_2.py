from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os
from pprint import pprint

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

response = session.get(url=url, params=parameters)
data = json.loads(response.text) # transforma a resposta em um dicionario

bitcoin_data = data['data']['BTC'] # acessa o dicionario e pega os dados do bitcoin
brl_quote = bitcoin_data['quote']['BRL'] # acessa o dicionario e pega a cotacao em real
brl_price = brl_quote['price'] # acessa o dicionario e pega o preco

# pprint(brl_quote) # imprime o dicionario inteiro
print(f"Última cotação do Bitcoin: ${brl_quote['price']:.2f} BRL")
print(f"Volume 24h: ${brl_quote['volume_24h']:.2f} BRL")
print(f"Market Cap: ${brl_quote['market_cap']:.2f} BRL")
print(f"Última atualização: {brl_quote['last_updated']}")