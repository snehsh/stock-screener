import yfinance as yf


class RSIStrategy:
    def __init__(self, ticker,rsi_length, window):
        self.signal = None
        self.ticker = ticker
        self.rsi_length = rsi_length
        self.window = window
        self.data = yf.download(ticker, period="", interval="1d")
        self.all_time_data = yf.download(ticker, period="max")
        self.all_time_high = self.all_time_data['Close'].max()
        self.current_price = self.data['Close'].iloc[-1]

    def RSI(self):
        delta = self.data["Close"].diff()
        delta = delta.dropna()

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        ema_up = up.ewm(alpha=1 / self.rsi_length, min_periods=self.rsi_length).mean()
        ema_down = down.abs().ewm(alpha=1 / self.rsi_length, min_periods=self.rsi_length).mean()

        RS = ema_up / ema_down
        RSI = 100 - (100 / (1 + RS))
        RSI = RSI.dropna()
        RSI_SMA=RSI.rolling(window=self.window).mean()

        return RSI,RSI_SMA

    def RSI_signal(self):
        data = self.RSI()[0]

        buy_level = 30
        sell_level = 70
        if data.iloc[-1] < buy_level:
            signal = "Buy"
        elif data.iloc[-1] > sell_level:
            signal = "Sell"
        else:
            signal = "Hold"
        self.signal = signal
        return signal, data.iloc[-1]
