from indicator import StockAnalyzer
import streamlit as st
from nifty_data import nse_stocks_list
from graphs import Graphs
from stock_data import StockData


def sma3_strategy_display():
    ticker_symbol = st.selectbox("Enter Stock Ticker Symbol:", nse_stocks_list.display_list)
    usable_ticker = ticker_symbol.upper() + ".NS"
    if st.button("Analyze"):
        stock_analyzer = StockAnalyzer(usable_ticker)
        signal = stock_analyzer.SMA_3()
        plot_graph = Graphs(usable_ticker)
        dividend_data=StockData(usable_ticker)
        latest_dividend_date, latest_dividend_amount = dividend_data.dividends()

        st.write(f"Ticker Symbol: {ticker_symbol.upper()}")
        st.write(f"Current Signal: {signal}")

        image_data = plot_graph.plot_data_3SMA()
        st.image(image_data, width=800)

        st.subheader("Additional Info")
        st.write(f"Latest Dividend Date: {latest_dividend_date.strftime('%Y-%m-%d')}")
        st.write(f"Latest Dividend Amount: {latest_dividend_amount:.2f}")


def percent_strategy_display():
    ticker_symbol = st.selectbox("Enter Stock Ticker Symbol:", nse_stocks_list.display_list_nifty50)
    usable_ticker = ticker_symbol.upper() + ".NS"
    if st.button("Analyze"):
        stock_analyzer = StockAnalyzer(usable_ticker)
        signal, rounded_percent_diff = stock_analyzer.percent_strategy()
        plot_graph = Graphs(usable_ticker)
        dividend_data = StockData(usable_ticker)
        latest_dividend_date, latest_dividend_amount = dividend_data.dividends()

        st.write(f"Ticker Symbol: {ticker_symbol.upper()}")
        st.write(f"Current Signal: {signal}")
        st.write(f"The stock is {rounded_percent_diff}% down from all time high.")

        image_data = plot_graph.plot_data_percent()
        st.image(image_data, width=800)
        st.subheader("Additional Info")
        st.write(f"Latest Dividend Date: {latest_dividend_date.strftime('%Y-%m-%d')}")
        st.write(f"Latest Dividend Amount: {latest_dividend_amount:.2f}")
