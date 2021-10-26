import requests
from bs4 import BeautifulSoup

def parse_ssr():
    response = requests.get('https://coinmarketcap.com/ru/')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('a', {'href': '/ru/currencies/dogecoin/markets/'}).text
    return data

def parse_csr():
    response = requests.get('https://www.blockchain.com/prices/api/coin-list-page?limit=20&page=0&tsym=USD')
    data = response.json()
    dogecoin = [x for x in data['Data'] if x['CoinInfo']['Name'] == 'DOGE'][0]
    return dogecoin['DISPLAY']['USD']['PRICE']

if __name__ == '__main__':
    print('Dogecoin rate:', parse_ssr())
    print('Dogecoin rate:', parse_csr())
