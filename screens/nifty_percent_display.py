import fpdf
from sort import nifty_percent_sort
import streamlit as st
import pandas as pd


def download_pdf_50_percent():

    my_list = nifty_percent_sort.nifty50_sort_percent()
    df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])
    sorted_df = df.sort_values(by='Signal')
    col1,col2 = st.columns(2)

    col1.header("Buy")
    col1.table(sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist())
    col2.header("No Signal")
    col2.table(sorted_df[sorted_df['Signal'] == 'No Signal']['Stock Name'].tolist())

    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(40, 10, txt="Buy", border=1, align='center')
    pdf.ln(10)

    buy_list = sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist()

    for stock in buy_list:
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.ln(6)

    pdf.output("nifty_50_recommendations_percent_analysis.pdf")
    with open("nifty_50_recommendations_percent_analysis.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_50_recommendations_percent_analysis.pdf")


def download_pdf_200_percent():
    my_list = nifty_percent_sort.nifty200_sort_percent()
    df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])
    sorted_df = df.sort_values(by='Signal')

    col1 = st.columns(1)

    col1.header("Buy")
    col1.table(sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist())

    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(40, 10, txt="Buy", border=1, align='center')
    pdf.ln(10)

    buy_list = sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist()

    for stock in buy_list:
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.ln(6)

    pdf.output("nifty_200_recommendations_percent_analysis.pdf")
    with open("nifty_200_recommendations_percent_analysis.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_200_recommendations_percent_analysis.pdf")


def download_pdf_500_percent():
    my_list = nifty_percent_sort.nifty500_sort_percent()
    df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])
    sorted_df = df.sort_values(by='Signal')

    col1 = st.columns(1)

    col1.header("Buy")
    col1.table(sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist())

    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(40, 10, txt="Buy", border=1, align='center')
    pdf.ln(10)

    buy_list = sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist()

    for stock in buy_list:
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.ln(6)

    pdf.output("nifty_500_recommendations_percent_analysis.pdf")
    with open("nifty_500_recommendations.pdf_percent_analysis", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_500_recommendations_percent_analysis.pdf")
