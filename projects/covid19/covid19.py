import streamlit as st
import pandas as pd
import altair as alt

# Arquivos e estilo de `img`
logo = 'https://logodownload.org/wp-content/uploads/2013/12/rede-globo-logo-4.png'
style_logo = 'display:block; margin-left:auto; margin-right:auto; width:25%'
virus = 'data/virus.csv'

# Elementos básicos da barra lateral
st.sidebar.markdown(
    f'<img src="{logo}" style="{style_logo}">',
    unsafe_allow_html=True
)
st.sidebar.markdown("## Painel SARS-CoV-2")
st.sidebar.markdown("Uma produção da equipe de Soluções do CoE Analytics")


# Aquisição de dados e salvamento em cache
@st.cache
def fetch_data(file):
    data = pd.read_csv(file)
    return data


data_virus = fetch_data(virus)

# Header do container principal
st.subheader('Etiologia')

# Criação do seletor de estados
estados = data_virus['uf'].unique().tolist()
estado_selecionado = st.sidebar.multiselect(
    'Digite as siglas dos estados',
    estados,
    default=["SP", "RJ"]
)
mask_estado = data_virus['uf'].isin(estado_selecionado)

# Atualização da variável `data_virus` com os estados
data_virus = data_virus[mask_estado]

# Criação do seletor de período
ano = st.sidebar.slider('Selecione o período', 2009, 2020, 2020)

# Atualização da variável `data_virus` com o ano selecionado
data_virus = data_virus[data_virus['ano'] <= ano]

# Criação do gráfico
g_virus = alt.Chart(data_virus).mark_bar().encode(
    y=alt.Y('sum(quantidade):Q', axis=alt.Axis(title="")),
    x=alt.X('ano:O', axis=alt.Axis(title="")),
    color=alt.Color(
        'virus',
        scale=alt.Scale(scheme='pastel1'),
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

# Nota e fonte
st.markdown(
    (f"<p style='font-size:10px;margin-top:-5px;'><b>Nota:</b> Dados até \
        a {int(max(data_virus['sem_epidem']))}ª semana epidemiológica de cada \
        ano<br/><b>Fonte:</b> Fiocruz</p>"),
    unsafe_allow_html=True
)
