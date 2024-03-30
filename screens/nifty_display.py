import fpdf
import nifty_sort
import streamlit as st
import pandas as pd


def download_pdf_50():
    my_list = nifty_sort.nifty50_sort()
    df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])
    sorted_df = df.sort_values(by='Signal')

    col1, col2, col3 = st.columns(3)

    col1.header("Buy")
    col1.table(sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist())

    col2.header("Sell")
    col2.table(sorted_df[sorted_df['Signal'] == 'Sell']['Stock Name'].tolist())

    col3.header("Hold")
    col3.table(sorted_df[sorted_df['Signal'] == 'Hold']['Stock Name'].tolist())
    # Generate PDF content
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Add headers for each column
    pdf.cell(40, 10, txt="Buy", border=1, align="center")
    pdf.cell(40, 10, txt="Sell", border=1, align="center")
    pdf.cell(40, 10, txt="Hold", border=1, align="center")
    pdf.ln(10)  # New line after headers

    # Get data for each column and write to PDF
    buy_list = sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist()
    sell_list = sorted_df[sorted_df['Signal'] == 'Sell']['Stock Name'].tolist()
    hold_list = sorted_df[sorted_df['Signal'] == 'Hold']['Stock Name'].tolist()

    for stock in buy_list:
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, border=1)
        pdf.ln(6)  # Line break between entries

    for stock in sell_list:
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.cell(40, 6, border=1)
        pdf.ln(6)

    for stock in hold_list:
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.ln(6)

    pdf.output("nifty_50_recommendations.pdf")
    with open("nifty_50_recommendations.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_50_recommendations.pdf")


def download_pdf_200():
    my_list = nifty_sort.nifty200_sort()
    df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])
    sorted_df = df.sort_values(by='Signal')

    col1, col2, col3 = st.columns(3)

    col1.header("Buy")
    col1.table(sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist())

    col2.header("Sell")
    col2.table(sorted_df[sorted_df['Signal'] == 'Sell']['Stock Name'].tolist())

    col3.header("Hold")
    col3.table(sorted_df[sorted_df['Signal'] == 'Hold']['Stock Name'].tolist())
    # Generate PDF content
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Add headers for each column
    pdf.cell(40, 10, txt="Buy", border=1, align='center')
    pdf.cell(40, 10, txt="Sell", border=1, align='center')
    pdf.cell(40, 10, txt="Hold", border=1, align='center')
    pdf.ln(10)  # New line after headers

    # Get data for each column and write to PDF
    buy_list = sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist()
    sell_list = sorted_df[sorted_df['Signal'] == 'Sell']['Stock Name'].tolist()
    hold_list = sorted_df[sorted_df['Signal'] == 'Hold']['Stock Name'].tolist()

    for stock in buy_list:
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, border=1)
        pdf.ln(6)  # Line break between entries

    for stock in sell_list:
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.cell(40, 6, border=1)
        pdf.ln(6)

    for stock in hold_list:
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.ln(6)

    # Generate PDF and set download options
    pdf.output("nifty_200_recommendations.pdf")  # Replace with desired filename
    with open("nifty_200_recommendations.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_200_recommendations.pdf")


def download_pdf_500():
    my_list = nifty_sort.nifty500_sort()
    df = pd.DataFrame(my_list, columns=['Stock Name', 'Signal'])
    sorted_df = df.sort_values(by='Signal')

    col1, col2, col3 = st.columns(3)

    col1.header("Buy")
    col1.table(sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist())

    col2.header("Sell")
    col2.table(sorted_df[sorted_df['Signal'] == 'Sell']['Stock Name'].tolist())

    col3.header("Hold")
    col3.table(sorted_df[sorted_df['Signal'] == 'Hold']['Stock Name'].tolist())
    # Generate PDF content
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Add headers for each column
    pdf.cell(40, 10, txt="Buy", border=1, align='center')
    pdf.cell(40, 10, txt="Sell", border=1, align='center')
    pdf.cell(40, 10, txt="Hold", border=1, align='center')
    pdf.ln(10)  # New line after headers

    # Get data for each column and write to PDF
    buy_list = sorted_df[sorted_df['Signal'] == 'Buy']['Stock Name'].tolist()
    sell_list = sorted_df[sorted_df['Signal'] == 'Sell']['Stock Name'].tolist()
    hold_list = sorted_df[sorted_df['Signal'] == 'Hold']['Stock Name'].tolist()

    for stock in buy_list:
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, border=1)
        pdf.ln(6)  # Line break between entries

    for stock in sell_list:
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.cell(40, 6, border=1)
        pdf.ln(6)

    for stock in hold_list:
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, border=1)
        pdf.cell(40, 6, txt=stock, border=1)
        pdf.ln(6)

    # Generate PDF and set download options
    pdf.output("nifty_500_recommendations.pdf")  # Replace with desired filename
    with open("nifty_500_recommendations.pdf", "rb") as pdf_file:
        data = pdf_file.read()
    st.download_button("Download PDF", data, file_name="nifty_500_recommendations.pdf")
