import requests
import os


class AlphaVantage:
    def __init__(self, key):
        self.key = key

    def get_intraday_crypto(self, symbol, interval):
        response = requests.get(
            f"https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=%s&market=USD&interval=%s&outputsize=full&apikey=%s&datatype=csv" % (symbol, interval, self.key))
        path = os.path.join('data', symbol+interval+'.csv')
        with open(path, 'w+') as f:
            f.write(response.text)
        return path

    def get_intraday_forex(self, from_symbol, to_symbol, interval):
        response = requests.get('https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={}&to_symbol={}&interval={}&outputsize=full&apikey={}&datatype=csv'.format(
            from_symbol, to_symbol, interval, self.key))
        path = os.path.join('data', from_symbol+to_symbol+interval+'.csv')
        with open(path, 'w+') as f:
            f.write(response.text)
        return path
