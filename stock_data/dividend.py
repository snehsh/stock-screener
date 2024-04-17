import yfinance as yf


class DividendData:
    def __init__(self, ticker):
        self.ticker = ticker

    def dividends(self):
        stock = yf.Ticker(self.ticker)
        dividends = stock.get_dividends()
        if dividends.empty:
            return "NA", "NA"
        else:
            latest_dividend_date = dividends.index[-1]
            latest_dividend_amount = dividends.iloc[-1]
            return latest_dividend_date, latest_dividend_amount
