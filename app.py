import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set\_page\_config(page\_title="Dashboard Arqueológico do Avatar", layout="wide")

# Carregar dados

@st.cache\_data
def load\_data():
return pd.read\_csv("JC3D23 - \[Jornada] PESQUISA LEADS  (respostas) - Respostas ao formulário 1.csv")

df = load\_data()

st.title("Dashboard Arqueológico do Avatar")

# DEBUG: Ver nomes reais das colunas

st.subheader("🔎 Colunas do CSV carregadas:")
st.code("\n".join(df.columns.tolist()))

# --- Aba 1 – Visão Geral ---

st.header("📊 Visão Geral: Faixa de Renda")

df\['Qual sua renda mensal?'] = df\['Qual sua renda mensal?'].fillna('Não informado')
renda\_counts = df\['Qual sua renda mensal?'].value\_counts().sort\_values(ascending=False)
total\_respostas = len(df)
renda\_percent = (renda\_counts / total\_respostas) \* 100

renda\_df = pd.DataFrame({
'Faixa de Renda': renda\_counts.index,
'Quantidade': renda\_counts.values,
'Percentual (%)': renda\_percent.round(1).values
})

st.dataframe(renda\_df)

fig, ax = plt.subplots()
colors = sns.color\_palette("pastel")
ax.pie(renda\_counts.values, labels=renda\_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
ax.axis('equal')
st.pyplot(fig)

# --- Aba 2 – Análise de Dores ---

st.header("💢 Análise de Dores por Faixa de Renda")

col\_dor = 'Qual o maior desafio ou dificuldade que você vem passando nesse momento? Na vida profissional?'
if col\_dor in df.columns:
df\[col\_dor] = df\[col\_dor].fillna("Não informado")
faixas = df\['Qual sua renda mensal?'].unique()

```
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
```

else:
st.warning(f"⚠️ A coluna '{col\_dor}' não foi encontrada no CSV. Copie o nome correto da seção acima.")

# --- Aba 3 – Desejos & Motivações ---

st.header("🎯 Desejos & Motivações")

col\_desejo = 'Qual seu maior sonho ou objetivo de vida?'
if col\_desejo in df.columns:
df\[col\_desejo] = df\[col\_desejo].fillna("Não informado")
desejo\_counts = df\[col\_desejo].value\_counts().head(10)

```
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
```

else:
st.warning(f"⚠️ A coluna '{col\_desejo}' não foi encontrada no CSV. Copie o nome correto da seção acima.")

# --- Aba 4 – Perfil Comportamental ---

st.header("🧠 Perfil Comportamental: Perguntas Frequentes e Dúvidas")

col\_duvidas = 'Se pudéssemos tomar um café juntos, e conversássemos sobre o mercado de Engenharia e Projetos de Infraestrutura e como ter sucesso nele, quais seriam as perguntas que você faria pra mim? Suas maiores dúvidas?'
if col\_duvidas in df.columns:
df\[col\_duvidas] = df\[col\_duvidas].fillna("Não informado")
duvida\_counts = df\[col\_duvidas].value\_counts().head(10)

```
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
```

else:
st.warning(f"⚠️ A coluna '{col\_duvidas}' não foi encontrada no CSV. Copie o nome correto da seção acima.")

# --- Rodapé ---

st.markdown("---")
st.subheader("🔜 As próximas seções do dashboard incluem:")
st.markdown("""

* Copy Power com sugestões de headline e CTA para cada persona

➡️ Em breve neste mesmo painel.
""")
