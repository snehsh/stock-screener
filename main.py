import streamlit as st
from screens import nifty_3SMA_display, individual_stock_analysis_display, nifty_percent_display


def main():
    st.title("Stock Screener")
    st.write("Welcome to Stock Screener")

    analysis_options = ["Individual Stock Analysis", "Nifty Buy/Sell/Hold Calls"]
    selected_analysis_option = st.radio("What would you like to do?", analysis_options)
    if selected_analysis_option == "Individual Stock Analysis":
        indicator_options_individual=["3-SMA Strategy", "30% down from all time high"]
        selected_individual_indicator_option = st.selectbox("Choose an Indicator", indicator_options_individual)
        if selected_individual_indicator_option == "3-SMA Strategy":
            individual_stock_analysis_display.sma3_strategy_display()
        elif selected_individual_indicator_option == "30% down from all time high":
            individual_stock_analysis_display.percent_strategy_display()

    elif selected_analysis_option == "Nifty Buy/Sell/Hold Calls":
        indicator_options_nifty=["3-SMA Strategy", "30% down from all time high"]
        selected_nifty_indicator_option = st.selectbox("Choose an indicator", indicator_options_nifty)
        nifty_category_options = ["Nifty 50 Analysis", "Nifty 200 Analysis", "Nifty 500 Analysis"]
        if selected_nifty_indicator_option == "3-SMA Strategy":
            selected_nifty_option_3SMA = st.selectbox("Choose a Category", nifty_category_options)
            if selected_nifty_option_3SMA == "Nifty 50 Analysis":
                if st.button("Analyze"):
                    nifty_3SMA_display.download_pdf_50_3SMA()
            elif selected_nifty_option_3SMA == "Nifty 200 Analysis":
                if st.button("Analyze"):
                    nifty_3SMA_display.download_pdf_200_3SMA()
            elif selected_nifty_option_3SMA == "Nifty 500 Analysis":
                if st.button("Analyze"):
                    nifty_3SMA_display.download_pdf_500_3SMA()
        elif selected_nifty_indicator_option == "30% down from all time high":
            selected_nifty_option_percent = st.selectbox("Choose a Category", nifty_category_options)
            if selected_nifty_option_percent == "Nifty 50 Analysis":
                if st.button("Analyze"):
                    nifty_percent_display.download_pdf_50_percent()
            elif selected_nifty_option_percent == "Nifty 200 Analysis":
                if st.button("Analyze"):
                    nifty_percent_display.download_pdf_200_percent()
            elif selected_nifty_option_percent == "Nifty 500 Analysis":
                if st.button("Analyze"):
                    nifty_percent_display.download_pdf_500_percent()




if __name__ == "__main__":
    main()
