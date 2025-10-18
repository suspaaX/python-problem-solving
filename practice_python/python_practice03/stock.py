import yfinance as yf
import streamlit as st
import pandas as pd

st.write ("""
### Simple Stock Price App

shown are the stock ***closing*** and **volume** of Google!

""")


tickerSymbol = 'GOOGL'
#get data  in this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the histroical prices for this ticker
tickerDf = tickerData.history(period= 'id',start='2010-5-31',end='2020-5-31')
#open high low close volume dividends stock splits


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)