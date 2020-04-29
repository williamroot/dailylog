import json
import streamlit as st
import pandas as pd
import altair as alt
import pydeck

# Datasets
virus = 'data/virus.csv'
casos = 'data/casos.csv'
pop = 'data/pop.csv'
json_file = 'data/ufs.json'

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

# --- TERCEIRO GRÁFICO ---

# A mecânica deste terceiro gráfico (um mapa feito com pydeck)
# não é a mais adequada. Por três motivos:
# 1. Ele não muda conforme as semanas
# 2. Ele consome dados geográficos de outro `geojson`
# 3. Ele cria um `geojson` que precisa ser hospedado para,
#    então sim, o mapa renderizar.
# A questão de pegar os polígonos de outro `geojson` não me
# causa tanto problema. As demais questões, sim, demandam
# ação. É preciso encontrar uma forma de usado dados
# `inline`, ou seja, sem a necessidade de geração e hospedagem
# de arquivo. E, sendo `inline`, ele automaticamente teria
# os dados dinâmico -- isto é, a cada semana selecionada,
# os dados mudariam.
# Tentei usar Altair, mas não rolou. (E, se optarmos por
# Altair, teremos de usar bibliotecas que convertam o formato
# `geojson` em `topojson`).

# Título
st.subheader('Internações por 1 milhão de habitantes')

# Aquisição de dados
data_casos = fetch_data(casos)
data_pop = fetch_data(pop)
data_casos = data_casos[data_casos['ano'] > 2009]  # Apenas para teste

# Definição de semana edidemiológica
max_se = int(max(data_casos['sem_epidem']))
se = st.number_input('Selecione a semana epidemiológica', 1, max_se, max_se)


# Função que gera um `dataframe` com todas as informações
@st.cache
def generate_data_map(ano=ano, se=se):
    df_casos = data_casos.groupby(
        ['uf', 'ano', 'sem_epidem']
    ).agg({
        'quantidade': 'sum'
    }).reset_index()
    df_casos = df_casos[(df_casos['ano'] == ano) & (df_casos['sem_epidem'] == se)]
    df = pd.merge(df_casos, data_pop, on=['uf', 'ano'], how='inner')
    df['taxa'] = (df['quantidade'] / df['pop']) * 1000000
    # Geração de RGB para ser usado no mapa (pydeck requer isso)
    r = []
    g = []
    b = []
    for i, v in df['taxa'].iteritems():
        if 0 < v <= 3:
            r.append(255)
            g.append(160)
            b.append(122)
        elif 3 < v <= 5.9999999999:
            r.append(255)
            g.append(127)
            b.append(80)
        elif 6 < v <= 8.9999999999:
            r.append(255)
            g.append(99)
            b.append(71)
        elif 9 < v <= 11.9999999999:
            r.append(220)
            g.append(20)
            b.append(60)
        else:
            r.append(178)
            g.append(34)
            b.append(34)
    df['r'] = r
    df['g'] = g
    df['b'] = b
    df = df[['uf', 'ano', 'sem_epidem', 'quantidade', 'taxa', 'r', 'g', 'b']]
    # Aqui ocorre a leitura do `geojson` que fornece dados geográficos
    jdata = pd.read_json(json_file)
    feat = list()
    coord = list()
    for x in jdata['features']:
        for v in x['properties'].items():
            feat.append(v)
    for i in jdata['features']:
        for v in i['geometry'].items():
            coord.append(tuple(v))
    estado = []
    types = []
    coordinates = []
    for i in feat:
        if i[0] == 'ESTADO':
            estado.append(i[1])
        else:
            pass
    for i in coord:
        if i[0] == 'type':
            types.append(i[1])
        elif i[1] not in ["Polygon", "MultiPolygon"]:
            coordinates.append(i[1])
    estado = pd.Series(estado)
    types = pd.Series(types)
    coordinates = pd.Series(coordinates)
    geo = pd.concat([estado, types, coordinates], axis=1).reset_index()
    geo.rename(columns={0: 'estado', 1: 'type', 2: 'coordinates'}, inplace=True)
    geo.drop(columns='index', inplace=True)
    df = pd.merge(df, geo, left_on='uf', right_on='estado', how='inner')
    df.drop(columns='estado', inplace=True)
    return df


geo_data = generate_data_map()


# Conversão do `dataframe` em `geojson`
def df2geojson(df, properties, coo='coordinates'):
    geojson = {"type": "FeatureCollection", "features": list()}
    for _, row in df.iterrows():
        feature = {f"type": "Feature",
                   "properties": {},
                   "geometry": {"type": row['type'], "coordinates": list()}}
        feature['geometry']['coordinates'] = row[coo]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    geojson = json.dumps(geojson, indent=4)
    # O arquivo a seguir é o que acaba hospedado
    with open('taxas.json', 'w') as file:
        file.write(geojson)
    return geojson


geojson = df2geojson(geo_data, properties=[
    'uf', 'ano', 'sem_epidem', 'taxa', 'r', 'g', 'b'
])


# Gerador de mapa
def map_maker(file):
    # Hospedado no GitHub
    url = 'https://raw.githubusercontent.com/rodolfo-viana/dailylog/master/misc/'
    url = url + 'taxas.json'
    LAND_COVER = [
        [[5.0, -81.9], [5.0, -84.2], [-32.0, -84.2], [-32.0, -81.9]]
    ]
    polygon = pydeck.Layer(
        "PolygonLayer",
        LAND_COVER,
        stroked=False,
        get_polygon="-",
        get_fill_color=[0, 0, 0, 20],
    )
    geojson = pydeck.Layer(
        "GeoJsonLayer",
        url,
        opacity=0.8,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True,
        get_fill_color="[properties.r, properties.g, properties.b, 200]",
        get_line_color=[255, 255, 255],
    )
    r = pydeck.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        layers=[polygon, geojson],
        initial_view_state=pydeck.ViewState(
            latitude=-15.7757875,
            longitude=-48.0778529,
            zoom=3,
            max_zoom=16,
            pitch=45,
            bearing=0
        )
    )
    return r


# Geração do mapa
g_map = map_maker(geojson)
st.pydeck_chart(g_map)

# Criação de tabela
show_df = geo_data[['uf', 'ano', 'sem_epidem', 'taxa']]
show_df = show_df[(show_df['ano'] == ano) & (show_df['sem_epidem'] == se)]
st.table(show_df)
