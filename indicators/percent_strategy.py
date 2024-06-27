import yfinance as yf


class PercentStrategy:
    def __init__(self, ticker, percent):
        self.signal = None
        self.ticker = ticker
        self.percent = percent
        self.data = yf.download(ticker, period="max", interval="1d")
        self.all_time_data = yf.download(ticker, period="max")
        self.sma20 = self.data['Close'].rolling(window=20).mean()[-260:]
        self.sma50 = self.data['Close'].rolling(window=50).mean()[-260:]
        self.sma200 = self.data['Close'].rolling(window=200).mean()[-260:]
        self.all_time_high = self.all_time_data['Close'].max()
        self.current_price = self.data['Close'].iloc[-1]

    def percent_strategy(self):
        current_price = self.current_price
        all_time_high = self.all_time_high
        percent = self.percent
        percent_diff_from_all_time_high = ((all_time_high - current_price) / all_time_high) * 100
        rounded_percent_diff = round(percent_diff_from_all_time_high, 2)

        if percent <= percent_diff_from_all_time_high:
            signal = "Buy"
        else:
            signal = "No Suggestion"
        self.signal = signal
        return signal, rounded_percent_diff
