import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Carga del Dataset", "EDA"])

def clasificar_variables(df):
    variables_numericas = df.select_dtypes(include="number").columns
    variables_categoricas = df.select_dtypes(include="object").columns
    return variables_numericas, variables_categoricas

class AnalizadorDatos:
    def __init__(self, df):
        self.df = df
    def estadisticas(self):
        return self.df.describe()
    def valores_nulos(self):
        return self.df.isnull().sum()
    def duplicados(self):
        return self.df.duplicated().sum()

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
    analizador = AnalizadorDatos(df)
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
      nulos = pd.DataFrame({"Valores nulos": analizador.valores_nulos()})
      st.dataframe(nulos)
      st.write("**Registros duplicados:**")
      st.write(analizador.duplicados())
          
    with tab2:
      st.subheader("Ítem 2: Clasificación de variables")
      st.write("En este apartado se clasifican las variables del dataset en numéricas y categóricas.")
      variables_numericas, variables_categoricas = clasificar_variables(df)
      st.write("**Variables numéricas:**")
      st.write(list(variables_numericas))
      st.write("**Variables categóricas:**")
      st.write(list(variables_categoricas))
      conteo_tipos = pd.DataFrame({"Tipo de variable": ["Numéricas", "Categóricas"],"Cantidad": [len(variables_numericas), len(variables_categoricas)]})
      st.write("**Cantidad de variables por tipo:**")
      st.dataframe(conteo_tipos) 
        
    with tab3:
      st.subheader("Ítem 3: Estadísticas descriptivas")
      st.write("En este apartado se presentan las principales estadísticas descriptivas de las variables numéricas del dataset.")
      estadisticas = analizador.estadisticas()
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

    with tab5:
      st.subheader("Ítem 5: Distribución de variables numéricas")
      st.write("En este apartado se observa la distribución de las variables numéricas mediante histogramas.")
      variables_numericas = df.select_dtypes(include="number").columns
      variable = st.selectbox("Seleccione una variable:",variables_numericas)
      fig, ax = plt.subplots()
      sns.histplot(df[variable], bins=10, kde=True, ax=ax)
      ax.set_title("Distribución de " + variable)
      ax.set_xlabel(variable)
      ax.set_ylabel("Frecuencia")
      st.pyplot(fig)

    with tab6:
      st.subheader("Ítem 6: Variables categóricas")
      st.write("En este apartado se analiza la frecuencia de las variables categóricas mediante tablas y gráficos.")
      variables_categoricas = df.select_dtypes(include="object").columns
      variable = st.selectbox("Seleccione una variable categórica:",variables_categoricas)
      conteo = df[variable].value_counts().reset_index()
      conteo.columns = ["Categoría", "Cantidad"]
      st.write("**Frecuencia de las categorías:**")
      st.dataframe(conteo)
      st.write("**Gráfico de frecuencias:**")
      st.bar_chart(conteo.set_index("Categoría"))

    with tab7:
      st.subheader("Ítem 7: Numérico vs categórico")
      st.write("En este apartado se comparan variables numéricas según la etiqueta depression_label.")
      variables_numericas = [
          "age",
          "daily_social_media_hours",
          "sleep_hours",
          "screen_time_before_sleep",
          "academic_performance",
          "physical_activity",
          "stress_level",
          "anxiety_level",
          "addiction_level"
      ]
      variable = st.selectbox("Seleccione una variable numérica:",variables_numericas)
      st.write("**Comparación de", variable, "según depression_label:**")
      fig, ax = plt.subplots()
      sns.boxplot(data=df,x="depression_label",y=variable,ax=ax)
      ax.set_xlabel("Depression Label")
      ax.set_ylabel(variable)
      st.pyplot(fig)
        
    with tab8:
      st.subheader("Ítem 8: Categórico vs categórico")
      st.write("En este apartado se analizan las relaciones entre dos variables categóricas.")
      variables_categoricas = ["gender","platform_usage","social_interaction_level","depression_label"]
      variable1 = st.selectbox("Seleccione la primera variable:",variables_categoricas) 
      variable2 = st.selectbox("Seleccione la segunda variable:",variables_categoricas)
      tabla = pd.crosstab(df[variable1], df[variable2])
      st.write("**Tabla de frecuencias:**")
      st.dataframe(tabla)
      st.write("**Gráfico de comparación:**")
      st.bar_chart(tabla)
    with tab9:
     st.subheader("Ítem 9: Análisis dinámico")
     st.write("En este apartado el usuario puede seleccionar parámetros para realizar un análisis personalizado del dataset.")
     col1, col2 = st.columns(2)
     with col1:
       edad = st.slider("Seleccione el rango de edad:", min_value=int(df["age"].min()),max_value=int(df["age"].max()),value=(int(df["age"].min()), int(df["age"].max())))
     with col2:
       generos = st.multiselect( "Seleccione el género:",df["gender"].unique(),default=df["gender"].unique())
     plataformas = st.multiselect("Seleccione la plataforma:", df["platform_usage"].unique(),default=df["platform_usage"].unique())
     variables_numericas = [
          "daily_social_media_hours",
          "sleep_hours",
          "screen_time_before_sleep",
          "academic_performance",
          "physical_activity",
          "stress_level",
          "anxiety_level",
          "addiction_level"
     ]
    variable = st.selectbox("Seleccione una variable para analizar:",variables_numericas)
    mostrar_datos = st.checkbox("Mostrar datos filtrados",value=True)
    df_filtrado = df[(df["age"] >= edad[0]) &(df["age"] <= edad[1]) &(df["gender"].isin(generos)) &(df["platform_usage"].isin(plataformas))]
    st.write("**Cantidad de registros:**")
    st.write(len(df_filtrado))
    if mostrar_datos:
        st.write("**Datos filtrados:**")
        st.dataframe(df_filtrado)
    st.write("**Gráfico de la variable seleccionada:**")
    fig, ax = plt.subplots()
    sns.histplot(df_filtrado[variable], bins=10, kde=True, ax=ax)
    ax.set_title("Distribución de " + variable)
    ax.set_xlabel(variable)
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)
        
    with tab10:
      st.subheader("Ítem 10: Hallazgos clave")
      st.write("En este apartado se presentan los principales hallazgos obtenidos durante el análisis exploratorio del dataset.")
      st.write("**1. Uso de redes sociales**")
      promedio_redes = df["daily_social_media_hours"].mean()
      st.write(f"El promedio de uso diario de redes sociales es de {promedio_redes:.2f} horas.")
      st.write("**2. Horas de sueño**")
      promedio_sueno = df["sleep_hours"].mean()
      st.write(f"El promedio de horas de sueño es de {promedio_sueno:.2f} horas por día.")
      st.write("**3. Rendimiento académico**")
      promedio_academico = df["academic_performance"].mean()
      st.write( f"El promedio del rendimiento académico es de {promedio_academico:.2f}.")
      st.write("**4. Nivel de estrés**")
      promedio_estres = df["stress_level"].mean()
      st.write( f"El nivel promedio de estrés registrado es de {promedio_estres:.2f} sobre 10.")
      st.write("**5. Plataforma más utilizada**")
      plataforma_mas_usada = df["platform_usage"].value_counts().idxmax()
      st.write( f"La plataforma o combinación de plataformas con mayor frecuencia es: {plataforma_mas_usada}.")
