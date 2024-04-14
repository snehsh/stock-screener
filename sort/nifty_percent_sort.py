import pandas as pd
import streamlit as st
from indicator import StockAnalyzer
import datetime


@st.cache_data(ttl=datetime.timedelta(hours=2), show_spinner=False)
def nifty50_sort_percent():
    results_50 = []
    csv_file_path = "nifty_data/ticker50.csv"
    df = pd.read_csv(csv_file_path)
    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.percent_strategy()
        results_50.append([row, signal])

    return results_50
