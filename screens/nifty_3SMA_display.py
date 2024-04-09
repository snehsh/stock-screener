from sort import nifty_3SMA_sort
import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def download_pdf_50_3SMA():
    my_list = nifty_3SMA_sort.nifty50_sort_3SMA()
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

    pdf = SimpleDocTemplate("nifty_50_recommendation_3SMA.pdf", pagesize=letter)
    table_data = []
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

    with open("nifty_50_recommendation_3SMA.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_50_recommendation_3SMA.pdf")


def download_pdf_200_3SMA():
    my_list = nifty_3SMA_sort.nifty200_sort_3SMA()
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

    pdf = SimpleDocTemplate("nifty_200_recommendation_3SMA", pagesize=letter)
    table_data = []
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

    with open("nifty_200_recommendation_3SMA.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_200_recommendation_3SMA.pdf")


def download_pdf_500_3SMA():
    my_list = nifty_3SMA_sort.nifty500_sort_3SMA()
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

    pdf = SimpleDocTemplate("nifty_500_recommendation_3SMA.pdf", pagesize=letter)
    table_data = []
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

    with open("nifty_500_recommendation_3SMA.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_500_recommendation_3SMA.pdf")
