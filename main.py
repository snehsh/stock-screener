import streamlit as st
from screens import nifty_3SMA_display, individual_stock_analysis_display, nifty_percent_display


def main():
    tab1, tab2, tab3 = st.tabs(["Home", "Individual Stock Analysis", "Index Analysis"])
    with tab1:
        st.header("Stock Screener")
        st.write("Welcome to Stock Screener")
        st.image("images/Intro.jpg", width=800)

    with tab2:
        st.header("Individual Stock Analysis")
        st.write("Analyze individual stocks to get Buy,Sell or Hold signals based on various indicators")
        indicator_options_individual = ["3-SMA Strategy", "30% down from all time high"]
        selected_individual_indicator_option = st.selectbox("Choose an Indicator", indicator_options_individual)
        if selected_individual_indicator_option == "3-SMA Strategy":
            individual_stock_analysis_display.sma3_strategy_display()
        elif selected_individual_indicator_option == "30% down from all time high":
            individual_stock_analysis_display.percent_strategy_display()

    with tab3:
        st.header("Index Analysis")
        st.write("Analyze an entire lot of stocks belonging to a particular index based on various indicators")
        indicator_options_nifty = ["3-SMA Strategy", "30% down from all time high"]
        selected_nifty_indicator_option = st.selectbox("Choose an indicator", indicator_options_nifty)
        if selected_nifty_indicator_option == "3-SMA Strategy":
            nifty_category_options_3SMA = ["Nifty 50 Analysis", "Nifty 200 Analysis", "Nifty 500 Analysis"]
            selected_nifty_option_3SMA = st.selectbox("Choose a Category", nifty_category_options_3SMA)
            if st.button("Analyze Stocks"):
                if selected_nifty_option_3SMA == "Nifty 50 Analysis":
                    nifty_3SMA_display.download_pdf_50_3SMA()
                elif selected_nifty_option_3SMA == "Nifty 200 Analysis":
                    nifty_3SMA_display.download_pdf_200_3SMA()
                elif selected_nifty_option_3SMA == "Nifty 500 Analysis":
                    nifty_3SMA_display.download_pdf_500_3SMA()
        elif selected_nifty_indicator_option == "30% down from all time high":
            nifty_category_options_percent = ["Nifty 50 Analysis"]
            selected_nifty_option_percent = st.selectbox("Choose a Category", nifty_category_options_percent)
            if st.button("Analyze Stocks"):
                if selected_nifty_option_percent == "Nifty 50 Analysis":
                    nifty_percent_display.download_pdf_50_percent()


if __name__ == "__main__":
    main()
