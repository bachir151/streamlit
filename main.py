import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
#Shown are the stock closing price and volume of Google!
""")

df = pd.read_excel("pop.xls")

st.dataframe(df['Year'])
st.line_chart(df["Year"])


