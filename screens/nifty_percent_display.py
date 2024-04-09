from sort import nifty_percent_sort
import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, SimpleDocTemplate, TableStyle


def download_pdf_50_percent():
    my_list = nifty_percent_sort.nifty50_sort_percent()
    df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])

    b = pd.DataFrame(df[df.Signal == 'Buy']['Stock Name'])
    b.columns = ['Buy']
    n = pd.DataFrame(df[df.Signal == 'No Signal']['Stock Name'])
    n.columns = ['No Signal']
    b = b.reset_index()['Buy']
    n = n.reset_index()['No Signal']
    sorted_df = pd.concat([b, n], axis=1).fillna('')
    col1, col2 = st.columns(2)

    col1.header("Buy")
    col1.table(sorted_df['Buy'])
    col2.header("No Signal")
    col2.table(sorted_df['No Signal'])

    pdf = SimpleDocTemplate("nifty_50_recommendation_%strategy.pdf", pagesize=letter)
    table_data = [['Buy', 'No Signal', ]]
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

    with open("nifty_50_recommendation_%strategy.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_50_recommendation_%strategy.pdf")
