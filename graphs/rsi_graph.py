import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
from indicators.rsi_strategy import RSIStrategy


class RSIGraph:
    def __init__(self, ticker, rsi_length, window):
        self.signal = None
        self.ticker = ticker
        self.rsi_length = rsi_length
        self.window = window
        self.data = yf.download(ticker, period="2y", interval="1d")
        self.all_time_data = yf.download(ticker, period="max")
        self.all_time_high = self.all_time_data['Close'].max()
        self.current_price = self.data['Close'].iloc[-1]

    def plot_data_RSI(self):
        plt.figure(figsize=(10, 6))
        year_data = self.data[-130:]
        RSI = RSIStrategy(self.ticker, self.rsi_length, self.window)
        rsi, rsi_sma = RSI.RSI()
        rsi = rsi[-130:]
        rsi_sma = rsi_sma[-130:]
        current_rsi = round(rsi.iloc[-1], 2)

        plt.plot(year_data.index, rsi, label=f'Current RSI: {current_rsi}', color='purple')
        plt.plot(year_data.index, rsi_sma, label=f'RSI SMA, Window: {self.window} days', color='orange')

        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.ylim(0, 100)
        plt.yticks(range(0, 101, 10))
        plt.title(f"RSI Graph for {self.ticker}")

        plt.axhline(y=30, color='black', linestyle='--', label="RSI=30(Buy Level)")
        plt.axhline(y=70, color='black', linestyle='--', label="RSI=70(Sell Level)")

        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()
        buffer.seek(0)

        return buffer
