import pandas as pd
from indicator import StockAnalyzer
from functools import lru_cache


@lru_cache(maxsize=None)
def nifty50_sort_percent():
    results_50 = []
    csv_file_path = "/Users/snehshah/PycharmProjects/Python_Task/nifty_data/ticker50.csv"
    df = pd.read_csv(csv_file_path)
    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.percent_strategy()
        results_50.append([row, signal])

    return results_50
