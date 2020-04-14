import io
import os
import glob
from functools import reduce
from datetime import date

import requests
import pandas as pd

TODAY = date.today().strftime('%Y-%m-%d')
DATA_DIR = f'data'
UF = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]


def create_dir():
    """
    Cria o diretório `data`, onde serão guardados os arquivos
    temporários e, ao fim, o arquivo `obitos.csv`. Este
    diretório é sobrescrito cada vez que o script é rodado.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def fetch_death_registrocivil():
    """
    Raspa os arquivos `json` do Portal Oficial do Registro Civil
    (registrocivil.org.br), onde são agregados os dados de óbitos
    dos cartórios do Brasil.

    Esta função itera sobre os estados, baixando os dados até a
    data presente. Salva cada `json` como `csv` e, ao fim, junta
    todos os `csv` num arquivo único.

    OUTPUT: `obitos_cartorio.csv`
    """
    for e in UF:
        url_base = 'https://transparencia.registrocivil.org.br/api/covid?data_type=data_ocorrido'
        url_search = f'&search=death-covid&state={e}&start_date=2020-01-01&end_date={TODAY}'
        url = url_base + url_search
        data = requests.get(url)
        raw_response = data.json()
        response = raw_response['chart']
        df = pd.DataFrame.from_dict(
            response,
            orient='index',
            columns=['obitos_cartorio']
        ).reset_index().rename(columns={'index': 'data'})
        df['uf'] = f"{e}"
        df = df[['uf', 'data', 'obitos_cartorio']]
        df['data'] = df['data'] + '/2020'
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        df.to_csv(f'raw_obitos_cartorios_{e}.csv', index=False)
    final = pd.concat(
        [pd.read_csv(f) for f in glob.glob(f'raw_obitos_cartorios_*.csv')]
    )
    final.to_csv('obitos_cartorio.csv', index=False)


def fetch_data_ministerio():
    """
    Pega o `csv` do repositório de Wesley Cota, pesquisador da
    UFV e da Universidad de Zaragoza, na Espanha. Cota está
    raspando diariamente os dados do ministério, e seu dataset
    serve, inclusive, as plataformas da Fiocruz.

    Esta função busca e formata o `csv` de Cota.

    OUTPUT: `obitos_ministerio.csv`
    """
    url = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv'
    url_data = requests.get(url).content
    df = pd.read_csv(io.StringIO(url_data.decode('utf-8')))
    df = df[(df['state'] != 'TOTAL') & (df['city'] == 'TOTAL')]
    df = df[['state', 'date', 'newDeaths']]
    df.rename(columns={
        'date': 'data',
        'state': 'uf',
        'newDeaths': 'obitos_ministerio'
    }, inplace=True)
    df.to_csv(f'obitos_ministerio.csv', index=False)


def fetch_data_secretarias():
    """
    Pega o `csv` de cada estado da plataforma Brasil.io, que está
    compilando os dados de cada estado a partir dos registros de
    cada município.
    
    Esta função itera sobre os estados, baixando os `csv`. Ao fim,
    junta todos os `csv` num arquivo único.

    OUTPUT: `obitos_secretarias.csv`
    """
    for e in UF:
        url = f'https://brasil.io/dataset/covid19/caso?state={e}&place_type=state&format=csv'
        df = pd.read_csv(url)
        df['obitos_secretaria'] = df['deaths'].diff(periods=-1).fillna(0).astype(int)
        df.rename(columns={
            'date': 'data',
            'state': 'uf'
        }, inplace=True)
        df = df[['uf', 'data', 'obitos_secretaria']]
        df.to_csv(f'raw_obitos_secretaria_{e}.csv', index=False)
    final = pd.concat(
        [pd.read_csv(f) for f in glob.glob(f'raw_obitos_secretaria_*.csv')]
    )
    final.to_csv(f'obitos_secretaria.csv', index=False)


def merge_dfs():
    """
    Pega os arquivos gerados pelas funções anteriores e agrupa num
    `csv` único a partir do estado e da data.

    OUTPUT: `obitos.csv`
    """
    cart = pd.read_csv('obitos_cartorio.csv')
    secr = pd.read_csv('obitos_secretaria.csv')
    mins = pd.read_csv('obitos_ministerio.csv')
    dfs = [mins, secr, cart]
    df = reduce(lambda left, right: pd.merge(
        left, right,
        on=['uf', 'data'],
        how='outer'
    ), dfs).fillna(0)
    df['obitos_ministerio'] = df['obitos_ministerio'].astype(int)
    df['obitos_secretaria'] = df['obitos_secretaria'].astype(int)
    df['obitos_cartorio'] = df['obitos_cartorio'].astype(int)
    df.to_csv('obitos.csv', index=False)


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    fetch_death_registrocivil()
    for f in glob.glob(f'raw_obitos_cartorios_*.csv'):
        os.remove(f)  # Apaga os arquivos temporários
    fetch_data_ministerio()
    fetch_data_secretarias()
    for f in glob.glob(f'raw_obitos_secretaria_*.csv'):
        os.remove(f)  # Apaga os arquivos temporários
    merge_dfs()
    for f in glob.glob(f'obitos_*.csv'):
        os.remove(f)  # Apaga os arquivos temporários
