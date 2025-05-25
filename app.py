import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Arqueológico do Avatar", layout="wide")

# Carregar dados
@st.cache_data
def load_data():
    return pd.read_csv("JC3D23 - [Jornada] PESQUISA LEADS  (respostas) - Respostas ao formulário 1.csv")

# Invocar carga de dados e garantir subheader separado

df = load_data()

st.title("Dashboard Arqueológico do Avatar")
# Subheader opcional de confirmação de dados carregados
# st.subheader("🔍 Colunas do CSV carregadas:")

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

# --- Aba 2 – Análise de Dores ---
st.header("💫 Análise de Dores por Faixa de Renda")

col_dor = 'Qual o maior desafio ou dificuldade que você vem passando nesse momento? Na vida profissional?'
df[col_dor] = df[col_dor].fillna("Não informado")

faixas = df['Qual sua renda mensal?'].unique()

for faixa in sorted(faixas):
    subset = df[df['Qual sua renda mensal?'] == faixa]
    st.subheader(f"Faixa de Renda: {faixa}")
    top_dores = subset[col_dor].value_counts().head(5)

    if not top_dores.empty:
        dor_df = pd.DataFrame({
            'Dores Mais Citadas': top_dores.index,
            'Quantidade': top_dores.values
        })
        st.dataframe(dor_df)

        fig_dor, ax_dor = plt.subplots()
        sns.barplot(data=dor_df, x='Quantidade', y='Dores Mais Citadas', ax=ax_dor, palette='flare')
        ax_dor.set_title(f"Top Dores - {faixa}")
        st.pyplot(fig_dor)
    else:
        st.markdown("Nenhuma dor registrada para essa faixa de renda.")

# --- Navegação futura para outras abas ---
st.markdown("---")
st.subheader("🚧 As próximas seções do dashboard incluem:")
st.markdown("""
- Hierarquia de Desejos & Motivações
- Perfil Comportamental
- Copy Power com sugestões de headline e CTA para cada persona

➡️ Em breve neste mesmo painel.
""")