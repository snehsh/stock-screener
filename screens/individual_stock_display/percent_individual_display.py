import streamlit as st
from nifty_data import nse_stocks_list
from stock_data.dividend import DividendData
from indicators.percent_strategy import PercentStrategy
from stock_data.balance_sheet import BalanceSheet
from stock_data.income_statement import IncomeStatement
from stock_data.cash_flow import CashFlow
from graphs.percent_graph import PercentGraph


def percent_strategy_display():
    ticker_symbol = st.selectbox(":orange[Enter Stock Ticker Symbol:]", nse_stocks_list.display_list_nifty50)
    usable_ticker = ticker_symbol.upper() + ".NS"
    select_percent = st.slider(":orange[Select percentage of your choice:]", 0, 100, 1,
                               key="individual_percentage slider")
    st.write(f"Selected Percentage: {select_percent}")
    if st.button("Analyze"):
        stock_analyzer = PercentStrategy(usable_ticker, select_percent)
        signal, rounded_percent_diff = stock_analyzer.percent_strategy()
        st.header(f":green[{ticker_symbol.upper()}]")
        st.subheader(f":orange[Current Signal:] {signal}")
        tab1, tab2, tab3, tab4 = st.tabs(["Graph", "Income Statement(P&L)", "Balance Sheet", "Additional Info"])

        with tab1:
            plot_graph = PercentGraph(usable_ticker)
            st.write(f"The stock is {rounded_percent_diff}% down from all time high.")
            image_data = plot_graph.plot_data_percent()
            st.image(image_data, use_column_width=True)

        with tab2:
            tab2_1, tab2_2 = st.tabs(["Yearly", "Quarterly"])
            with tab2_1:
                enter_income_statement = IncomeStatement(usable_ticker)
                get_income_statement = enter_income_statement.income_statement_yearly()

                st.subheader(":orange[Income Statement(P&L)]")
                st.dataframe(get_income_statement)

            with tab2_2:
                enter_income_statement = IncomeStatement(usable_ticker)
                get_income_statement = enter_income_statement.income_statement_quarterly()

                st.subheader(":orange[Income Statement(P&L)]")
                st.dataframe(get_income_statement)

        with tab3:
            tab3_1, tab3_2 = st.tabs(["Yearly", "Quarterly"])
            with tab3_1:
                enter_balance_sheet = BalanceSheet(usable_ticker)
                get_balance_sheet = enter_balance_sheet.balance_sheet_yearly()
                st.subheader(":orange[Balance Sheet]")
                st.dataframe(get_balance_sheet)
            with tab3_2:
                enter_balance_sheet = BalanceSheet(usable_ticker)
                get_balance_sheet = enter_balance_sheet.balance_sheet_quarterly()
                st.subheader(":orange[Balance Sheet]")
                st.dataframe(get_balance_sheet)

        with tab4:
            dividend_data = DividendData(usable_ticker)
            latest_dividend_date, latest_dividend_amount = dividend_data.dividends()
            st.subheader(":orange[Dividend Details:]")

            if latest_dividend_date == "NA":
                st.write(f"Latest Dividend Date: {latest_dividend_date}")
            else:
                st.write(f"Latest Dividend Date: {latest_dividend_date.strftime('%Y-%m-%d')}")

            st.write(f"Latest Dividend Amount: {latest_dividend_amount}")

            st.subheader(":orange[Cashflow Details:]")
            st.write("Yearly Cashflow:")
            enter_cash_flow = CashFlow(usable_ticker)
            get_yearly_cash_flow = enter_cash_flow.cash_flow_yearly()
            if get_yearly_cash_flow.empty:
                st.write("NA")
            else:
                st.dataframe(get_yearly_cash_flow)
            st.write("Quarterly Cashflow:")
            get_quarterly_cash_flow = enter_cash_flow.cash_flow_quarterly()
            if get_quarterly_cash_flow.empty:
                st.write("NA")
            else:
                st.dataframe(get_quarterly_cash_flow)
