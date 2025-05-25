```python
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

# --- Aba 2 – Análise de Dores ---
st.header("💢 Análise de Dores por Faixa de Renda")

col_dor = 'Qual o maior desafio ou dificuldade que você vem passando nesse momento? Na vida profissional?'
if col_dor in df.columns:
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
            sns.barplot(data=dor_df, x='Quantidade', y='Dores Mais Citadas', ax=ax_dor, palette='flare')
            ax_dor.set_title(f"Top Dores - {faixa}")
            st.pyplot(fig_dor)
        else:
            st.markdown("Nenhuma dor registrada para essa faixa de renda.")
else:
    st.warning(f"⚠️ A coluna '{col_dor}' não foi encontrada no CSV.")

# --- Aba 3 – Desejos & Motivações ---
st.header("🎯 Aba 3: Desejos & Motivações")

col_desejo = 'Qual seu maior sonho ou objetivo de vida?'
if col_desejo in df.columns:
    df[col_desejo] = df[col_desejo].fillna("Não informado")
    desejo_counts = df[col_desejo].value_counts().head(10)

    if not desejo_counts.empty:
        desejo_df = pd.DataFrame({
            'Desejos / Objetivos': desejo_counts.index,
            'Quantidade': desejo_counts.values
        })
        st.dataframe(desejo_df)

        fig_desejo, ax_desejo = plt.subplots()
        sns.barplot(data=desejo_df, x='Quantidade', y='Desejos / Objetivos', ax=ax_desejo, palette='crest')
        ax_desejo.set_title("Top 10 Desejos / Objetivos de Vida")
        st.pyplot(fig_desejo)
    else:
        st.markdown("Nenhum desejo registrado.")
else:
    st.warning(f"⚠️ A coluna '{col_desejo}' não foi encontrada no CSV.")

# --- Aba 4 – Perfil Comportamental ---
st.header("🧠 Aba 4: Perfil Comportamental")

col_duvidas = 'Se pudéssemos tomar um café juntos, e conversássemos sobre o mercado de Engenharia e Projetos de Infraestrutura e como ter sucesso nele, quais seriam as perguntas que você faria pra mim? Suas maiores dúvidas?'
if col_duvidas in df.columns:
    df[col_duvidas] = df[col_duvidas].fillna("Não informado")
    duvida_counts = df[col_duvidas].value_counts().head(10)

    if not duvida_counts.empty:
        duvida_df = pd.DataFrame({
            'Principais Dúvidas / Perguntas': duvida_counts.index,
            'Quantidade': duvida_counts.values
        })
        st.dataframe(duvida_df)

        fig_duvida, ax_duvida = plt.subplots()
        sns.barplot(data=duvida_df, x='Quantidade', y='Principais Dúvidas / Perguntas', ax=ax_duvida, palette='mako')
        ax_duvida.set_title("Top Dúvidas sobre o Mercado de Projetos")
        st.pyplot(fig_duvida)
    else:
        st.markdown("Nenhuma dúvida registrada.")
else:
    st.warning(f"⚠️ A coluna '{col_duvidas}' não foi encontrada no CSV.")

# --- Rodapé ---
st.markdown("---")
st.subheader("🔜 Próximas seções:")
st.markdown("- Copy Power com sugestões de headline e CTA para cada persona")
```
