import datetime
import streamlit as st

d = st.date_input("Data de nascimento:", value=None)
st.write("Your birthday is:", d)
