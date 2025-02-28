import datetime
import streamlit as st

print("Cadastro de Aluno")

st.text_input("Nome:",key="i_1", max_chars=50)

st.text_input("CPF:",key="i_2", max_chars=11)

st.text_input("Email:", key="i_3", max_chars=30)

st.text_input("Telefone:",key="i_4", max_chars=11)

d = st.date_input("Data de nascimento", value=None)
if d:
    st.write("Data selecionada:", d.strftime("%d/%m/%Y"))
