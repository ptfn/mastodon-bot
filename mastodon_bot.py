import requests
import schedule
import os
import time

token = os.getenv('TOKEN')
coins = ['btc', 'eth', 'xmr', 'ltc', 'etc', 'dot', 'grin']
url = "https://botsin.space/api/v1/statuses"


def price_coin(arr):
    r = requests.get('https://www.bw.com/exchange/config/controller/website/pricecontroller/getassistprice')
    data = r.json()
    string = ''
    for i in range(len(arr)):
        price = data['datas']['usd'][arr[i]]
        string_coin = arr[i]
        string = string + string_coin.upper() + ': ' + price + '$' + '\n'
    return string


def run_func(price_coin):
    headers = {"Authorization": "Bearer " + token}
    body = {"status": price_coin(coins) }
    r = requests.post(url, headers = headers, json = body, timeout = 10)


schedule.every().day.at("00:00").do(run_func, price_coin)
schedule.every().day.at("04:00").do(run_func, price_coin)
schedule.every().day.at("08:00").do(run_func, price_coin)
schedule.every().day.at("12:00").do(run_func, price_coin)
schedule.every().day.at("16:00").do(run_func, price_coin)
schedule.every().day.at("20:00").do(run_func, price_coin)


while True:
    schedule.run_pending()
    time.sleep(1)