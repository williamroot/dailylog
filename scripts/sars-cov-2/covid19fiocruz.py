import os
import glob

import requests
import pandas as pd

DATA_DIR = 'data'
URL_BASE = 'http://info.gripe.fiocruz.br/data/detailed/'
UF = {
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

    OUTPUT: `srag_fiocruz.csv`
    """
    for y in range(2008, 2021):
        for w in range(1, 54):
            url_suffix = f'1/2/{y}/{w}/1/Brasil/data-table'
            url = URL_BASE + url_suffix
            data = requests.get(url)
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
    final.replace(UF, inplace=True)
    final['semana_epidem'] = final['semana_epidem'].astype(int)
    final['casos'] = final['casos'].fillna(0).astype(int)
    final.to_csv('fiocruz_srag_sem_epidem.csv', index=False)


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    fetch_srag_data()
    for f in glob.glob(f'raw_srag_fiocruz_*.csv'):
        os.remove(f)
