import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Tips')

# Название
st.title('Tutorial data-science app from elbrus-bootcamp')
st.write('Загружаем dataset tips.csv и визуальзируем его')

path = './datasets/updated-tips.csv'
tips_df = pd.read_csv(path)

plot = sns.displot(data=tips_df, x='total_bill')
plot.fig.suptitle('Распределение суммы счета клиентов')
st.pyplot(plot.fig)

fn='tips-displot.png'
plt.savefig(fn)
with open(fn, 'rb') as img:
    st.sidebar.download_button(
            label='Скачать график Распеределения', data=img, file_name=fn, mime='image/png')


plot = sns.catplot(data=tips_df, x='day', y='total_bill', hue='time', kind='boxen')
plot.fig.suptitle('Зависимость счета клиента от дня недели и времени')
st.pyplot(plot.fig)

fn='tips-boxen.png'
plt.savefig(fn)
with open(fn, 'rb') as img:
    st.sidebar.download_button(
            label='Скачать график Зависимостей', data=img, file_name=fn, mime='image/png')


