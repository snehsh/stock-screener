import pandas as pd

from indicators.SMA3_strategy import SMA3Strategy
import streamlit as st
from nifty_data import nse_stocks_list
from graphs import Graphs
from stock_data import StockData
from indicators.percent_startegy import PercentStrategy
from balance_sheet import BalanceSheet



def sma3_strategy_display():
    ticker_symbol = st.selectbox("Enter Stock Ticker Symbol:", nse_stocks_list.display_list)
    usable_ticker = ticker_symbol.upper() + ".NS"
    if st.button("Analyze"):
        stock_analyzer = SMA3Strategy(usable_ticker)
        signal = stock_analyzer.SMA_3()
        st.header(f"{ticker_symbol.upper()}")
        st.write(f"Current Signal: {signal}")
        tab1, tab2, tab3 = st.tabs(["Graph", "Additional Info", "Balance Sheet"])

        with tab1:
            plot_graph = Graphs(usable_ticker)
            image_data = plot_graph.plot_data_3SMA()
            st.image(image_data, use_column_width=True)

        with tab2:
            dividend_data = StockData(usable_ticker)
            latest_dividend_date, latest_dividend_amount = dividend_data.dividends()
            st.subheader("Additional Info")
            st.write(f"Latest Dividend Date: {latest_dividend_date.strftime('%Y-%m-%d')}")
            st.write(f"Latest Dividend Amount: {latest_dividend_amount:.2f}")

        with tab3:
            enter_balance_sheet = BalanceSheet(usable_ticker)
            get_balance_sheet = enter_balance_sheet.balance_sheet()

            st.subheader("Balance Sheet")
            st.dataframe(get_balance_sheet)


def percent_strategy_display():
    ticker_symbol = st.selectbox("Enter Stock Ticker Symbol:", nse_stocks_list.display_list_nifty50)
    usable_ticker = ticker_symbol.upper() + ".NS"
    select_percent = st.slider("Enter your choice of %", 0, 100, 1)
    st.write(f"Selected Percentage: {select_percent}")
    if st.button("Analyze"):
        stock_analyzer = PercentStrategy(usable_ticker, select_percent)
        signal, rounded_percent_diff = stock_analyzer.percent_strategy()
        st.header(f"{ticker_symbol.upper()}")
        st.write(f"Current Signal: {signal}")
        tab1, tab2, tab3 = st.tabs(["Graph", "Additional Info", "Balance Sheet"])

        with tab1:
            plot_graph = Graphs(usable_ticker)
            st.write(f"The stock is {rounded_percent_diff}% down from all time high.")
            image_data = plot_graph.plot_data_percent()
            st.image(image_data, use_column_width=True)

        with tab2:
            dividend_data = StockData(usable_ticker)
            latest_dividend_date, latest_dividend_amount = dividend_data.dividends()
            st.subheader("Additional Info")
            st.write(f"Latest Dividend Date: {latest_dividend_date.strftime('%Y-%m-%d')}")
            st.write(f"Latest Dividend Amount: {latest_dividend_amount:.2f}")

        with tab3:
            enter_balance_sheet = BalanceSheet(usable_ticker)
            get_balance_sheet = enter_balance_sheet.balance_sheet()
            st.subheader("Balance Sheet")
            st.dataframe(get_balance_sheet)
