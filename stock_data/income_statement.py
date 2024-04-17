import yfinance as yf


class IncomeStatement:
    def __init__(self, ticker):
        self.ticker = ticker

    def income_statement_yearly(self):
        stock = yf.Ticker(self.ticker)
        income_statement = stock.income_stmt
        income_statement.columns = income_statement.columns.strftime('%Y-%m-%d')
        return income_statement

    def income_statement_quarterly(self):
        stock = yf.Ticker(self.ticker)
        income_statement = stock.quarterly_income_stmt
        income_statement.columns = income_statement.columns.strftime('%Y-%m-%d')
        return income_statement
