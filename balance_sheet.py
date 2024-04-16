import yfinance as yf


class BalanceSheet:
    def __init__(self, ticker):
        self.ticker = ticker

    def balance_sheet(self):
        stock = yf.Ticker(self.ticker)
        balance_sheet = stock.get_balance_sheet()
        return balance_sheet

