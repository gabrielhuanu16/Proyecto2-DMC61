import streamlit as st

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Carga del Dataset"])
if modulo == "Home":
  st.title("Modulo 2 - Análisis Exploratorio de Datos sobre Salud Mental en Adolescentes")
  st.image("gabriel_logo.png", width=200)
  st.subheader("Elaborado por: Fabricio Gabriel Huánuco Rivero")
  st.subheader("Teen Mental Health Dataset – Proyecto Aplicado")
  st.divider()
  st.write("**Información General**")
  st.markdown("""
  - Carrera Profesional: Ingenieria de Sistemas e Informatica
  - Universidad: Universidad Continental
  - Ciclo: 6to
  - Especialización: Python for Analytics
  - Año: 2026
  """)
  st.divider()
  st.write("**Descripción del Proyecto**")
  st.write("Este proyecto consiste en realizar un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos relacionado con hábitos digitales, descanso, actividad física, interacción social y variables de bienestar en adolescentes. Mediante Python y Streamlit se realizará la limpieza, transformación, exploración y visualización de los datos con el objetivo de identificar patrones y relaciones relevantes dentro del dataset.")
  st.write("**¿Qué contiene el dataset?**")
  st.write("El dataset contiene 1,200 registros correspondientes a adolescentes de entre 13 y 19 años y cuenta con 13 variables. La información incluye edad, género, uso diario de redes sociales, plataforma utilizada, horas de sueño, tiempo de pantalla antes de dormir, rendimiento académico, actividad física, interacción social y escalas de estrés, ansiedad y dependencia. También contiene una etiqueta denominada depression_label, utilizada únicamente como variable de análisis exploratorio.")
  st.divider()
  st.write("**Tecnologías Utilizadas**")
  st.markdown("""
  - Python
  - Streamlit
  - GitHub
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  """)
