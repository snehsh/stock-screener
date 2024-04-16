import yfinance as yf


class StockAnalyzer:
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

    def percent_strategy(self):
        current_price = self.current_price
        all_time_high = self.all_time_high
        percent_diff_from_all_time_high = ((all_time_high - current_price) / all_time_high) * 100
        rounded_percent_diff = round(percent_diff_from_all_time_high, 2)

        if 30 <= percent_diff_from_all_time_high:
            signal = "Buy"
        else:
            signal = "No Suggestion"
        self.signal = signal
        return signal, rounded_percent_diff
