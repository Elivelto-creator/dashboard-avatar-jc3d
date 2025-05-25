import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Arqueológico do Avatar", layout="wide")

# Carregar dados
@st.cache_data
def load_data():
    return pd.read_csv(
        "JC3D23 - [Jornada] PESQUISA LEADS  (respostas) - Respostas ao formulário 1.csv"
    )

# Invocar carga de dados
df = load_data()

# Título do Dashboard
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
ax.pie(
    renda_counts.values,
    labels=renda_counts.index,
    autopct='%1.1f%%',
    colors=colors,
    startangle=140
)
ax.axis('equal')
st.pyplot(fig)

# --- Aba 2 – Análise de Dores ---
st.header("💫 Análise de Dores por Faixa de Renda")

col_dor = (
    'Qual o maior desafio ou dificuldade que você vem passando nesse momento? '
    'Na vida profissional?'
)
df[col_dor] = df[col_dor].fillna("Não informado")

for faixa in sorted(df['Qual sua renda mensal?'].unique()):
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
        sns.barplot(
            data=dor_df,
            x='Quantidade',
            y='Dores Mais Citadas',
            ax=ax_dor,
            palette='flare'
        )
        ax_dor.set_title(f"Top Dores - {faixa}")
        st.pyplot(fig_dor)
    else:
        st.markdown("Nenhuma dor registrada para essa faixa de renda.")

# --- Aba 3 – Desejos & Motivações ---
st.header("🎯 Aba 3: Desejos & Motivações")

col_desejo = 'Qual seu maior sonho ou objetivo profissional?'
df[col_desejo] = df[col_desejo].fillna("Não informado")

# Top 10 desejos gerais

desejos_counts = df[col_desejo].value_counts().head(10)
desejos_df = pd.DataFrame({
    'Desejos & Motivações': desejos_counts.index,
    'Quantidade': desejos_counts.values
})
st.dataframe(desejos_df)

fig_desejo, ax_desejo = plt.subplots()
sns.barplot(
    data=desejos_df,
    x='Quantidade',
    y='Desejos & Motivações',
    ax=ax_desejo,
    palette='crest'
)
ax_desejo.set_title("Top 10 Desejos Gerais")
st.pyplot(fig_desejo)

# Desejos por faixa de renda
for faixa in sorted(df['Qual sua renda mensal?'].unique()):
    subset = df[df['Qual sua renda mensal?'] == faixa]
    counts = subset[col_desejo].value_counts().head(5)
    st.subheader(f"Desejos Principais – Faixa: {faixa}")
    sub_df = pd.DataFrame({
        'Desejos': counts.index,
        'Quantidade': counts.values
    })
    st.dataframe(sub_df)
    fig_sub, ax_sub = plt.subplots()
    sns.barplot(
        data=sub_df,
        x='Quantidade',
        y='Desejos',
        ax=ax_sub,
        palette='mako'
    )
    ax_sub.set_title(f"Top Desejos - {faixa}")
    st.pyplot(fig_sub)

# --- Navegação futura para outras abas ---
st.markdown("---")
st.subheader("🚧 As próximas seções do dashboard incluem:")
st.markdown(
    """
    - Perfil Comportamental
    - Copy Power com sugestões de headline e CTA para cada persona

    ➡️ Em breve neste mesmo painel.
    """
)
