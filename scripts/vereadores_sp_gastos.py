import os
import urllib.request as r
from datetime import datetime
import json
import pandas as pd

CSV_PARAMS = {'compression': 'xz', 'encoding': 'utf-8', 'index': False}
DATA_DIR = os.path.join(os.getcwd(), 'data')
COLUNAS = ['chave', 'nome_arquivo', 'centro_custo', 'departamento',
           'tipo_departamento', 'vereador', 'ano', 'mes', 'despesa',
           'cnpj', 'fornecedor', 'valor']
ANO_ATUAL = datetime.now().year


def create_dir():
    """
    Cria diretório 'data', se ele não existir.
    """
    if (not os.path.exists(DATA_DIR)):
        os.mkdir(DATA_DIR)


def fetch_data():
    """
    Aponta para os dados de vereadores e lideranças, faz o download dos
    registros de todos os meses e anos a partir de 2015, converte json
    em csv, comprime o arquivo para xz.
    """
    base = 'http://app-sisgvconsulta-prd.azurewebsites.net/ws/ws2.asmx'
    deb_vereador = '/ObterDebitoVereadorJSON?ano=%s&mes=%s'
    deb_lideranca = '/ObterDebitoLiderancaJSON?ano=%s&mes=%s'
    gastos = pd.DataFrame(columns=COLUNAS)
    for ano in range(2015, ANO_ATUAL + 1):
        for mes in range(1, 13):
            print(f'Baixando registros de {mes}/{ano}')
            json_data = r.urlopen(base + deb_vereador % (ano, mes)).read()
            if json_data:
                gastos = gastos.append(parse_expenses(json_data))
            json_data = r.urlopen(base + deb_lideranca % (ano, mes)).read()
            if json_data:
                gastos = gastos.append(parse_expenses(json_data))
    hoje = datetime.strftime(datetime.now(), '%Y-%m-%d')
    arquivo = os.path.join(DATA_DIR, '%s_gastos_vereadores.xz' % (hoje))
    gastos.to_csv(arquivo, **CSV_PARAMS)
    print(f'{len(gastos)} registros de despesas salvos no arquivo {hoje}_gastos_vereadores.xz')


def parse_expenses(json_data):
    """
    Faz iteração nos registros para alocá-los nas respectivas colunas.
    """
    df = pd.DataFrame(columns=COLUNAS)
    data = json.loads(json_data)
    for gasto in data:
        chave = gasto['Chave']
        nome_arquivo = gasto['NomeArquivo']
        centro_custo = gasto['CENTROCUSTOSID']
        departamento = gasto['DEPARTAMENTO']
        tipo_departamento = gasto['TIPODEPARTAMENTO']
        vereador = gasto['VEREADOR']
        ano = gasto['ANO']
        mes = gasto['MES']
        despesa = gasto['DESPESA']
        cnpj = gasto['CNPJ']
        fornecedor = gasto['FORNECEDOR']
        valor = gasto['VALOR']
        df.loc[len(df)] = [chave, nome_arquivo, centro_custo,
                           departamento, tipo_departamento,
                           vereador, ano, mes, despesa, cnpj,
                           fornecedor, valor]
    return df


if __name__ == '__main__':
    create_dir()
    fetch_data()
