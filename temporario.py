import streamlit as st

st.button("Botão Salvar")
st.toggle("Toggle")
st.header("link")
st.text_area("Insira texto")
st.text_input("")
st.selectbox(
  'Qual a sua cor favorita?',
  ('Azul','Vermelho','Verde'))
st.multiselect(
  'Quais são suas cores favoritas?',
  ['Verde','Amarelo','Vermelho','Azul'],
  ['Amarelo','Vermelho'])

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')
