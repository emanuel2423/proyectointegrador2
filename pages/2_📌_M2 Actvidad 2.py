import streamlit as st
import pandas as pd




# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

def load_data():
    return pd.read_csv("pages/static/datasets/estudiantes_colombia.csv")

st.title("Análisis de Estudiantes en Colombia")

st.header("Semana 8")
df = pd.read_csv("pages/static/datasets/estudiantes_colombia.csv")


st.dataframe(df)

data = load_data()

columnas_seleccionadas = ["nombre", "edad", "promedio"]

columnas_existentes = [col for col in columnas_seleccionadas if col in data.columns]

st.subheader("Primeras 5 filas del dataset")
st.write(data.head())

st.subheader("Últimas 5 filas del dataset")
st.write(data.tail())

st.subheader("Resumen de información del dataset")
buffer_info = data.info() 
st.text(buffer_info)

st.subheader("Estadísticas del dataset")
st.write(data.describe()) 

promedio_minimo = st.slider(
    "Selecciona el promedio mínimo", 
    min_value=float(data['promedio'].min()), 
    max_value=float(data['promedio'].max()), 
    value=float(data['promedio'].min()), 
    step=0.1
)

estudiantes_filtrados = data[data['promedio'] > promedio_minimo]

st.subheader(f"Estudiantes con promedio mayor a {promedio_minimo}")
st.write(estudiantes_filtrados[columnas_existentes])

