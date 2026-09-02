import streamlit as st

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Carga del Dataset"])
if modulo == "Home":
