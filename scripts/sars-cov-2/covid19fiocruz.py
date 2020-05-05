import os
import glob
from io import StringIO

import requests
import pandas as pd

DATA_DIR = 'data'


def create_dir():
    """
    Cria o diretório `data`, onde serão guardados os arquivos
    temporários e, ao fim, o arquivo final. Este diretório é
    sobrescrito cada vez que o script é rodado.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def fetch_srag_data():
    """
    Faz o download de todos os `json` de casos de SRAG do site da
    Fiocruz. Cada semana epidemiológica gera um `json`; temos,
    portanto, mais de 400 `json` desde 2012.

    Cada `json` é convertido em `csv`. Concatenados, eles foram um
    dataset que é limpo e tem os nomes dos estados trocados por
    siglas.

    OUTPUT: `fiocruz_srag_sem_epidem.csv`
    """
    uf = {
        'Acre': 'AC', 'Alagoas': 'AL', 'Amapá': 'AP', 'Amazonas': 'AM',
        'Bahia': 'BA', 'Ceará': 'CE', 'Distrito Federal': 'DF',
        'Espírito Santo': 'ES', 'Goiás': 'GO', 'Maranhão': 'MA',
        'Mato Grosso': 'MT', 'Mato Grosso do Sul': 'MS',
        'Minas Gerais': 'MG', 'Pará': 'PA', 'Paraíba': 'PB', 'Paraná': 'PR',
        'Pernambuco': 'PE', 'Piauí': 'PI', 'Rio de Janeiro': 'RJ',
        'Rio Grande do Norte': 'RN', 'Tocantins': 'TO',
        'Rio Grande do Sul': 'RS', 'Rondônia': 'RO', 'Roraima': 'RR',
        'Santa Catarina': 'SC', 'São Paulo': 'SP', 'Sergipe': 'SE'
    }
    url_base = 'http://info.gripe.fiocruz.br/data/detailed/'
    req = requests.Session()
    for y in range(2015, 2021):
        for w in range(1, 54):
            url_suffix = f'1/2/{y}/{w}/1/Brasil/data-table'
            url = url_base + url_suffix
            data = req.get(url)
            raw_response = data.json()
            response = raw_response['data']
            df = pd.DataFrame.from_dict(response)
            df['ano'] = f'{y}'
            df.to_csv(f'raw_srag_fiocruz_{y}_{w}.csv', index=False)

    final = pd.concat(
        [pd.read_csv(f) for f in glob.glob(f'raw_srag_fiocruz_*.csv')],
        sort=False
    )
    final = final[['ano', 'epiweek', 'territory_name', 'value']]
    final = final[final['territory_name'] != 'Brasil']
    final['value'] = final['value'].str.split(r"\s", expand=True)
    final.rename(columns={
        'epiweek': 'semana_epidem',
        'territory_name': 'uf',
        'value': 'casos'
    }, inplace=True)
    final.replace(uf, inplace=True)
    final['semana_epidem'] = final['semana_epidem'].astype(int)
    final['casos'] = final['casos'].fillna(0).astype(int)
    final.to_csv('fiocruz_srag_sem_epidem.csv', index=False)


def fetch_srag_data_MAVE():
    """
    Faz o parsing do `csv` do repositório do MAVE, corrige vírgula,
    descarta variáveis e registros desnecessários.

    OUTPUT: `fiocruz_srag_idade_sexo_virus.csv`
    """
    columns = [
        'data de publicação', 'UF', 'dado', 'escala', 'sexo',
        'Ano epidemiológico', 'Semana epidemiológica',
        'Total reportado até a última atualização', 'Idade desconhecida',
        '< 2 anos', '2-4 anos', '5-9 anos', '10-19 anos', '20-29 anos',
        '30-39 anos', '40-49 anos', '50-59 anos', '60+ anos',
        'Testes positivos', 'Testes negativos', 'Casos aguardando resultado',
        'Casos sem informação laboratorial', 'Casos sem teste laboratorial',
        'Influenza A', 'Influenza B', 'SARS-CoV-2',
        'Vírus sincicial respiratório (VSR)', 'Parainfluenza 1',
        'Parainfluenza 2', 'Parainfluenza 3', 'Adenovirus'
    ]
    int_columns = [
        'Total reportado até a última atualização', 'Idade desconhecida',
        '< 2 anos', '2-4 anos', '5-9 anos', '10-19 anos', '20-29 anos',
        '30-39 anos', '40-49 anos', '50-59 anos', '60+ anos',
        'Testes positivos', 'Testes negativos', 'Casos aguardando resultado',
        'Casos sem informação laboratorial', 'Casos sem teste laboratorial',
        'Influenza A', 'Influenza B', 'SARS-CoV-2',
        'Vírus sincicial respiratório (VSR)', 'Parainfluenza 1',
        'Parainfluenza 2', 'Parainfluenza 3', 'Adenovirus'
    ]
    new_columns = {
        'data de publicação': 'atualizacao',
        'UF': 'uf', 'dado': 'categoria', 'escala': 'escala',
        'sexo': 'sexo', 'Ano epidemiológico': 'ano',
        'Semana epidemiológica': 'sem_epidem',
        'Total reportado até a última atualização': 'total_casos',
        'Idade desconhecida': 'idade_desconhecida',
        '< 2 anos': 'idade_menos_2anos', '2-4 anos': 'idade_2_4anos',
        '5-9 anos': 'idade_5_9anos', '10-19 anos': 'idade_10_19anos',
        '20-29 anos': 'idade_20_29anos', '30-39 anos': 'idade_30_39anos',
        '40-49 anos': 'idade_40_49anos', '50-59 anos': 'idade_50_59anos',
        '60+ anos': 'idade_60anos_mais',
        'Testes positivos': 'testes_positivos',
        'Testes negativos': 'testes_negativos',
        'Casos aguardando resultado': 'casos_aguardando_resultado',
        'Casos sem informação laboratorial': 'casos_sem_info_laboratorial',
        'Casos sem teste laboratorial': 'casos_sem_teste_laboratorial',
        'Influenza A': 'casos_influenza_a',
        'Influenza B': 'casos_influenza_b',
        'SARS-CoV-2': 'casos_sars_cov_2',
        'Vírus sincicial respiratório (VSR)': 'casos_sincicial',
        'Parainfluenza 1': 'casos_parainfluenza_1',
        'Parainfluenza 2': 'casos_parainfluenza_2',
        'Parainfluenza 3': 'casos_parainfluenza_3',
        'Adenovirus': 'casos_adenovirus'
    }
    uf_cod = {
        11: "RO", 12: "AC", 13: "AM", 14: "RR", 15: "PA", 16: "AP",
        17: "TO", 21: "MA", 22: "PI", 23: "CE", 24: "RN", 25: "PB",
        26: "PE", 27: "AL", 28: "SE", 29: "BA", 31: "MG", 32: "ES",
        33: "RJ", 35: "SP", 41: "PR", 42: "SC", 43: "RS", 50: "MS",
        51: "MT", 52: "GO", 53: "DF"
    }
    url_prefix = 'https://gitlab.procc.fiocruz.br/mave/repo/raw/master/Dados/'
    file = 'InfoGripe/dados_semanais_faixa_etaria_sexo_virus.csv'
    url = url_prefix + file
    df = pd.read_csv(
        StringIO(requests.get(url).text),
        sep=';',
        decimal=',',
        low_memory=False)
    df = df[columns]
    df = df[
        (df['escala'] != 'incidência')
        & (df['sexo'] != 'Total')
        & (df['UF'].between(11, 53))
    ]
    df[int_columns] = df[int_columns].astype(int)
    df['UF'].replace(uf_cod, inplace=True)
    df.rename(columns=new_columns, inplace=True)
    df.to_csv('fiocruz_srag_idade_sexo_virus.csv', index=False)


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    fetch_srag_data()
    os.system('rm raw_srag*')
    fetch_srag_data_MAVE()
