import streamlit as st
import pandas as pd
import altair as alt

# Datasets
virus = 'data/virus.csv'
casos = 'data/casos.csv'
pop = 'data/pop.csv'

# Arquivos e estilo de `img`
logo = 'https://logodownload.org/wp-content/uploads/2013/12/rede-globo-logo-4.png'
style_logo = 'display:block; margin-left:auto; margin-right:auto; width:20%'

# Imagem na barra lateral
st.sidebar.markdown(
    f"<img src='{logo}' style='{style_logo}' />",
    unsafe_allow_html=True
)

# Título, linha-fina e linha horizontal na barra lateral
st.sidebar.markdown(
    "<h3 align=center>" +
    "Painel SARS-CoV-2" +
    "</h3>" +
    "<p align=center style='font-size:smaller;'>" +
    "Equipe de Soluções do CoE Analytics" +
    "</p>" +
    "<hr>",
    unsafe_allow_html=True
)


# --- CONSTRUÇÃO DA MECÂNICA ---
# Função para aquisição de dados e salvamento em cache
@st.cache
def fetch_data(file):
    data = pd.read_csv(file)
    return data


# Aquisição dos dados
data_casos = fetch_data(casos)
data_virus = fetch_data(virus)

# Criação do seletor de estados na barra lateral
# (Como os estados de ambos os datasets são iguais,
# pegamos os de `cata_dasos`)
estados = data_casos['uf'].unique().tolist()
estado_selecionado = st.sidebar.multiselect(
    'Digite as siglas dos estados',
    estados,
    default=["SP", "RJ", "MG", "ES", "PR", "SC", "RS"]
)
lista_estados = data_casos['uf'].isin(estado_selecionado)

# Atualização das variáveis `data_*` com os estados
data_casos = data_casos[lista_estados]
data_virus = data_virus[lista_estados]

# Criação do seletor de período na barra lateral
# (Como os anos de ambos os datasets são iguais,
# pegamos os de `data_casos`)
ano_max = int(max(data_casos['ano']))
ano = st.sidebar.slider('Selecione o período', 2009, ano_max, ano_max)

# Atualização das variáveis `data_*` com o ano selecionado
data_casos = data_casos[data_casos['ano'] <= ano]
data_virus = data_virus[data_virus['ano'] <= ano]

# --- CONTEÚDO ---
# Criação do header e do subheader
st.title("Síndrome respiratória aguda grave")
st.write(
    "**Fonte:** Fundação Oswaldo Cruz - Fiocruz<br>" +
    f"**Nota:** Dados até a {int(max(data_casos['sem_epidem']))}ª " +
    "semana epidemiológica de cada ano",
    unsafe_allow_html=True
)

# --- PRIMEIRO GRÁFICO ---
# Título
st.subheader('Casos')


# Criação de gráfico de linha
def line_chart(dataset, x, y, color_index, scheme, legend_title):
    ponto_proximo = alt.selection(
        type='single',
        nearest=True,
        on='mouseover',
        fields=[x],
        empty='none'
    )
    linhas = alt.Chart(dataset).mark_line(interpolate='linear').encode(
        x=alt.X(x, axis=alt.Axis(title="")),
        y=alt.Y(y, axis=alt.Axis(title="")),
        color=alt.Color(
            color_index,
            scale=alt.Scale(scheme=scheme),
            legend=alt.Legend(title=legend_title)
        )
    )
    seletores = alt.Chart(dataset).mark_point().encode(
        x=x,
        opacity=alt.value(0),
    ).add_selection(
        ponto_proximo
    )
    texto = linhas.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(
            ponto_proximo,
            y,
            alt.value(' ')
        )
    )
    regua = alt.Chart(dataset).mark_rule(color='gray').encode(
        x=x,
    ).transform_filter(
        ponto_proximo
    )
    graph = alt.layer(
        linhas, seletores, regua, texto
    ).configure_view(
        continuousHeight=400
    ).configure_axis(
        grid=False
    )
    return graph


g_casos = line_chart(
    data_casos,
    'sem_epidem:Q',
    'sum(quantidade):Q',
    'ano:N',
    'blueorange',
    'Anos'
)

# Apresentação
st.altair_chart(g_casos, use_container_width=True)

# --- SEGUNDO GRÁFICO ---
# Título
st.subheader('Etiologia')

# Configurações do gráfico
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

# Apresentação
st.altair_chart(g_virus, use_container_width=True)
