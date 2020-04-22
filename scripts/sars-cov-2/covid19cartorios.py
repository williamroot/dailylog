import os
import glob
from datetime import date

import requests
import pandas as pd

DATA_DIR = 'data'
URL_BASE = 'https://transparencia.registrocivil.org.br/api/covid?data_type=data_ocorrido'
UF = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]
TODAY = date.today().strftime('%Y-%m-%d')


def create_dir():
    """
    Cria o diretório `data`, onde serão guardados os arquivos
    temporários e, ao fim, o arquivo final. Este diretório é
    sobrescrito cada vez que o script é rodado.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def fetch_registrocivil_data():
    """
    Raspa os arquivos `json` do Portal Oficial do Registro Civil
    (registrocivil.org.br), onde são agregados os dados de óbitos
    dos cartórios do Brasil.

    Esta função itera sobre os estados, baixando os dados até a
    data presente. Salva cada `json` como `csv` e, ao fim, junta
    todos os `csv` num arquivo único.

    OUTPUT: `cartorios_obitos_covid.csv`
    """
    for e in UF:
        url_search = f'&search=death-covid&state={e}&start_date=2020-01-01&end_date={TODAY}'
        url = URL_BASE + url_search
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
    final.to_csv('cartorios_obitos_covid.csv', index=False)


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    fetch_registrocivil_data()
    os.system('rm obitos_cartorios*')
