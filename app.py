import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Arqueológico do Avatar", layout="wide")

# Carregar dados
@st.cache_data
def load_data():
    return pd.read_csv("JC3D23 - [Jornada] PESQUISA LEADS  (respostas) - Respostas ao formulário 1.csv")

df = load_data()

st.title("Dashboard Arqueológico do Avatar")

# --- Aba 1 – Visão Geral ---
st.header("📊 Visão Geral: Faixa de Renda")

df['Qual sua renda mensal?'] = df['Qual sua renda mensal?'].fillna('Não informado')
renda_counts = df['Qual sua renda mensal?'].value_counts().sort_values(ascending=False)
total_respostas = len(df)
renda_percent = (renda_counts / total_respostas) * 100

renda_df = pd.DataFrame({
    'Faixa de Renda': renda_counts.index,
    'Quantidade': renda_counts.values,
    'Percentual (%)': renda_percent.round(1).values
})

st.dataframe(renda_df)

fig, ax = plt.subplots()
colors = sns.color_palette("pastel")
ax.pie(renda_counts.values, labels=renda_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
ax.axis('equal')
st.pyplot(fig)

# --- Navegação futura para outras abas ---
st.markdown("---")
st.subheader("🚧 As próximas seções do dashboard incluem:")
st.markdown("""
- Análise de Dores por faixa de faturamento
- Hierarquia de Desejos & Motivações
- Perfil Comportamental
- Copy Power com sugestões de headline e CTA para cada persona

➡️ Em breve neste mesmo painel.
""")