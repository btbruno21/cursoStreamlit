import streamlit as st

with st.container():
    st.header("Ingredientes para o Bolo de Leite Condensado")
    
    latas_leite_condensado = st.number_input("Quantidade de latas de leite condensado necessárias para a receita:")
    gramas_por_lata = st.number_input("Digite a quantidade de gramas que cada lata de leite condensado tem:")
    quantidade_xicaras_f = st.number_input("Quantidade de xícaras de farinha necessárias para a receita:")
    gramas_por_xicara_f = st.number_input("Digite a quantidade de gramas que cada xícara de farinha tem:")
    quantidade_ovos = st.number_input("Quantidade de ovos necessários para a receita:")

    st.subheader("Ingredientes recebidos:")
    st.write(f"Latas de leite condensado: {latas_leite_condensado} latas ({latas_leite_condensado * gramas_por_lata}g)")
    st.write(f"Farinha de trigo: {quantidade_xicaras_f} xícaras ({quantidade_xicaras_f * gramas_por_xicara_f}g)")
    st.write(f"Ovos: {quantidade_ovos} ovos")
