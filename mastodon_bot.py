import requests
import schedule
import os
import time

token = os.getenv('TOKEN')
coins = ['btc', 'eth', 'xmr', 'ltc', 'etc', 'dot','grin', 'ksm']
url = "https://botsin.space/api/v1/statuses"


def price_coin(arr):
    string = ''
    for i in range(len(arr)):
        try:
            r = requests.get('https://api.bitfinex.com/v1/pubticker/'+ arr[i] +'usd')
            data = r.json()
            price = data['ask']
            string_coin = arr[i]
            string = string + string_coin.upper() + ': ' + price + '$' + '\n'
        except:
            print('Error')
    return string


def run_func(price_coin):
    headers = {"Authorization": "Bearer " + token}
    body = {"status": price_coin(coins) }
    r = requests.post(url, headers = headers, json = body, timeout = 10)


schedule.every().hour.do(run_func, price_coin)


while True:
    schedule.run_pending()
    time.sleep(1)
