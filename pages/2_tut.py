import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Название
#Описание
st.title('Заполни пропуски')
st.write('Загрузи свой датафрейм и заполни недостающие значения')

##Шаг 1. Загрузка CSV файла
uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')

if not uploaded_file:
    st.stop()

df = pd.read_csv(uploaded_file)
st.write(df.head(5))

##Шаг 2. Проверка на наличие пропуской в файле 
na_values = df.isna().sum()
na_values = na_values[na_values>0]
if len(na_values) > 0:
    fig, ax = plt.subplots()
    sns.barplot(x=na_values.index, y=na_values.values)
    ax.set_title('Пропуски в столбцах')
    ax.set_ylable('Кол-во пропусков')
    st.pyplot(fig)

    fn='na-graph.png'
    plt.savefig(fn)
    with open(fn, 'rb') as img:
        st.sidebar.download_button(
                label='Скачать график Пропусков', data=img, file_name=fn, mime='image/png')

else:
    st.write('В вашем датасете - нет пропущенных значений!')
    st.stop()

##Шаг 3. Заполнение недостающих значений
df_filled = df.loc[df.isna()].copy()

if len(na_values) > 0:
    button = st.button('Заполнить пропуски')

    if button:
        df_filled = df.loc[df.isna()].copy()

        for col in df_filled.columns:
            if df_filled[col].dtype == 'number':
                df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
            else:
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])

##Шаг 4. Выгрузка финального файла

        st.download_button(label='Скачать CSV файл',
                           data=df_filled.to_csv(),
                           file_name='filled_file.csv')

