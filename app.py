import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Dashboard de Funcionários",
    layout="wide"
)

st.title("📊 Dashboard de Análise de Funcionários")


@st.cache_data
def carregar_dados():
    dados = {
        "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
        "idade": [23, 35, 29, np.nan, 40],
        "cidade": ["SP", "RJ", "SP", "MG", "RJ"],
        "salario": [3000, 5000, 4000, 3500, np.nan],
        "data_contratacao": pd.to_datetime([
            "2020-01-10",
            "2019-03-15",
            "2021-07-22",
            "2018-11-05",
            "2022-06-30"
        ])
    }

    df = pd.DataFrame(dados)

    # Limpeza de dados
    df["idade"] = df["idade"].fillna(df["idade"].mean())
    df["salario"] = df["salario"].fillna(df["salario"].median())

    df["salario_anual"] = df["salario"] * 12
    df["ano_contratacao"] = df["data_contratacao"].dt.year
    df["categoria_salario"] = df["salario"].apply(
        lambda x: "Alto" if x > 4500 else "Médio" if x > 3000 else "Baixo"
    )

    return df


df = carregar_dados()


st.sidebar.header("🔎 Filtros")

cidades = st.sidebar.multiselect(
    "Selecione a cidade",
    options=df["cidade"].unique(),
    default=df["cidade"].unique()
)

faixa_salario = st.sidebar.slider(
    "Faixa salarial",
    float(df["salario"].min()),
    float(df["salario"].max()),
    (float(df["salario"].min()), float(df["salario"].max()))
)

opcao = st.sidebar.selectbox("Cidade específica", ["Todas"] + list(df["cidade"].unique()))


df_filtrado = df[
    (df["cidade"].isin(cidades)) &
    (df["salario"] >= faixa_salario[0]) &
    (df["salario"] <= faixa_salario[1])
]

if opcao != "Todas":
    df_filtrado = df_filtrado[df_filtrado["cidade"] == opcao]


col1, col2, col3 = st.columns(3)

col1.metric("💰 Salário Médio", f"R$ {df_filtrado['salario'].mean():.2f}")
col2.metric("👥 Total Funcionários", df_filtrado.shape[0])
col3.metric("📈 Salário Máximo", f"R$ {df_filtrado['salario'].max():.2f}")


st.subheader("📊 Análises")

col1, col2 = st.columns(2)

media_cidade = df_filtrado.groupby("cidade")["salario"].mean()
col1.bar_chart(media_cidade)

categoria = df_filtrado["categoria_salario"].value_counts()
col2.bar_chart(categoria)


st.subheader("📋 Dados")

st.dataframe(
    df_filtrado,
    use_container_width=True
)


pivot = pd.pivot_table(
    df_filtrado,
    values="salario",
    index="cidade",
    columns="categoria_salario",
    aggfunc="mean"
)

st.subheader("📊 Tabela Dinâmica")
st.dataframe(pivot)


st.sidebar.subheader("📂 Upload de CSV")

uploaded_file = st.sidebar.file_uploader(
    "Envie um CSV",
    type=["csv"]
)

if uploaded_file:
    df_upload = pd.read_csv(uploaded_file)
    st.write("📄 Dados carregados:")
    st.dataframe(df_upload)