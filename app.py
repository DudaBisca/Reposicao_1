import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_excel("dataset_sinalizacao_ferroviaria.xlsx")

st.title("Reposição: Dashboard de Sinalização Ferroviária")

st.write("Análise dos dados de sinalização das Linhas A e B.")
st.write("Criador: Maria Eduarda de Oliveira Bisca")
st.subheader("Informações do Dataset")

st.write(f"Quantidade de registros: {len(df)}")
st.write(f"Quantidade de colunas: {len(df.columns)}")

st.subheader("Dados do Dataset")

st.dataframe(df)

#GRÁFICO 1

st.title("Dashbord 1")
st.subheader("1. Velocidade permitida x Tempo de ocupação")

grafico1 = px.scatter(
    df,
    x="velocidade_permitida_kmh",
    y="tempo_ocupacao_circuito_seg",
    color="tipo_sinalizacao",
    title="Velocidade permitida x Tempo de ocupação"
)

st.plotly_chart(grafico1)

#GRÁFICO 2 

st.title("Dashbord 2")
st.subheader("2. Aspecto dos sinais por tipo de sinalização")

contagem_sinais = pd.crosstab(
    df["tipo_sinalizacao"],
    df["aspecto_sinal"]
)

grafico2 = px.bar(
    contagem_sinais,
    barmode="stack",
    title="Aspecto dos sinais por tipo de sinalização"
)

st.plotly_chart(grafico2)