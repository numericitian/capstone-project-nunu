import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(layout = "wide")

tickerAAPL = yf.Ticker("AAPL")
tickerDfAAPL = tickerAAPL.history(period = "1mo")

tickerGOOGL = yf.Ticker("GOOGL")
tickerDfGOOGL = tickerAAPL.history(period = "1mo")

with st.sidebar:
    st.title("Stock Price")
    
    title1 = st.radio("Pick Stock 1", ["GOOGL", "AAPL", "TSLA"])
    title2 = st.radio("Pick Stock 2", ["GOOGL", "AAPL", "TSLA"])
    
    tickerSymbol_text = st.text_input("Enter Ticker")
    tickerData = yf.Ticker(tickerSymbol_text)
    select_period = st.select_slider("Select period", ["1d", "5d", "1mo"])

tickerDf = tickerData.history(period = select_period)

c1, c2 = st.columns(2)

with c1:
    st.header(title1)
    st.line_chart(tickerDfAAPL['Close'])
    
with c2:
    st.header(title2)
    st.line_chart(tickerDfGOOGL['Close'])

st.line_chart(tickerDf['Close'])
st.dataframe(tickerDf)
