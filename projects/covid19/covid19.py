import streamlit as st
import pandas as pd
import altair as alt

# Datasets
virus = 'data/virus.csv'
casos = 'data/casos.csv'

# Arquivos e estilo de `img`
logo = 'https://logodownload.org/wp-content/uploads/2013/12/rede-globo-logo-4.png'
style_logo = 'display:block; margin-left:auto; margin-right:auto; width:25%'

# Elementos básicos da barra lateral
st.sidebar.markdown(
    f'<img src="{logo}" style="{style_logo}">',
    unsafe_allow_html=True
)
st.sidebar.markdown("## Painel SARS-CoV-2")
st.sidebar.markdown("Uma produção da equipe de Soluções do CoE Analytics")


# Função para aquisição de dados e salvamento em cache
@st.cache
def fetch_data(file):
    data = pd.read_csv(file)
    return data


# Aquisição do arquivo `casos.csv`
data_casos = fetch_data(casos)

# ----- HEADER -----
st.title("Síndrome respiratória aguda grave")
st.write(f"**Fonte:** Fundação Oswaldo Cruz - Fiocruz<br>**Nota:** Dados até a {int(max(data_casos['sem_epidem']))}ª semana epidemiológica de cada ano", unsafe_allow_html=True)

# ----- PRIMEIRA PARTE -----
# Subheader
st.subheader('Casos')

# Criação do seletor de estados
estados = data_casos['uf'].unique().tolist()
estado_selecionado = st.sidebar.multiselect(
    'Digite as siglas dos estados',
    estados,
    default=["SP", "RJ", "MG", "ES", "PR", "SC", "RS"]
)
lista_estados = data_casos['uf'].isin(estado_selecionado)

# Atualização da variável `data_casos` com os estados
data_casos = data_casos[lista_estados]

# Criação do seletor de período
ano = st.sidebar.slider('Selecione o período', 2009, 2020, 2020)

# Atualização da variável `data_virus` com o ano selecionado
data_casos = data_casos[data_casos['ano'] <= ano]

# Criação de seleção que toma o ponto mais próximo das linhas
ponto_proximo = alt.selection(
    type='single',
    nearest=True,
    on='mouseover',
    fields=['sem_epidem'],
    empty='none'
)

# Criação das linhas
linhas = alt.Chart(data_casos).mark_line(interpolate='linear').encode(
    x=alt.X('sem_epidem:Q', axis=alt.Axis(title="Semana epidemiológica")),
    y=alt.Y('sum(quantidade):Q', axis=alt.Axis(title="")),
    color=alt.Color(
        'ano:N',
        scale=alt.Scale(scheme='blueorange'),
        legend=alt.Legend(title="Anos")
    )
)

# Criação de seletor transparente que indica a posição do mouse no gráfico
seletores = alt.Chart(data_casos).mark_point().encode(
    x='sem_epidem:Q',
    opacity=alt.value(0),
).add_selection(
    ponto_proximo
)

# Criação de texto que segue os pontos
texto = linhas.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(
        ponto_proximo,
        'sum(quantidade):Q',
        alt.value(' ')
    )
)

# Desenha a régua
regua = alt.Chart(data_casos).mark_rule(color='gray').encode(
    x='sem_epidem:Q',
).transform_filter(
    ponto_proximo
)

# Agrega as camadas
g_casos = alt.layer(
    linhas, seletores, regua, texto
).configure_view(
    continuousHeight=400
).configure_axis(
    grid=False
)

st.altair_chart(g_casos, use_container_width=True)

# ----- SEGUNDA PARTE -----
data_virus = fetch_data(virus)

data_virus = data_virus[lista_estados]

data_virus = data_virus[data_virus['ano'] <= ano]

st.subheader('Etiologia')

g_virus = alt.Chart(data_virus).mark_bar().encode(
    y=alt.Y('sum(quantidade):Q', axis=alt.Axis(title="")),
    x=alt.X('ano:O', axis=alt.Axis(title="")),
    color=alt.Color(
        'virus',
        scale=alt.Scale(scheme='blueorange'),
        legend=alt.Legend(title="Tipos de vírus")
    ),
    tooltip=[
        alt.Tooltip('virus', title='Tipo de vírus'),
        alt.Tooltip('ano', title='Ano'),
        alt.Tooltip('sum(quantidade)', title='Quantidade')
    ]
).configure_view(
    continuousHeight=400
).configure_axis(
    grid=False
)

st.altair_chart(g_virus, use_container_width=True)
