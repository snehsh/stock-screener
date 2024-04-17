import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO


class SMA3Graph:
    def __init__(self, ticker):
        self.signal = None
        self.ticker = ticker
        self.data = yf.download(ticker, period="2y", interval="1d")
        self.all_time_data = yf.download(ticker, period="max")
        self.sma20 = self.data['Close'].rolling(window=20).mean()[-260:]
        self.sma50 = self.data['Close'].rolling(window=50).mean()[-260:]
        self.sma200 = self.data['Close'].rolling(window=200).mean()[-260:]
        self.all_time_high = self.all_time_data['Close'].max()
        self.current_price = self.data['Close'].iloc[-1]

    def plot_data_3SMA(self):
        plt.figure(figsize=(10, 6))
        current_price = self.current_price
        rounded_price = round(current_price, 2)
        rounded_sma20 = round(self.sma20[-1], 2)
        rounded_sma50 = round(self.sma50[-1], 2)
        rounded_sma200 = round(self.sma200[-1], 2)
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


