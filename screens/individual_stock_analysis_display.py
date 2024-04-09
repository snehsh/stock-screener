from indicator import StockAnalyzer
import streamlit as st
from nifty_data import nse_stocks_list

def sma3_strategy_display():
    ticker_symbol = st.selectbox("Enter Stock Ticker Symbol:", nse_stocks_list.display_list)
    usable_ticker = ticker_symbol.upper() + ".NS"
    if st.button("Analyze"):
        stock_analyzer = StockAnalyzer(usable_ticker)
        signal = stock_analyzer.SMA_3()

        st.write(f"Ticker Symbol: {ticker_symbol.upper()}")
        st.write(f"Current Signal: {signal}")

        image_data = stock_analyzer.plot_data_3SMA()
        st.image(image_data, width=1000)

def percent_strategy_display():
    ticker_symbol = st.selectbox("Enter Stock Ticker Symbol:",nse_stocks_list.display_list_nifty50)
    usable_ticker = ticker_symbol.upper() + ".NS"
    if st.button("Analyze"):
        stock_analyzer = StockAnalyzer(usable_ticker)
        signal = stock_analyzer.percent_strategy()

        st.write(f"Ticker Symbol: {ticker_symbol.upper()}")
        st.write(f"Current Signal: {signal}")

        image_data = stock_analyzer.plot_data_percent()
        st.image(image_data, width=1000)