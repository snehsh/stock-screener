import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO


class PercentGraph:
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