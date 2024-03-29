import os
import time
import requests
import schedule


token = os.getenv('TOKEN')
url = "https://botsin.space/api/v1/statuses"
coins = ['btc', 'eth', 'ltc',
         'xmr', 'uni', 'dot',
         'ksm', 'ada', 'xrp']
last_price = {'btc': 0, 'eth': 0, 'ltc': 0,
              'xmr': 0, 'uni': 0, 'dot': 0,
              'ksm': 0, 'ada': 0, 'xrp': 0}


def persent_price(last, new):
    return round((new - last) / last * 100, 2)


def price_coin(arr):
    string = ''
    for i in range(len(arr)):
        r = requests.get('https://api.bitfinex.com/v1/pubticker/'+arr[i]+'usd')
        data = r.json()
        price = data['ask']
        coin = arr[i]
        if last_price[coin] == 0:
            string = string + coin.upper() + ': ' + '$' + price + '\n'
        else:
            per = persent_price(float(last_price[coin]), float(price))
            string += f"{coin.upper()}: $ {price} {per}%\n"
        last_price[coin] = price
    return string


def request(price_coin):
    headers = {"Authorization": "Bearer " + token}
    body = {"status": price_coin(coins)}
    r = requests.post(url, headers=headers, json=body, timeout=60)


def main():
    schedule.every().hours.do(request, price_coin)

    while True:
        try:
            schedule.run_pending()
        except Exception:
            print("--Request Error!--")
        else:
            print("--Request Ok!--")
        finally:
            time.sleep(15)


if __name__ == "__main__":
    main()
