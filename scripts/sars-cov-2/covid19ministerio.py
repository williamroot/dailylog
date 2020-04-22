import os
from io import StringIO

import requests
import pandas as pd

DATA_DIR = 'data'
URL_BASE = 'https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/'
HEADERS = {"x-parse-application-id": "unAFkcaNDeXajurGB7LChj8SgQYS2ptm"}
LISTA = [
    'PortalCovid', 'PortalFaixa', 'PortalSrag',
    'PortalEtiologia', 'PortalAcumulo', 'PortalGeral'
]


def create_dir():
    """
    Cria o diretório `data`. Este diretório é sobrescrito
    cada vez que o script é rodado.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def fetch_ministerio_data():
    """
    Raspa itens das abas `Painel geral` e `SRAG` do portal oficial
    `covid.saude.gov.br`, exclui colunas desnecessárias, formata
    data e transforma casos e óbitos acumulados em casos e óbitos
    por dia.

    Script feito em parceria com Adriano Bini, que criou a versão do
    scraper em C#. Kudos!

    OUTPUT:
        `hospitalizacoes_srag_covid.csv`
        `hospitalizacoes_srag_sexo_idade.csv`
        `hospitalizacoes_srag_semana_epidem.csv`
        `hospitalizacoes_srag_etiologia.csv`
        `br_diario.csv`
        `estados_diario.csv`
    """
    for i in LISTA:
        url = URL_BASE + i
        r = requests.get(url, headers=HEADERS)
        raw_data = r.json()
        data = raw_data['results']

        if i == 'PortalCovid':
            df = pd.DataFrame.from_dict(data)
            df.drop(['createdAt', 'objectId'], axis=1, inplace=True)
            df.rename(columns={
                'label': 'uf',
                'qtd_covid': 'covid',
                'qtd_outros': 'outros',
                'updatedAt': 'atualizacao'
            }, inplace=True)
            df.to_csv('ministerio_hospitalizacoes_srag_covid.csv', index=False)
        elif i == 'PortalFaixa':
            df = pd.DataFrame.from_dict(data)
            df.drop(['createdAt', 'objectId'], axis=1, inplace=True)
            df.rename(columns={
                'label': 'faixa_etaria',
                'qtd_homens': 'masculino',
                'qtd_mulheres': 'feminino',
                'updatedAt': 'atualizacao'
            }, inplace=True)
            df.to_csv('ministerio_hospitalizacoes_srag_sexo_idade.csv', index=False)
        elif i == 'PortalSrag':
            df = pd.DataFrame.from_dict(data)
            df.drop(['createdAt', 'objectId'], axis=1, inplace=True)
            df.rename(columns={
                'label': 'sem_epidem',
                'qtd_2019': 'ano_2019',
                'qtd_2020': 'ano_2020',
                'updatedAt': 'atualizacao'
            }, inplace=True)
            df.to_csv('ministerio_hospitalizacoes_srag_semana_epidem.csv', index=False)
        elif i == 'PortalEtiologia':
            df = pd.DataFrame.from_dict(data)
            df.drop(['createdAt', 'objectId'], axis=1, inplace=True)
            df.rename(columns={
                'label': 'sem_epidem',
                'qtd_influenza_ab': 'influenza_ab',
                'qtd_investigacao': 'em_investigacao',
                'qtd_outros': 'outros',
                'std_sars_cov2': 'sars_cov2',
                'updatedAt': 'atualizacao'
            }, inplace=True)
            df.to_csv('ministerio_hospitalizacoes_srag_etiologia.csv', index=False)
        elif i == 'PortalAcumulo':
            df = pd.DataFrame.from_dict(data)
            df.drop(['createdAt', 'objectId'], axis=1, inplace=True)
            df_temp = pd.DataFrame({
                'data': ['25/02'], 'casos': [0],
                'obitos': [0], 'atualizacao': ['manual']
            })
            df.rename(columns={
                'label': 'data',
                'qtd_confirmado': 'casos',
                'qtd_obito': 'obitos',
                'updatedAt': 'atualizacao'
            }, inplace=True)
            df = pd.concat([df_temp, df], ignore_index=True)
            df['data'] = df['data'] + '/2020'
            df['data'] = pd.to_datetime(df['data'], dayfirst=True)
            df['casos'] = df['casos'].diff(periods=1).fillna(0).astype(int)
            df['obitos'] = df['obitos'].diff(periods=1).fillna(0).astype(int)
            df.to_csv('ministerio_br_diario.csv', index=False)
        elif i == 'PortalGeral':
            new_url = data[0]['arquivo']['url']
            df = pd.read_csv(StringIO(requests.get(new_url).text), sep=";")
            df = df[['estado', 'data', 'casosNovos', 'obitosNovos']]
            df['data'] = pd.to_datetime(df['data'], dayfirst=True)
            df.rename(columns={
                'estado': 'uf',
                'casosNovos': 'casos',
                'obitosNovos': 'obitos'
            }, inplace=True)
            df.to_csv('ministerio_uf_diario.csv', index=False)


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    fetch_ministerio_data()
