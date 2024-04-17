import streamlit as st
from screens import nifty_SMA3_display, individual_stock_analysis_display, nifty_percent_display


def main():
    tab1, tab2, tab3 = st.tabs(["Home", "Individual Stock Analysis", "Index Analysis"])
    with tab1:
        st.header(":orange[Stock Screener]")
        st.write("Welcome to Stock Screener")
        st.image("images/Intro.jpg", use_column_width=True)

    with tab2:
        st.header(":orange[Individual Stock Analysis]")
        st.write("Analyze individual stocks to get Buy,Sell or Hold signals based on various indicators")
        indicator_options_individual = ["3-SMA Strategy", "Percentage Strategy"]
        selected_individual_indicator_option = st.selectbox(":orange[Choose an Indicator]", indicator_options_individual)
        if selected_individual_indicator_option == "3-SMA Strategy":
            st.write("This indicator gives 'Buy','Sell' and 'Hold' signals based on the below given conditions:")
            st.write(
                ":violet[Buy Call:] :blue[When the order of moving averages from bottom to top is 20,50,200 and the current "
                "price is below the 20 level.]")
            st.write(":violet[Sell Call:] :blue[When the order of moving averages from bottom to top "
                     "is 200,50,20 and the current price is above the 20 level]")
            st.write(":violet[Hold Call:] :blue[In all other possible scenarios]")
            individual_stock_analysis_display.sma3_strategy_display()
        elif selected_individual_indicator_option == "Percentage Strategy":
            st.write(
                "This strategy is a personalized one. You have to choose a percentage of your choice as a reference, "
                "If the current price is below the reference percentage from all time high then indicator "
                "will show a 'Buy' signal.")
            st.write(" For Example: If you Choose 40%, the indicator will show a buy sign if the "
                     "current stock price is more than 40% down from all time high.")
            individual_stock_analysis_display.percent_strategy_display()

    with tab3:
        st.header(":orange[Index Analysis]")
        st.write("Analyze an entire lot of stocks belonging to a particular index based on various indicators")
        tab3_1, tab3_2, tab3_3 = st.tabs(["Nifty 50", "Nifty 200", "Nifty 500"])

        with tab3_1:
            indicator_options_nifty = ["3-SMA Strategy", "Percentage Strategy"]
            selected_nifty_indicator_option = st.selectbox(":orange[Choose an Indicator:]", indicator_options_nifty,
                                                           key="tab3_1_select")
            if selected_nifty_indicator_option == "3-SMA Strategy":
                st.write("This indicator gives 'Buy','Sell' and 'Hold' signals based on the below given conditions:")
                st.write(
                    ":violet[Buy Call:] :blue[When the order of moving averages from bottom to top is 20,50,200 and the current "
                    "price is below the 20 level.]")
                st.write(":violet[Sell Call:] :blue[When the order of moving averages from bottom to top "
                         "is 200,50,20 and the current price is above the 20 level]")
                st.write(":violet[Hold Call:] :blue[In all other possible scenarios]")
                if st.button("Analyze Stocks", key="tab3_1_button"):
                    nifty_SMA3_display.download_pdf_50_3SMA()
            elif selected_nifty_indicator_option == "Percentage Strategy":
                st.write(
                    "This startegy is a personalized one. You have to choose a percentage of your choice as a "
                    "reference,"
                    "all stocks whose current price is below the reference percentage from all time will have a 'Buy' signal.")
                st.write("For Example: If you Choose 40%, then all stocks whose current price is more that 40% down from all time high "
                         "will be displayed.")
                nifty_percent_display.download_pdf_50_percent()

        with tab3_2:
            indicator_options_nifty = ["3-SMA Strategy"]
            selected_nifty_indicator_option = st.selectbox(":orange[Choose an Indicator:]", indicator_options_nifty,
                                                           key="tab3_2_select")
            if selected_nifty_indicator_option == "3-SMA Strategy":
                st.write("This indicator gives 'Buy','Sell' and 'Hold' signals based on the below given conditions:")
                st.write(
                    ":violet[Buy Call:] :blue[When the order of moving averages from bottom to top is 20,50,200 and the current "
                    "price is below the 20 level.]")
                st.write(":violet[Sell Call:] :blue[When the order of moving averages from bottom to top "
                         "is 200,50,20 and the current price is above the 20 level]")
                st.write(":violet[Hold Call:] :blue[In all other possible scenarios]")
                if st.button("Analyze Stocks", key="tab3_2_button"):
                    nifty_SMA3_display.download_pdf_200_3SMA()

        with tab3_3:
            indicator_options_nifty = ["3-SMA Strategy"]
            selected_nifty_indicator_option = st.selectbox(":orange[Choose an Indicator:]", indicator_options_nifty,
                                                           key="tab3_3_select")
            if selected_nifty_indicator_option == "3-SMA Strategy":
                st.write("This indicator gives 'Buy','Sell' and 'Hold' signals based on the below given conditions:")
                st.write(":violet[Buy Call:] :blue[When the order of moving averages from bottom to top is 20,50,200 and the current "
                         "price is below the 20 level.]")
                st.write(":violet[Sell Call:] :blue[When the order of moving averages from bottom to top "
                         "is 200,50,20 and the current price is above the 20 level]")
                st.write(":violet[Hold Call:] :blue[In all other possible scenarios]")
                if st.button("Analyze Stocks", key="tab3_3_button"):
                    nifty_SMA3_display.download_pdf_500_3SMA()


if __name__ == "__main__":
    main()
