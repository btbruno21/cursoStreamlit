import datetime
import streamlit as st

st.text_input("Nome:")

d = st.date_input("Data de nascimento", value=None)
if d:
    st.write("Data selecionada:", d.strftime("%d/%m/%Y"))
