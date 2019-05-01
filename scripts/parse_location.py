from glob import glob
import os

import pandas as pd

# Definir colunas para renomear ou remover

cols_rename = {
    'geometry.coordinates': 'lat_long',
    'properties.DISPLAY_NAME': 'nm_distrito',
    'properties.MOVEMENT_ID': 'id_distrito',
    'properties.NomeDistri': 'nm_regiao',
    'properties.NomeMunici': 'nm_cidade',
    'properties.NumDistrit': 'id_regiao',
    'properties.NumeroMuni': 'id_cidade'
}

cols_drop = [
    'geometry.type',
    'properties.NomeZona',
    'properties.NumeroZona',
    'type'
]

cols_drop_fmt = ['sourceid', 'dstid']

# Tratar dados de locais

location = pd.read_csv('locais.csv', sep=';')
location.drop(columns=cols_drop, inplace=True)
location.rename(columns=cols_rename, inplace=True)
location = location[[
    'nm_distrito', 'id_distrito', 'nm_regiao', 'id_regiao',
    'nm_cidade', 'id_cidade', 'lat_long'
]]
location.to_csv('fmt_location.csv', sep=';', index=False)

# Abrir cada arquivo da pasta, aplicar os dados de locais e salvar

os.chdir('./data/')
os.mkdir('data_fmt/')
for i in glob('*.csv'):
    data = pd.read_csv(i, sep=',', low_memory=False)
    df_agg = data.merge(location,
                        left_on='sourceid',
                        right_on='id_distrito')
    df_agg = df_agg.merge(location,
                          left_on='dstid',
                          right_on='id_distrito',
                          suffixes=('_origem', '_destino'))
    df_agg.drop(columns=cols_drop_fmt, inplace=True)
    fmt_filename = 'data_fmt/fmtd_' + i
    df_agg.to_csv(fmt_filename, index=False)
