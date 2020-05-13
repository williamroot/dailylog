import json
import base64
import requests
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import datetime

dias = 'data/secretaria_sp_municipios_dia.csv'
pop = 'data/pop2.csv'
json_file = requests.get(
    'https://raw.githubusercontent.com/rodolfo-viana/dailylog/master/misc/sp_municipios_ibge_2018.json')
json_data = json_file.text


@st.cache
def fetch_data():
    data = pd.read_csv(dias)
    data = data.groupby(['cod_ibge', 'municipio']).agg({'casos': 'sum', 'obitos': 'sum'}).reset_index()
    popula = pd.read_csv(pop)
    data = pd.merge(data, popula, on='cod_ibge', how='left')
    data['taxa'] = (data['casos'] / data['pop']) * 1000
    return data


st.title("Casos por 1 mil habitantes")

dados = fetch_data()

# st.slider("Selecione o período final", datetime.date()) # CONTINUAR

dados = dados[dados['cod_ibge'] != 9999999]


@st.cache
def cria_mapa():
    geojson = json.loads(json_data)
    return geojson


geojson = cria_mapa()

fig = px.choropleth_mapbox(
    dados, geojson=geojson,
    color="taxa", color_continuous_scale=px.colors.sequential.Reds,
    opacity=0.8, locations="cod_ibge", featureidkey="properties.CD_GEOCMU",
    center={"lat": -22.495, "lon": -48.557778},
    mapbox_style="carto-positron", zoom=5.5
)

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

st.plotly_chart(fig)
