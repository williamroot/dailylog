# To have this script working some criteria must be met:
# 1. The first column of the csv file must be the school's unique id.
# 2. The csv file must correspond to a city or a state.
import os
import unicodedata
import csv
import json

TEST_FILE = 'escolas.csv'  # Change it to the file you want to convert


def csv2json(csv_file):
    """Converts a csv file with multiple rows into multiple one-array
    json files, each one corresponding to a single row of the original
    file, and saves them into a designated folder.

    Args:
        csv_file (string): csv file to convert

    Retuns:
        {json_file}.json (file): one-array json file

    """
    with open(f'{csv_file}') as input:
        reader = csv.DictReader(input)
        for row in reader:
            content = dict(row)
            json_file = list(content.values())[0]
            uf = json_file[:2]

            if 'CO_MUNICIPIO' in content.keys():
                if 'CO_ENTIDADE' in content.keys():
                    path = f"{uf}/{content['CO_MUNICIPIO']}/escolas/"\
                        .replace(' ', '').replace("'", '')
                    path = unicodedata.normalize('NFD', path)\
                        .encode('ascii', 'ignore')\
                        .decode('utf-8')
                    if not os.path.exists(path):
                        os.makedirs(path)
                    with open(f'{path}/{json_file}.json', 'wb') as output:
                        output.write(json.dumps([content], ensure_ascii=False).encode('utf8'))
                else:
                    path = f"{uf}/{content['CO_MUNICIPIO']}/"\
                        .replace(' ', '').replace("'", '')
                    path = unicodedata.normalize('NFD', path)\
                        .encode('ascii', 'ignore')\
                        .decode('utf-8')
                    if not os.path.exists(path):
                        os.makedirs(path)
                    with open(f'{path}/{json_file}.json', 'wb') as output:
                        output.write(json.dumps([content], ensure_ascii=False).encode('utf8'))
            if 'CO_MUNICIPIO' not in content.keys():
                path = f"{content['CO_UF']}"
                if not os.path.exists(path):
                    os.makedirs(path)
                with open(f'{path}/{json_file}.json', 'wb') as output:
                    output.write(json.dumps([content], ensure_ascii=False).encode('utf8'))


csv2json(TEST_FILE)
print("Done!")
