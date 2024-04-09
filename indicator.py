import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO


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
        year_data = self.data[-260:]

        plt.plot(year_data.index, year_data['Close'], label='Close Price')
        plt.plot(year_data.index, self.sma20, label='20-Day SMA', color='red')
        plt.plot(year_data.index, self.sma50, label='50-Day SMA', color='blue')
        plt.plot(year_data.index, self.sma200, label='200-Day SMA', color='green')

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
        year_data = self.data[-260:]
        all_time_high = self.all_time_high

        plt.plot(year_data.index, year_data['Close'], label='Close Price')

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f"Stock Prices for {self.ticker} (Last 12 Months)")

        plt.axhline(y=current_price, color='green', linestyle='--', label=f"Current Price: {current_price}")
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

        if 30 <= ((all_time_high - current_price) / all_time_high) * 100:
            signal = "Buy"
        else:
            signal = "No Signal"
        self.signal = signal
        return signal
