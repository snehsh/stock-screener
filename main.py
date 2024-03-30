import streamlit as st
from screens import nifty_display, individual_stock_display


def main():
    st.title("Stock Screener")
    st.write("Welcome to Stock Screener")

    options = ["Individual Stock Analysis", "Nifty 50 Analysis", "Nifty 200 Analysis", "Nifty 500 Analysis"]
    selected_option = st.radio("What would you like to do?", options)
    if selected_option == "Individual Stock Analysis":
        individual_stock_display.individual_stock_display()

    elif selected_option == "Nifty 50 Analysis":
        if st.button("Analyze"):
            nifty_display.download_pdf_50()

    elif selected_option == "Nifty 200 Analysis":
        if st.button("Analyze"):
            nifty_display.download_pdf_200()

    elif selected_option == "Nifty 500 Analysis":
        if st.button("Analyze"):
            nifty_display.download_pdf_500()


if __name__ == "__main__":
    main()
