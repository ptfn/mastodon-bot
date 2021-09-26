import requests
import schedule
import os
import time

token = os.getenv('TOKEN')
coins = ['btc', 'eth', 'ltc', 'xmr', 'uni', 'dot', 'ksm']
url = "https://botsin.space/api/v1/statuses"
last_price = {'btc' : 0, 'eth' : 0, 'ltc' : 0, 'xmr' : 0, 'uni' : 0, 'dot' : 0, 'ksm' : 0}


def persent_price(last, new):
    return round((new - last) / last * 100, 2)


def price_coin(arr):
    string = ''
    for i in range(len(arr)):
        r = requests.get('https://api.bitfinex.com/v1/pubticker/'+ arr[i] +'usd')
        data = r.json()
        price = data['ask']
        coin = arr[i]
        if last_price[coin] == 0:
            string = string + coin.upper() + ': ' + '$' + price + '\n'
        else:
            per = persent_price(float(last_price[coin]), float(price))
            string = string + coin.upper() + ': ' + '$' + price + ' ({}%)'.format(per) + '\n'
        last_price[coin] = price
    return string


def run_func(price_coin):
    headers = {"Authorization": "Bearer " + token}
    body = {"status": price_coin(coins) }
    r = requests.post(url, headers = headers, json = body, timeout = 30)


schedule.every().hours.do(run_func, price_coin)


while True:
    try:
        schedule.run_pending()
    except:
        print("Error!")
        time.sleep(10)
