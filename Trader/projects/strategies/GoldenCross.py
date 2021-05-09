import backtrader as bt
import math
import pytz
from .history import *

local_tz = pytz.timezone('Europe/Istanbul')


def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)  # .normalize might be unnecessary


class GoldenCross(bt.Strategy):
    params = {('fast', 50), ('slow', 200),
              ('order_percentage', 0.95), ('ticker', 'BTC')}

    def __init__(self, ticker, order_percentage, response, id):
        self.params.ticker = ticker
        self.params.order_percentage = order_percentage
        self.response = response
        self.id = id

        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='50 minutes SMA')
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='200 minutes SMA')

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, self.slow_moving_average)

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (
                    self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                op = {'op': 'buy', 'date': str(utc_to_local(self.data.datetime.datetime(
                ))), 'val': self.data.close[0], 'ticker': self.params.ticker}
                if search_history(self.id, op):
                    set_history(self.id, op)
                    # callback from here
                    self.response.set_response("AL:  {} adet {}.  Değer: {}  Zaman: {}".format(self.params.ticker, self.size,
                                                                                               self.data.close[0], utc_to_local(self.data.datetime.datetime())))
                    self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:
                op = {'op': 'sell', 'date': utc_to_local(self.data.datetime.datetime(
                )), 'val': self.data.close[0], 'ticker': self.params.ticker}
                if search_history(self.id, op):
                    set_history(self.id, op)
                    # callback from here
                    self.response.set_response("SAT: {} adet {}.  Değer: {}  Zaman: {}".format(self.params.ticker, self.size,
                                                                                               self.data.close[0], utc_to_local(self.data.datetime.datetime())))
                    self.close()
