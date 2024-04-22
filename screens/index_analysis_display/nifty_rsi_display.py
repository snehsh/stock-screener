import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, SimpleDocTemplate, TableStyle
from indicators.rsi_strategy import RSIStrategy


def download_pdf_50_rsi():
    select_length = st.number_input(":orange[Select RSI length:]", key="number_input_1", min_value=1, max_value=100,
                                    value=14)
    st.write(f"Selected RSI length: {select_length}")
    select_window = st.number_input(":orange[Select SMA Window:]", key="number_input_2", min_value=1, max_value=260,
                                    value=14)
    st.write(f"Selected Window: {select_window}")
    if st.button("Analyze Stocks", key="button1"):
        results_50 = []
        csv_file_path = "nifty_data/ticker50.csv"
        df = pd.read_csv(csv_file_path)
        for row in df['Ticker']:
            analyze = RSIStrategy(row + ".NS", select_length, select_window)
            signal = analyze.RSI_signal()
            results_50.append([row, signal[0]])

        my_list = results_50
        df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])

        b = pd.DataFrame(df[df.Signal == 'Buy']['Stock Name'])
        b.columns = ['Buy']
        s = pd.DataFrame(df[df.Signal == 'Sell']['Stock Name'])
        s.columns = ['Sell']
        h = pd.DataFrame(df[df.Signal == 'Hold']['Stock Name'])
        h.columns = ['Hold']
        b = b.reset_index()['Buy']
        s = s.reset_index()['Sell']
        h = h.reset_index()['Hold']
        sorted_df = pd.concat([b, s, h], axis=1).fillna('')

        col1, col2, col3 = st.columns(3)

        col1.header("Buy")
        col1.table(sorted_df['Buy'])

        col2.header("Sell")
        col2.table(sorted_df['Sell'])

        col3.header("Hold")
        col3.table(sorted_df['Hold'])

        pdf = SimpleDocTemplate("nifty_50_recommendation_rsi_strategy.pdf", pagesize=letter)
        table_data = [['Buy', 'Sell', 'Hold']]
        for i, row in sorted_df.iterrows():
            table_data.append(list(row))

        table = Table(table_data)
        table_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ])

        table.setStyle(table_style)

        pdf_table = []
        pdf_table.append(table)

        pdf.build(pdf_table)

        with open("nifty_50_recommendation_rsi_strategy.pdf", "rb") as pdf_file:
            data = pdf_file.read()
        st.download_button("Download PDF", data, file_name="nifty_50_recommendation_rsi_strategy.pdf")


def download_pdf_200_rsi():
    select_length = st.number_input(":orange[Select RSI length:]", key="number_input_3", min_value=1, max_value=100,
                                    value=14)
    st.write(f"Selected RSI length: {select_length}")
    select_window = st.number_input(":orange[Select SMA Window:]", key="number_input_4", min_value=1, max_value=260,
                                    value=14)
    st.write(f"Selected SMA Window: {select_window}")
    if st.button("Analyze Stocks", key="button2"):
        results_200 = []
        csv_file_path = "nifty_data/ticker200.csv"
        df = pd.read_csv(csv_file_path)
        for row in df['Ticker']:
            analyze = RSIStrategy(row + ".NS", select_length, select_window)
            signal = analyze.RSI_signal()
            results_200.append([row, signal[0]])

        my_list = results_200
        df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])

        b = pd.DataFrame(df[df.Signal == 'Buy']['Stock Name'])
        b.columns = ['Buy']
        s = pd.DataFrame(df[df.Signal == 'Sell']['Stock Name'])
        s.columns = ['Sell']
        h = pd.DataFrame(df[df.Signal == 'Hold']['Stock Name'])
        h.columns = ['Hold']
        b = b.reset_index()['Buy']
        s = s.reset_index()['Sell']
        h = h.reset_index()['Hold']
        sorted_df = pd.concat([b, s, h], axis=1).fillna('')

        col1, col2, col3 = st.columns(3)

        col1.header("Buy")
        col1.table(sorted_df['Buy'])

        col2.header("Sell")
        col2.table(sorted_df['Sell'])

        col3.header("Hold")
        col3.table(sorted_df['Hold'])

        pdf = SimpleDocTemplate("nifty_200_recommendation_rsi_strategy.pdf", pagesize=letter)
        table_data = [['Buy', 'Sell', 'Hold']]
        for i, row in sorted_df.iterrows():
            table_data.append(list(row))

        table = Table(table_data)
        table_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ])

        table.setStyle(table_style)

        pdf_table = []
        pdf_table.append(table)

        pdf.build(pdf_table)

        with open("nifty_200_recommendation_rsi_strategy.pdf", "rb") as pdf_file:
            data = pdf_file.read()
        st.download_button("Download PDF", data, file_name="nifty_200_recommendation_rsi_strategy.pdf")


def download_pdf_500_rsi():
    select_length = st.number_input(":orange[Select RSI length:]", key="number_input_5", min_value=1, max_value=100,
                                    value=14)
    st.write(f"Selected RSI length: {select_length}")
    select_window = st.number_input(":orange[Select SMA Window:]", key="number_input_6", min_value=1, max_value=260,
                                    value=14)
    st.write(f"Selected SMA Window: {select_window}")
    if st.button("Analyze Stocks", key="button3"):
        results_500 = []
        csv_file_path = "nifty_data/ticker500.csv"
        df = pd.read_csv(csv_file_path)
        for row in df['Ticker']:
            analyze = RSIStrategy(row + ".NS", select_length, select_window)
            signal = analyze.RSI_signal()
            results_500.append([row, signal[0]])

        my_list = results_500
        df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])

        b = pd.DataFrame(df[df.Signal == 'Buy']['Stock Name'])
        b.columns = ['Buy']
        s = pd.DataFrame(df[df.Signal == 'Sell']['Stock Name'])
        s.columns = ['Sell']
        h = pd.DataFrame(df[df.Signal == 'Hold']['Stock Name'])
        h.columns = ['Hold']
        b = b.reset_index()['Buy']
        s = s.reset_index()['Sell']
        h = h.reset_index()['Hold']
        sorted_df = pd.concat([b, s, h], axis=1).fillna('')

        col1, col2, col3 = st.columns(3)

        col1.header("Buy")
        col1.table(sorted_df['Buy'])

        col2.header("Sell")
        col2.table(sorted_df['Sell'])

        col3.header("Hold")
        col3.table(sorted_df['Hold'])

        pdf = SimpleDocTemplate("nifty_500_recommendation_rsi_strategy.pdf", pagesize=letter)
        table_data = [['Buy', 'Sell', 'Hold']]
        for i, row in sorted_df.iterrows():
            table_data.append(list(row))

        table = Table(table_data)
        table_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ])

        table.setStyle(table_style)

        pdf_table = []
        pdf_table.append(table)

        pdf.build(pdf_table)

        with open("nifty_500_recommendation_rsi_strategy.pdf", "rb") as pdf_file:
            data = pdf_file.read()
        st.download_button("Download PDF", data, file_name="nifty_500_recommendation_rsi_strategy.pdf")
