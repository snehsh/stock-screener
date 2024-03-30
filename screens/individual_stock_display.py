from indicator import StockAnalyzer
import streamlit as st

def individual_stock_display():
    ticker_symbol = st.text_input("Enter Stock Ticker Symbol:")
    usable_ticker = ticker_symbol.upper() + ".NS"
    if st.button("Analyze"):
        stock_analyzer = StockAnalyzer(usable_ticker)
        signal = stock_analyzer.SMA_3()

        st.write(f"Ticker Symbol: {ticker_symbol.upper()}")
        st.write(f"Current Signal: {signal}")

        image_data = stock_analyzer.plot_data()
        st.image(image_data, width=1000)