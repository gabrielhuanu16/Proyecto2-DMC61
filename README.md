# Proyecto2-DMC61
# Teen Mental Health Dataset

## Descripción

Este proyecto consiste en realizar un análisis exploratorio de datos sobre un dataset relacionado con la salud mental y los hábitos de adolescentes.

Se analizan datos como el uso de redes sociales, horas de sueño, actividad física, interacción social, rendimiento académico y niveles de estrés, ansiedad y dependencia.

El proyecto fue desarrollado utilizando Python y Streamlit.

## Objetivos

* Conocer la información general del dataset.
* Clasificar las variables.
* Obtener estadísticas descriptivas.
* Revisar valores faltantes y datos duplicados.
* Crear gráficos para analizar las variables.
* Comparar diferentes variables del dataset.
* Realizar filtros para hacer un análisis más específico.
* Encontrar algunos resultados importantes a partir de los datos.

## Dataset

El archivo utilizado es:

Teen_Mental_Health_Dataset.csv

El dataset tiene 1,200 registros y 13 variables. Los datos corresponden a adolescentes entre 13 y 19 años.

Las principales variables son:

| Variable                 | Descripción                           |
| ------------------------ | ------------------------------------- |
| age                      | Edad                                  |
| gender                   | Género                                |
| daily_social_media_hours | Horas de uso diario de redes sociales |
| platform_usage           | Plataforma utilizada                  |
| sleep_hours              | Horas de sueño                        |
| screen_time_before_sleep | Tiempo de pantalla antes de dormir    |
| academic_performance     | Rendimiento académico                 |
| physical_activity        | Actividad física                      |
| social_interaction_level | Nivel de interacción social           |
| stress_level             | Nivel de estrés                       |
| anxiety_level            | Nivel de ansiedad                     |
| addiction_level          | Nivel de dependencia                  |
| depression_label         | Etiqueta utilizada para el análisis   |

## Tecnologías utilizadas

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn
* GitHub

## Contenido de la aplicación

La aplicación tiene las siguientes secciones:

### Home

Muestra información general del proyecto y del estudiante.

### Carga del Dataset

Permite cargar el archivo CSV y ver una parte de los datos, además de la cantidad de filas y columnas.

### EDA

En esta sección se realizan diferentes análisis:

1. Información general
2. Clasificación de variables
3. Estadísticas descriptivas
4. Valores faltantes
5. Distribución de variables
6. Variables categóricas
7. Numérico vs categórico
8. Categórico vs categórico
9. Análisis dinámico
10. Hallazgos clave

## Programación Orientada a Objetos

Para el proyecto se creó la clase `AnalizadorDatos`, la cual permite realizar algunas operaciones sobre el dataset, como obtener estadísticas, revisar valores nulos y encontrar registros duplicados.

## Capturas de pantalla

### Página principal

Aquí colocaré una captura de la página principal.

### Carga del Dataset

Aquí colocaré una captura de la carga del dataset.

### Análisis EDA

Aquí colocaré una captura de los análisis realizados.

### Análisis dinámico

Aquí colocaré una captura del análisis con filtros.

## Instalación

Primero se debe clonar el repositorio:

```bash
git clone URL_DE_TU_REPOSITORIO
```

Luego ingresar a la carpeta del proyecto:

```bash
cd NOMBRE_DEL_REPOSITORIO
```

Instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

Finalmente ejecutar la aplicación:

```bash
streamlit run app.py
```

## Enlaces

Repositorio de GitHub:

PEGAR AQUI EL LINK DE GITHUB

Aplicación en Streamlit Cloud:

PEGAR AQUI EL LINK DE STREAMLIT

## Autor

Fabricio Gabriel Huánuco Rivero

Ingeniería de Sistemas e Informática
Universidad Continental

2026
