# Created by Luiz Cavalcanti and Rodolfo Viana
# November, 2017

import datetime
import json
import io
import os
import requests
import pandas as pd
import urllib.request as request
from shutil import rmtree
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileWriter, PdfFileReader

BASE_DATA_DIR = os.path.join(os.getcwd(), 'data')
TEMP_DATA_DIR = os.path.join(BASE_DATA_DIR, 'notas_fiscais')

EXPENSES_COLUMNS = ['chave', 'nome_arquivo', 'centro_custo',
                    'departamento', 'tipo_departamento',
                    'vereador', 'ano', 'mes', 'despesa',
                    'cnpj', 'fornecedor', 'valor']

CURRENT_YEAR = datetime.datetime.now().year


def fetch_datasets():
    clean_temp_files()
    fetch_expenses()
    fetch_receipts()


def clean_temp_files():
    if (not os.path.exists(BASE_DATA_DIR)):
        os.mkdir(BASE_DATA_DIR)
    if (os.path.exists(TEMP_DATA_DIR)):
        rmtree(TEMP_DATA_DIR)
    os.mkdir(TEMP_DATA_DIR)


def fetch_expenses():
    base_url = 'https://app-sisgvconsulta-prd.azurewebsites.net'
    councilperson_expenses_url = '/ws/ws2.asmx/ObterDebitoVereadorJSON?ano=%s&mes=%s'
    leadership_expenses_url = '/ws/ws2.asmx/ObterDebitoLiderancaJSON?ano=%s&mes=%s'

    expenses = pd.DataFrame(columns=EXPENSES_COLUMNS)

    for year in range(2017, CURRENT_YEAR+1):
        for month in range(1, 13):
            print('Baixando dados de %s/%s' % (month, year))
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


def fetch_receipts():
    base_url = 'http://www.camara.sp.gov.br/wp-content/uploads/contas_vereadores/'
    years_url = 'contas_ano_%s.html'
    base_filename = '%s-%s-%s.pdf'
    for year in range(2017, CURRENT_YEAR+1):
        year_page = BeautifulSoup(request.urlopen(base_url+years_url % (year)).read(), 'html.parser')
        print('Baixando notas fiscais de %s. Isso vai levar algum tempo...' % year)
        for councilperson in year_page.find_all('a'):
            councilperson_name = councilperson.text.replace(' ', '').replace('/', '')
            councilperson_page = BeautifulSoup(request.urlopen(base_url+councilperson.get('href')).read(), 'html.parser')
            councilperson_dir = os.path.join(TEMP_DATA_DIR, councilperson_name)
            for month_entry in councilperson_page.find_all('a'):
                if (not os.path.exists(councilperson_dir)):
                    os.mkdir(councilperson_dir)

                seq = 1
                month = month_entry.text.split(' ')[0].lower()

                pdf_url = month_entry.get('href')
                pdf_content = PdfFileReader(io.BytesIO(requests.get(pdf_url).content))
                for page_num in range(pdf_content.numPages):
                    pdf_out = open(os.path.join(councilperson_dir, base_filename % (year, month, seq)), 'wb')
                    writer = PdfFileWriter()
                    writer.addPage(pdf_content.getPage(page_num))
                    writer.write(pdf_out)
                    seq += 1


fetch_datasets()

print('Feito!')
