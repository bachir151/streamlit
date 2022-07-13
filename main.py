import yfinance as yf
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

#st.write("""
# Simple Stock Price App
#Shown are the stock closing price and volume of Google!
#""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#####tickerSymbol = 'GOOGL'
#get data on this ticker
####tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
####tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

####st.line_chart(tickerDf.Close)
#####st.line_chart(tickerDf.Volume)

st.write("""
# Simple Stock Price App
#Shown are the stock closing price and volume of Google!
""")

df = pd.read_excel("C:/Users/bachi/Downloads/pop.xls")

print(df.dtypes)
#df['year']=df['year'].astype(int)
st.dataframe(df['Year'])
st.line_chart(df["Year"])
"""st.line_chart(df)"""

