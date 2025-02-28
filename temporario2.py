import datetime
import streamlit as st
st.text_input("Nome:",key="i_1", max_chars=50)

st.text_input("CPF:",key="i_2", max_chars=11)

d = st.date_input("Data de nascimento", value=None)
if d:
    st.write("Data selecionada:", d.strftime("%d/%m/%Y"))
