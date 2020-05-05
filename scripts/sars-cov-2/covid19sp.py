import os
import ssl
from datetime import datetime

import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context


DATA_DIR = 'data'
MONTH = datetime.now().strftime('%m')
URL_BASE = f'http://www.seade.gov.br/wp-content/uploads/2020/{MONTH}/'
DICT_DATE = {
    r"(\d{2})\sjan": r"2020-01-\1", r"(\d{2})\sfev": r"2020-02-\1",
    r"(\d{2})\smar": r"2020-03-\1", r"(\d{2})\sabr": r"2020-04-\1",
    r"(\d{2})\smai": r"2020-05-\1", r"(\d{2})\sjun": r"2020-06-\1",
    r"(\d{2})\sjul": r"2020-07-\1", r"(\d{2})\sago": r"2020-08-\1",
    r"(\d{2})\sset": r"2020-09-\1", r"(\d{2})\sout": r"2020-10-\1",
    r"(\d{2})\snov": r"2020-11-\1", r"(\d{2})\sdez": r"2020-12-\1"
}


def create_dir():
    """
    Cria o diretório `data`, onde serão guardados os arquivos.
    Este diretório é sobrescrito cada vez que o script é rodado.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def fetch_state_data():
    """
    Passa os dados do `csv` da fonte (Seade) para um `dataframe`,
    elimina as colunas desnecessárias e as linhas em branco,
    traduz as datas para leitura por máquina e salva em `csv`.

    OUTPUT: `sp_estado_dia.csv`
    """
    url = URL_BASE + 'Dados-covid-19-estado.csv'
    df = pd.read_csv(url, sep=';', encoding='latin-1')
    df = df[['Data', 'Casos por dia', 'Óbitos por dia']]
    df = df.dropna(how='all').fillna(0)
    df.rename(columns={
        'Data': 'data',
        'Casos por dia': 'casos',
        'Óbitos por dia': 'obitos'
    }, inplace=True)
    df[['casos', 'obitos']] = df[['casos', 'obitos']].astype(int)
    df.replace(regex=DICT_DATE, inplace=True)
    df['data'] = pd.to_datetime(df['data'])
    df.to_csv(
        'secretaria_sp_estado_dia.csv',
        sep=',',
        encoding='utf-8',
        index=False
    )


def fetch_cities_data():
    """
    Passa os dados do `csv` da fonte (Seade) para um `dataframe`,
    elimina as colunas desnecessárias e as linhas em branco e
    salva em `csv`.

    OUTPUT: `sp_municipios.csv`
    """
    url = URL_BASE + 'Dados-covid-19-municipios.csv'
    df = pd.read_csv(url, sep=';', encoding='latin-1')
    df = df[['Município', 'Mun_Total de casos', 'Mun_Total de óbitos']]
    df = df.dropna(how='all').fillna(0)
    df.rename(columns={
        'Município': 'municipio',
        'Mun_Total de casos': 'casos',
        'Mun_Total de óbitos': 'obitos'
    }, inplace=True)
    df[['casos', 'obitos']] = df[['casos', 'obitos']].astype(int)
    df.to_csv(
        'secretaria_sp_municipios_total.csv',
        sep=',',
        encoding='utf-8',
        index=False
    )


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    fetch_state_data()
    fetch_cities_data()
