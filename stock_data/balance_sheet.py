import yfinance as yf


class BalanceSheet:
    def __init__(self, ticker):
        self.ticker = ticker

    def balance_sheet_yearly(self):
        stock = yf.Ticker(self.ticker)
        balance_sheet = stock.balance_sheet
        balance_sheet.columns = balance_sheet.columns.strftime('%Y-%m-%d')
        return balance_sheet

    def balance_sheet_quarterly(self):
        stock = yf.Ticker(self.ticker)
        balance_sheet = stock.quarterly_balance_sheet
        balance_sheet.columns = balance_sheet.columns.strftime('%Y-%m-%d')
        return balance_sheet
