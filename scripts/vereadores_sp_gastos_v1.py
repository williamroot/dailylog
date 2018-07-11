# Created by Luiz Cavalcanti and Rodolfo Viana
# October, 2017

import datetime
import json
import os
import pandas as pd
import urllib.request as request

BASE_DATA_DIR = os.path.join(os.getcwd(), 'data')

EXPENSES_COLUMNS = ['chave', 'nome_arquivo', 'centro_custo',
                    'departamento', 'tipo_departamento',
                    'vereador', 'ano', 'mes', 'despesa',
                    'cnpj', 'fornecedor', 'valor']

CURRENT_YEAR = datetime.datetime.now().year


def fetch_datasets():
    clean_temp_files()
    fetch_expenses()


def clean_temp_files():
    if (not os.path.exists(BASE_DATA_DIR)):
        os.mkdir(BASE_DATA_DIR)


def fetch_expenses():
    base_url = 'https://app-sisgvconsulta-prd.azurewebsites.net'
    councilperson_expenses_url = '/ws/ws2.asmx/ObterDebitoVereadorJSON?ano=%s&mes=%s'
    leadership_expenses_url = '/ws/ws2.asmx/ObterDebitoLiderancaJSON?ano=%s&mes=%s'

    expenses = pd.DataFrame(columns=EXPENSES_COLUMNS)

    for year in range(2015, CURRENT_YEAR+1):
        for month in range(1, 13):
            print('Baixando dados do ano %s, mês %s' % (year, month))
            json_data = request.urlopen(base_url+councilperson_expenses_url % (year, month)).read()
            if json_data:
                expenses = expenses.append(parse_expenses(json_data))

            json_data = request.urlopen(base_url+leadership_expenses_url % (year, month)).read()
            if json_data:
                expenses = expenses.append(parse_expenses(json_data))

    output_file = os.path.join(BASE_DATA_DIR, 'gastos_vereadores.csv')
    expenses.to_csv(output_file, sep=';', encoding='utf-8', index=False)


def parse_expenses(json_data):
    df = pd.DataFrame(columns=EXPENSES_COLUMNS)
    data = json.loads(json_data)

    for expense in data:
        chave = expense['Chave']
        nome_arquivo = expense['NomeArquivo']
        centro_custo = expense['CENTROCUSTOSID']
        departamento = expense['DEPARTAMENTO']
        tipo_departamento = expense['TIPODEPARTAMENTO']
        vereador = expense['VEREADOR']
        ano = expense['ANO']
        mes = expense['MES']
        despesa = expense['DESPESA']
        cnpj = expense['CNPJ']
        fornecedor = expense['FORNECEDOR']
        valor = expense['VALOR']

        df.loc[len(df)] = [chave, nome_arquivo, centro_custo,
                           departamento, tipo_departamento,
                           vereador, ano, mes, despesa, cnpj,
                           fornecedor, valor]

    return df


fetch_datasets()
