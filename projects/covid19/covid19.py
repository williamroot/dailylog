import streamlit as st
import pandas as pd
import altair as alt

# Datasets
virus = 'data/virus.csv'
casos = 'data/casos.csv'
geojson = 'data/ufs.json'

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
# pegamos os de `cata_casos`)
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
ano = st.sidebar.slider('Selecione o período', 2009, 2020, 2020)

# Atualização das variáveis `data_*` com o ano selecionado
data_casos = data_casos[data_casos['ano'] <= ano]
data_virus = data_virus[data_virus['ano'] <= ano]

# --- HEADER ---
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

# Desenho da régua vertical
regua = alt.Chart(data_casos).mark_rule(color='gray').encode(
    x='sem_epidem:Q',
).transform_filter(
    ponto_proximo
)

# Agregação das camadas
g_casos = alt.layer(
    linhas, seletores, regua, texto
).configure_view(
    continuousHeight=400
).configure_axis(
    grid=False
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

# --- TERCEIRO GRÁFICO
#
#
# def gen_base(geojson):
#     base = alt.Chart(alt.Data(values=geojson)).mark_geoshape(
#         stroke='black',
#         strokeWidth=1
#     ).encode(
#     ).properties(
#         width=400,
#         height=400
#     )
#     return base
#
#
# base = gen_base(geojson)
#
#
# def create_geodata(geojson, local):
#     geodata = pd.read_json(geojson)
#     feat = list()
#     coord = list()
#     for x in geodata['features']:
#         for v in x['properties'].items():
#             feat.append(v)
#     for i in geodata['features']:
#         for v in i['geometry'].items():
#             coord.append(v)
#     geografia = list()
#     coordinates = list()
#     for i in feat:
#         if i[0] == local:
#             geografia.append(i[1])
#         else:
#             pass
#     for i in coord:
#         if i[0] == 'coordinates':
#             coordinates.append(i[1][0])
#         else:
#             pass
#     geografia = pd.Series(geografia)
#     coordinates = pd.Series(coordinates)
#     geo = pd.concat([geografia, coordinates], axis=1).reset_index()
#     geo.rename(columns={0: local.lower(), 1: 'coordinates'}, inplace=True)
#     geo.drop(columns='index', inplace=True)
#     return geo
#
#
# geo = create_geodata(geojson, 'ESTADO')
#
# --- TO DO ---
# 1. Criar o dataset de casos/milhão de habitantes
# 2. Juntar os dois datasets
# 3. Definir as props (estado, ano, casos, taxa)
#   cols_props = ['uf', 'ano', 'quantidade', 'taxa']
# 4. Transformar tudo num json
# 5. Depois de criar a função abaixo...
#   def df2geojson(df, properties, coo='coordinates'):
#       geojson = {"type": "FeatureCollection", "features": []}
#       for _, row in df.iterrows():
#           feature = {"type": "Feature",
#                      "properties": {},
#                      "geometry": {"type": "Polygon", "coordinates": []}}
#           feature['geometry']['coordinates'] = [row[coo]]
#           for prop in properties:
#               feature['properties'][prop] = row[prop]
#           geojson['features'].append(feature)
#       return geojson
# ...rodar:
#   geo_final = df2geojson(df, cols_props)
