import streamlit as st
import pandas as pd
import plotly.express as px

#CRIAÇÃO DO TITULO
st.title("Dasboard de Desempenho de Alunos")

#CARREGAMENTO DOS DADOS
df = pd.read_csv("dados.csv")
st.subheader("Tabela de dados")
st.dataframe(df)

#CRIAÇÃO DE FILTRO
curso = st.selectbox("Selecione o Curso", df["Curso"].unique())
df_filtrado = df[df["Curso"]== curso]
st.subheader("Dados Filtrados")
st.write(df_filtrado)

#ELABORAÇÃO DE GRAFICO

barra = px.bar(
        df_filtrado,
        x="Aluno",
        y="Nota",
        color="Aluno",
        title="Notas dos Alunos"
)

st.plotly_chart(barra)