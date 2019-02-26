import os
from urllib.request import urlretrieve
from zipfile import ZipFile


def main():
    DATA_DIR = '../files'
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    else:
        os.path.join(DATA_DIR)

    for ano in range(2016, 2019):
        for mes in range(1, 13):
            mes = format(mes, '02d')
            url_base = 'http://www.portaltransparencia.gov.br/download-de-dados/'
            url_path = f'bolsa-familia-saques/{ano}{mes}'
            url = url_base + url_path

            urlretrieve(url, f'{DATA_DIR}/{ano}{mes}_BolsaFamilia_saques.zip')
            zip_file = ZipFile(f'{DATA_DIR}/{ano}{mes}_BolsaFamilia_saques.zip', 'r')
            zip_file.extractall(f'{DATA_DIR}')
            zip_file.close()
            os.remove(f'{DATA_DIR}/{ano}{mes}_BolsaFamilia_saques.zip')


if __name__ == '__main__':
    main()
