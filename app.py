import streamlit as st

from page_1 import page_1
from page_2 import page_2

st.sidebar.markdown('### Настройки')
languages = ['rus', 'eng']
selected_languages = st.sidebar.selectbox('Язык', languages)

# Create a page dropdown 
page = st.sidebar.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"]) 

if page == "Page 1":
    page_1()
elif page == "Page 2":
    page_2()