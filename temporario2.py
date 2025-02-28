import datetime
import streamlit as st

d = st.date_input("Data de nascimento", datetime.date(2025, 2, 28))
st.write("Your birthday is:", d)
