import streamlit as st

with st.container():
    st.header("Ingredientes para o Bolo de Leite Condensado")
    
    latas_leite_condensado = float(st.text_input("Quantidade de latas de leite condensado necessárias para a receita:","0.0"))
    gramas_por_lata = float(st.text_input("Digite a quantidade de gramas que cada lata de leite condensado tem:","0.0"))
    quantidade_xicaras_f = float(st.text_input("Quantidade de xícaras de farinha necessárias para a receita:","0.0"))
    gramas_por_xicara_f = float(st.text_input("Digite a quantidade de gramas que cada xícara de farinha tem:","0.0"))
    quantidade_ovos = float(st.text_input("Quantidade de ovos necessários para a receita:","0.0"))

    st.subheader("Ingredientes recebidos:")
    st.write(f"Latas de leite condensado: {latas_leite_condensado} latas ({latas_leite_condensado * gramas_por_lata}g)")
    st.write(f"Farinha de trigo: {quantidade_xicaras_f} xícaras ({quantidade_xicaras_f * gramas_por_xicara_f}g)")
    st.write(f"Ovos: {quantidade_ovos} ovos")
