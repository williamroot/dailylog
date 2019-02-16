import os
import shutil
import glob
from urllib.request import urlretrieve
from zipfile import ZipFile
from datetime import datetime

ano_atual = datetime.now().year


def main():
    if not os.path.exists('dados_camara_deputados'):
        os.makedirs('dados_camara_deputados')

    for ano in range(2008, ano_atual + 1):
        url = f'https://www.camara.leg.br/cotas/Ano-{ano}.csv.zip'
        urlretrieve(url, f'dados_camara_deputados/Ano-{ano}.csv.zip')
        zip_file = ZipFile(f'dados_camara_deputados/Ano-{ano}.csv.zip', 'r')
        zip_file.extractall('dados_camara_deputados')
        zip_file.close()
        os.remove(f'dados_camara_deputados/Ano-{ano}.csv.zip')

    todos = glob.glob('dados_camara_deputados/*.csv')
    with open('dados_camara_deputados/camara_deputados_final.csv', 'wb') as saida:
        for i, arquivo in enumerate(todos):
            with open(arquivo, 'rb') as original:
                if i != 0:
                    original.readline()
                shutil.copyfileobj(original, saida)


if __name__ == '__main__':
    main()
