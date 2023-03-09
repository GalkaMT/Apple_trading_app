import yfinance as yf
import streamlit as st
import pandas as pd


tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2022-01-01')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.header(":red[Данные о суточных котировках компании Apple (с 01.01.2022)] :apple:")

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.1, 1, 0.1, 1, 0.1))
with row0_1:
    st.subheader(':orange[Цена открытия _(Open)_:city_sunrise:]')
    st.line_chart(tickerDf[['Open']])


with row0_2:
    st.subheader(':orange[Цена закрытия _(Close)_:city_sunset:]')
    st.line_chart(tickerDf[['Close']])


row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.columns((0.1, 1, 0.1, 1, 0.1))
with row1_1:
    st.subheader(':orange[Минимальная цена _(Low)_:fearful:]')
    st.line_chart(tickerDf[['Low']])

with row1_2:
    st.subheader(':orange[Максимальная цена _(High)_:muscle:]')
    st.line_chart(tickerDf[['High']])


st.subheader("""Тренд цены и объёма - PVT ***(Volume)*** :cake:""")
st.line_chart(tickerDf.Volume)


