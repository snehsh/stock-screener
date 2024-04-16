import yfinance as yf


class StockData:
    def __init__(self, ticker):
        self.signal = None
        self.ticker = ticker

    def dividends(self):
        stock = yf.Ticker(self.ticker)
        dividends = stock.get_dividends()
        latest_dividend_date = dividends.index[-1]
        latest_dividend_amount = dividends.iloc[-1]
        return latest_dividend_date, latest_dividend_amount
