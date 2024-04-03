import pandas as pd
from indicator import StockAnalyzer


def nifty50_sort_percent():
    results_50 = []
    csv_file_path = "../nifty_data/ticker50.csv"
    df = pd.read_csv(csv_file_path)
    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.percent_strategy()
        results_50.append([row, signal])

    return results_50


def nifty200_sort_percent():
    results_200 = []
    csv_file_path = "../nifty_data/ticker200.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.percent_strategy()
        results_200.append([row, signal])

    return results_200


def nifty500_sort_percent():
    results_500 = []
    csv_file_path = "../nifty_data/ticker500.csv"
    df = pd.read_csv(csv_file_path)

    for row in df['Ticker']:
        analyze = StockAnalyzer(row + ".NS")
        signal = analyze.percent_strategy()
        results_500.append([row, signal])

    return results_500
