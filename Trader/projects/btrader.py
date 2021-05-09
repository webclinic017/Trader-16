import pandas as pd
import backtrader as bt
from API.alphavantage import AlphaVantage
from strategies.GoldenCross import GoldenCross
from matplotlib import pyplot
from config.config import *
import bank
import options


class Response():
    def __init__(self):
        self.responses = []

    def set_response(self, text):
        self.responses.append(text)

    def get_response(self):
        text = ""
        if self.responses:
            for i in self.responses:
                text += i.replace('+03:00', '') + '\n'
        return text


class BTrader():
    def __init__(self, cash, id):
        self.cerebro = bt.Cerebro()
        self.av = AlphaVantage(ALPHA_VANTAGE_API_KEY)
        self.id = id
        self.response = Response()

        temp_cash = bank.get_cash(id)
        if temp_cash:
            self.set_cash(temp_cash)
            self.cash = temp_cash
        else:
            self.set_cash(cash)
            self.cash = cash

        temp_opt = options.get_opt(id)
        if temp_opt:
            self.bar_period = temp_opt['bar']
            self.percentage = temp_opt['per']
        else:
            self.bar_period = selected_tf
            self.percentage = order_percentage

    def run(self):
        prices = pd.read_csv(self.av.get_intraday_crypto(
            ticker, self.bar_period), index_col='timestamp', parse_dates=True).iloc[::-1]
        feed = bt.feeds.PandasData(dataname=prices)

        self.cerebro.adddata(feed)
        self.cerebro.addstrategy(
            GoldenCross, ticker, self.percentage, self.response, self.id)

        self.cerebro.run()
        bank.set_cash(self.id, self.get_cash())

        return self.__get_revenue()

    def set_cash(self, amount):
        self.cerebro.broker.setcash(amount)

    def get_cash(self):
        return self.cerebro.broker.getvalue()

    def __get_revenue(self):
        revenue = ((- self.cash + self.get_cash()) / self.cash) * 100
        if revenue > 0:
            return "{0:.4f}% kar".format(revenue)
        elif revenue < 0:
            return "{0:.4f}% zarar".format(revenue)
        else:
            return 'Ne kar ne zarar'
