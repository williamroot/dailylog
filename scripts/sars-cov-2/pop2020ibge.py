import os
from ftplib import FTP
import fnmatch

import pandas as pd

DATA_DIR = 'data'
URL_BASE = 'ftp://ftp.ibge.gov.br/'
FTP_PATH = 'ftp.ibge.gov.br'
FOLDER = 'Projecao_da_Populacao/Projecao_da_Populacao_2018/'

IGN_LIST = [
    'BRASIL', 'Norte', 'Nordeste',
    'Sul', 'Sudeste', 'Centro-Oeste'
]


def create_dir():
    """
    Cria o diretório `data`, onde será guardado o arquivo.
    Este diretório é sobrescrito cada vez que o script é rodado.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def fetch_data():
    """
     Procura o arquivo `xlsx` no FTP do IBGE, converte cada aba
     de estado em um `dataframe`, encontra a célula referente à
     população total no ano de 2020 e salva em `csv`.

     OUTPUT: `ibge_projecao_populacao_2020.csv`
     """
    fc = FTP(FTP_PATH)
    fc.login()
    fc.cwd(FOLDER)
    root = fc.nlst()
    for i in root:
        if fnmatch.fnmatch(i, "projecoes_2018_populacao_2010_2060_*.xls"):
            file = i
    lista = []
    url = URL_BASE + FOLDER + file
    xl = pd.ExcelFile(url)
    for i in xl.sheet_names:
        if i not in IGN_LIST:
            sheet = pd.read_excel(xl, sheet_name=i, header=None)
            x = sheet.loc[51, 11]
            dicionario = {"uf": i, "populacao": int(x)}
            lista.append(dicionario)
    df = pd.DataFrame(lista)
    df = df[['uf', 'populacao']]
    df.to_csv('ibge_projecao_populacao_2020.csv', index=False)


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    fetch_data()
