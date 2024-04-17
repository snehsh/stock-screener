import yfinance as yf


class CashFlow:
    def __init__(self, ticker):
        self.ticker = ticker

    def cash_flow_yearly(self):
        stock = yf.Ticker(self.ticker)
        cash_flow = stock.cash_flow
        cash_flow.columns = cash_flow.columns.strftime('%Y-%m-%d')
        return cash_flow.head(1)

    def cash_flow_quarterly(self):
        stock = yf.Ticker(self.ticker)
        cash_flow = stock.quarterly_cash_flow
        cash_flow.columns = cash_flow.columns.strftime('%Y-%m-%d')
        return cash_flow.head(1)
