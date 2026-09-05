import streamlit as st
import pandas as pd

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Carga del Dataset", "EDA"])

def clasificar_variables(df):
    variables_numericas = df.select_dtypes(include="number").columns
    variables_categoricas = df.select_dtypes(include="object").columns
    return variables_numericas, variables_categoricas

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
elif modulo == "Carga del Dataset":
  st.title("Carga del Dataset")
  st.divider()
  st.write("**Seleccione el archivo CSV que desea analizar:**")
  archivo = st.file_uploader("Cargar Teen_Mental_Health_Dataset.csv",type=["csv"])
  if archivo is not None:
    df = pd.read_csv(archivo)
    st.session_state.df = df
  if "df" in st.session_state:
    df = st.session_state.df
    st.success("Dataset cargado correctamente")
    st.write("Vista previa del dataset")
    st.dataframe(df.head())
    st.write("Cantidad de filas:", df.shape[0])
    st.write("Cantidad de columnas:", df.shape[1])
  else:
    st.warning("Debe cargar el archivo CSV")
elif modulo == "EDA":
  st.title("EDA")
  st.divider()
  if "df" not in st.session_state:
    st.warning("Primero debe cargar el dataset.")
  else:
    df = st.session_state.df
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
          "Información general",
          "Clasificación",
          "Estadísticas",
          "Valores faltantes",
          "Distribuciones",
          "Variables categóricas",
          "Numérico vs categórico",
          "Categórico vs categórico",
          "Análisis dinámico",
          "Hallazgos clave"])
    
    with tab1:
      st.subheader("Ítem 1: Información general del dataset")
      st.write("En este apartado se muestra información general sobre la estructura del dataset, los tipos de datos, los valores nulos y los registros duplicados.")
      st.write("**Información general:**")
      df.info()
      st.write("**Tipos de datos:**")
      tipos = pd.DataFrame({"Tipo de dato": df.dtypes.astype(str)})
      st.dataframe(tipos)
      st.write("**Valores nulos:**")
      nulos = pd.DataFrame({"Valores nulos": df.isnull().sum()})
      st.dataframe(nulos)
      st.write("**Registros duplicados:**")
      st.write(df.duplicated().sum())
  
    with tab2:
      st.subheader("Ítem 2: Clasificación de variables")
      st.write("En este apartado se clasifican las variables del dataset en numéricas y categóricas.")
      tipos_variables = df.dtypes.astype(str).reset_index()
      tipos_variables.columns = ["Variable", "Tipo"]
      conteo_tipos = tipos_variables["Tipo"].value_counts().reset_index()
      conteo_tipos.columns = ["Tipo de variable", "Cantidad"]
      st.dataframe(tipos_variables)
      st.write("**Cantidad de variables por tipo:**")
      st.dataframe(conteo_tipos) 
        
    with tab3:
      st.subheader("Ítem 3: Estadísticas descriptivas")
      st.write("En este apartado se presentan las principales estadísticas descriptivas de las variables numéricas del dataset.")
      estadisticas = df.describe()
      st.dataframe(estadisticas)
      st.write("**Detección preliminar de valores atípicos:**")
      Q1 = df.quantile(0.25, numeric_only=True)
      Q3 = df.quantile(0.75, numeric_only=True)
      IQR = Q3 - Q1
      limite_inferior = Q1 - 1.5 * IQR
      limite_superior = Q3 + 1.5 * IQR
      outliers = ((df.select_dtypes(include="number") < limite_inferior) | (df.select_dtypes(include="number") > limite_superior)).sum()
      conteo_outliers = outliers.reset_index()
      conteo_outliers.columns = ["Variable", "Cantidad de outliers"]
      st.dataframe(conteo_outliers)
    with tab4:
      st.subheader("Ítem 4: Valores faltantes")
      st.write("En este apartado se identifican los valores faltantes del dataset y se muestra su porcentaje por variable.")
      valores_nulos = df.isnull().sum()
      porcentaje_nulos = (df.isnull().sum() / len(df)) * 100
      tabla_nulos = pd.DataFrame({"Variable": df.columns,"Valores nulos": valores_nulos,"Porcentaje (%)": porcentaje_nulos})
      st.dataframe(tabla_nulos)
      st.write("**Valores nulos por variable:**")
      st.bar_chart(valores_nulos)
      if valores_nulos.sum() == 0:
          st.success("El dataset no presenta valores faltantes.")
      else:
          st.warning("El dataset presenta valores faltantes que deben ser revisados.")
    
    
