import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd


class StockAnalyzer:
    def __init__(self, ticker, *percent):
        self.signal = None
        self.ticker = ticker
        self.percent = percent
        self.data = yf.download(ticker, period="2y", interval="1d")
        self.all_time_data = yf.download(ticker, period="max")
        self.sma20 = self.data['Close'].rolling(window=20).mean()[-260:]
        self.sma50 = self.data['Close'].rolling(window=50).mean()[-260:]
        self.sma200 = self.data['Close'].rolling(window=200).mean()[-260:]
        self.all_time_high = self.all_time_data['Close'].max()
        self.current_price = self.data['Close'].iloc[-1]


    def SMA_3(self):
        current_price = self.current_price
        sma20 = self.sma20
        sma50 = self.sma50
        sma200 = self.sma200

        if (sma20.iloc[-1] < sma50.iloc[-1] < sma200.iloc[-1]) and (current_price < sma20.iloc[-1]):
            signal = "Buy"
        elif (sma200.iloc[-1] < sma50.iloc[-1] < sma20.iloc[-1]) and (current_price > sma20.iloc[-1]):
            signal = "Sell"
        else:
            signal = "Hold"
        self.signal = signal

        return signal

    def plot_data_3SMA(self):
        plt.figure(figsize=(10, 6))
        current_price = self.current_price
        rounded_price = round(current_price,2)
        rounded_sma20 = round(self.sma20[-1],2)
        rounded_sma50 = round(self.sma50[-1],2)
        rounded_sma200 = round(self.sma200[-1],2)
        year_data = self.data[-260:]

        plt.plot(year_data.index, year_data['Close'], label=f'Close Price: {rounded_price}')
        plt.plot(year_data.index, self.sma20, label=f'20-Day SMA: {rounded_sma20}', color='red')
        plt.plot(year_data.index, self.sma50, label=f'50-Day SMA: {rounded_sma50}', color='blue')
        plt.plot(year_data.index, self.sma200, label=f'200-Day SMA: {rounded_sma200}', color='green')

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f"Stock Prices for {self.ticker} (Last 12 Months)")

        if self.signal == "Buy":
            plt.axhline(y=current_price, color='green', linestyle='--', label=f"Current Price: {current_price}")

        elif self.signal == "Sell":
            plt.axhline(y=current_price, color='red', linestyle='--', label=f"Current Price: {current_price}")

        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()
        buffer.seek(0)

        return buffer

    def plot_data_percent(self):
        plt.figure(figsize=(10, 6))
        current_price = self.current_price
        rounded_price = round(current_price, 2)
        year_data = self.data[-260:]
        all_time_high = self.all_time_high
        plt.plot(year_data.index, year_data['Close'], label=f'Close Price {rounded_price}')

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f"Stock Prices for {self.ticker} (Last 12 Months)")

        plt.axhline(y=all_time_high, color='red', linestyle='--', label=f"All Time High: {all_time_high}")

        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()
        buffer.seek(0)

        return buffer

    def percent_strategy(self):
        current_price = self.current_price
        all_time_high = self.all_time_high
        percent_diff_from_all_time_high = ((all_time_high - current_price) / all_time_high) * 100
        rounded_percent_diff = round(percent_diff_from_all_time_high,2)

        if 30 <= percent_diff_from_all_time_high:
            signal = "Buy"
        else:
            signal = "No Suggestion"
        self.signal = signal
        return signal, rounded_percent_diff

    def dividends(self):
        stock = yf.Ticker(self.ticker)
        dividends = stock.get_dividends()
        latest_dividend_date = dividends.index[-1]
        latest_dividend_amount = dividends.iloc[-1]
        return latest_dividend_date, latest_dividend_amount

