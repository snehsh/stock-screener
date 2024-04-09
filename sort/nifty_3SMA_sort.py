import pandas as pd
from indicator import StockAnalyzer
from functools import lru_cache


@lru_cache(maxsize=None)
def nifty50_sort_3SMA():
    results_50 = []
    csv_file_path = "/Users/snehshah/PycharmProjects/Python_Task/nifty_data/ticker50.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.SMA_3()
        results_50.append([row, signal])

    return results_50


@lru_cache(maxsize=None)
def nifty200_sort_3SMA():
    results_200 = []
    csv_file_path = "/Users/snehshah/PycharmProjects/Python_Task/nifty_data/ticker200.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.SMA_3()
        results_200.append([row, signal])

    return results_200


@lru_cache(maxsize=None)
def nifty500_sort_3SMA():
    results_500 = []
    csv_file_path = "/Users/snehshah/PycharmProjects/Python_Task/nifty_data/ticker500.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.SMA_3()
        results_500.append([row, signal])

    return results_500
