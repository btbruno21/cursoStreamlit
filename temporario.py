import streamlit as st
import pandas as pd

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
  ['Verde','Amarelo','Vermelho','Azul'])

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')

st.color_picker("Pick a Color", "#00f900")
st.feedback("stars")

df = pd.DataFrame(
  [
    {"command": "st.selectbox", "rating":4, "is_widget":True},
    {"command": "st.ballons", "rating":5, "is_widget":False},
    {"command": "st.time_input", "rating":3, "is_widget":True},
  ]
)
edited_df = st.data_editor(df)

class BalloonsMixin:
    @gather_metrics("balloons")
    def balloons(self) -> DeltaGenerator:
        """Draw celebratory balloons.

        Example
        -------
        >>> import streamlit as st
        >>>
        >>> st.balloons()

        ...then watch your app and get ready for a celebration!

        """
        balloons_proto = BalloonsProto()
        balloons_proto.show = True
        return self.dg._enqueue("balloons", balloons_proto)

    @property
    def dg(self) -> DeltaGenerator:
        """Get our DeltaGenerator."""
        return cast("DeltaGenerator", self)
