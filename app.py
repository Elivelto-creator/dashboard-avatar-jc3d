```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração da página
st.set_page_config(page_title="Dashboard Arqueológico do Avatar", layout="wide")

# --- Carregar dados ---
@st.cache_data
def load_data():
    return pd.read_csv(
        "JC3D23 - [Jornada] PESQUISA LEADS  (respostas) - Respostas ao formulário 1.csv"
    )

df = load_data()

st.title("Dashboard Arqueológico do Avatar")

# --- Aba 1: Visão Geral ---
st.header("📊 Visão Geral: Faixa de Renda")

df['Qual sua renda mensal?'] = df['Qual sua renda mensal?'].fillna('Não informado')
renda_counts = df['Qual sua renda mensal?'].value_counts()
total = len(df)
renda_percent = (renda_counts / total) * 100
renda_df = pd.DataFrame({
    'Faixa de Renda': renda_counts.index,
    'Quantidade': renda_counts.values,
    'Percentual (%)': renda_percent.round(1).values
})
st.dataframe(renda_df)
fig, ax = plt.subplots()
ax.pie(renda_counts.values, labels=renda_counts.index, autopct='%1.1f%%')
st.pyplot(fig)

# --- Aba 2: Análise de Dores ---
st.header("💢 Análise de Dores por Faixa de Renda")
col_dor = 'Qual o maior desafio ou dificuldade que você vem passando nesse momento? Na vida profissional?'
if col_dor in df.columns:
    df[col_dor] = df[col_dor].fillna('Não informado')
    for faixa in sorted(df['Qual sua renda mensal?'].unique()):
        subset = df[df['Qual sua renda mensal?'] == faixa]
        st.subheader(f"Faixa de Renda: {faixa}")
        top_dores = subset[col_dor].value_counts().head(5)
        dor_df = pd.DataFrame({'Dores': top_dores.index, 'Qtd': top_dores.values})
        st.dataframe(dor_df)
        fig2, ax2 = plt.subplots()
        sns.barplot(data=dor_df, x='Qtd', y='Dores', ax=ax2)
        st.pyplot(fig2)
else:
    st.warning(f"Coluna de dores não encontrada: {col_dor}")

# --- Aba 3: Desejos & Motivações ---
st.header("🎯 Aba 3: Desejos & Motivações")
col_desejo = 'Qual seu maior sonho ou objetivo de vida?'
if col_desejo in df.columns:
    df[col_desejo] = df[col_desejo].fillna('Não informado')
    top_desejos = df[col_desejo].value_counts().head(10)
    desejo_df = pd.DataFrame({'Desejo': top_desejos.index, 'Qtd': top_desejos.values})
    st.dataframe(desejo_df)
    fig3, ax3 = plt.subplots()
    sns.barplot(data=desejo_df, x='Qtd', y='Desejo', ax=ax3)
    st.pyplot(fig3)
else:
    st.warning(f"Coluna de desejos não encontrada: {col_desejo}")

# --- Aba 4: Perfil Comportamental ---
st.header("🧠 Aba 4: Perfil Comportamental")
col_duvidas = (
    'Se pudéssemos tomar um café juntos, e conversássemos sobre o mercado de Engenharia '
    'e Projetos de Infraestrutura e como ter sucesso nele, quais seriam as perguntas '
    'que você faria pra mim? Suas maiores dúvidas?'
)
if col_duvidas in df.columns:
    df[col_duvidas] = df[col_duvidas].fillna('Não informado')
    top_duvidas = df[col_duvidas].value_counts().head(10)
    duvida_df = pd.DataFrame({'Dúvida': top_duvidas.index, 'Qtd': top_duvidas.values})
    st.dataframe(duvida_df)
    fig4, ax4 = plt.subplots()
    sns.barplot(data=duvida_df, x='Qtd', y='Dúvida', ax=ax4)
    st.pyplot(fig4)
else:
    st.warning(f"Coluna de dúvidas não encontrada: {col_duvidas}")

# --- Rodapé ---
st.markdown("---")
st.subheader("🔜 Próximas seções: Copy Power por Persona")
```
