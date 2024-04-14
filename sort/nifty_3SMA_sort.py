import pandas as pd
from indicator import StockAnalyzer
import streamlit as st
import datetime


@st.cache_data(ttl=datetime.timedelta(hours=2), show_spinner=False)
def nifty50_sort_3SMA():
    results_50 = []
    csv_file_path = "/Users/snehshah/PycharmProjects/Python_Task/nifty_data/ticker50.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.SMA_3()
        results_50.append([row, signal])

    return results_50


@st.cache_data(ttl=datetime.timedelta(hours=2), show_spinner=False)
def nifty200_sort_3SMA():
    results_200 = []
    csv_file_path = "/Users/snehshah/PycharmProjects/Python_Task/nifty_data/ticker200.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.SMA_3()
        results_200.append([row, signal])

    return results_200


@st.cache_data(ttl=datetime.timedelta(hours=2), show_spinner=False)
def nifty500_sort_3SMA():
    results_500 = []
    csv_file_path = "/Users/snehshah/PycharmProjects/Python_Task/nifty_data/ticker500.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.SMA_3()
        results_500.append([row, signal])

    return results_500
