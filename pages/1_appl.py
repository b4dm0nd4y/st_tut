import streamlit as st
import yfinance as yf

st.set_page_config(page_title='Appl')

# Название
st.title('Tutorial data-science app from elbrus-bootcamp')
st.write('Показывает информацию о котировках компании Apple')
# Описание


## 1. Берем данные компании Apple
ticker_symbol = 'AAPL'
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(
    period='1d', start='2010-5-31', end='2020-5-31'
)

## 2. Выводим данные на экран
st.write('''
## Closing price
''')
st.line_chart(ticker_df.Close)

st.write('''
## Volume price
''')
st.line_chart(ticker_df.Volume)

