import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

df = pd.read_csv("store - store.csv")

st.title('Ini Dashboard Latihan')

st.metric("Sales", 100, "-4%")

st.write('Hello World')

st.caption('Semua orang bisa bikin dashboard')

st.code('import streamlit as st')

"Nama saya Nunu"

st.header('Ini Chart Sales')

st.line_chart(df['Sales'])

st.bar_chart(df['Quantity'])

st.dataframe(df)

