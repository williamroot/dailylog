import glob
import os
import unicodedata

import pandas as pd

DATA_DIR = 'data'
URL_BASE = "https://github.com/seade-R/dados-covid-sp/raw/master/data/"
FILE = "Municipios%20informacoes%20dia.xlsx"
URL = URL_BASE + FILE
IGN_LIST = [
    0, "Total", "TOTAL", "total", "Total Geral",
    "Total geral", "TOTAL GERAL", "total geral"
]
DICT_DATE = {
    r"(\d{2})\_jan": r"2020-01-\1", r"(\d{2})\_fev": r"2020-02-\1",
    r"(\d{2})\_mar": r"2020-03-\1", r"(\d{2})\_abr": r"2020-04-\1",
    r"(\d{2})\_mai": r"2020-05-\1", r"(\d{2})\_jun": r"2020-06-\1",
    r"(\d{2})\_jul": r"2020-07-\1", r"(\d{2})\_ago": r"2020-08-\1",
    r"(\d{2})\_set": r"2020-09-\1", r"(\d{2})\_out": r"2020-10-\1",
    r"(\d{2})\_nov": r"2020-11-\1", r"(\d{2})\_dez": r"2020-12-\1"
}

# As tabelas dos dias 4, 5 e 21 de abril estão com problema na origem
missing_dates = [
    {"munic": "ÁGUAS DE LINDOIA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "AGUDOS", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "AMERICANA", "casos": 3, "obitos": 1, "data": "04_abr"},
    {"munic": "ARAÇATUBA", "casos": 4, "obitos": 0, "data": "04_abr"},
    {"munic": "ARARAQUARA", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "ARUJÁ", "casos": 5, "obitos": 1, "data": "04_abr"},
    {"munic": "ASSIS", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "ATIBAIA", "casos": 3, "obitos": 0, "data": "04_abr"},
    {"munic": "BARUERI", "casos": 29, "obitos": 1, "data": "04_abr"},
    {"munic": "BAURU", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "BOTUCATU", "casos": 7, "obitos": 0, "data": "04_abr"},
    {"munic": "BRODOWSKI", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "CACHOEIRA PAULISTA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "CAIEIRAS", "casos": 19, "obitos": 1, "data": "04_abr"},
    {"munic": "CAJAMAR", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "CAMPINAS", "casos": 26, "obitos": 4, "data": "04_abr"},
    {"munic": "CARAPICUIBA", "casos": 11, "obitos": 1, "data": "04_abr"},
    {"munic": "CEDRAL", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "COTIA", "casos": 28, "obitos": 2, "data": "04_abr"},
    {"munic": "CRAVINHOS", "casos": 2, "obitos": 1, "data": "04_abr"},
    {"munic": "DIADEMA", "casos": 23, "obitos": 1, "data": "04_abr"},
    {"munic": "DRACENA", "casos": 1, "obitos": 1, "data": "04_abr"},
    {"munic": "EMBU DAS ARTES", "casos": 19, "obitos": 1, "data": "04_abr"},
    {"munic": "FERRAZ DE VASCONCELOS", "casos": 15, "obitos": 0, "data": "04_abr"},
    {"munic": "FRANCA", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "FRANCISCO MORATO", "casos": 8, "obitos": 1, "data": "04_abr"},
    {"munic": "FRANCO DA ROCHA", "casos": 7, "obitos": 1, "data": "04_abr"},
    {"munic": "GUARARAPES", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "GUARUJA", "casos": 3, "obitos": 0, "data": "04_abr"},
    {"munic": "GUARULHOS", "casos": 62, "obitos": 5, "data": "04_abr"},
    {"munic": "HORTOLÂNDIA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "Ignorado", "casos": 8, "obitos": 0, "data": "04_abr"},
    {"munic": "INDAIATUBA", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "IRACEMAPÓLIS", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "ITANHAÉM", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "ITAPECERICA DA SERRA", "casos": 9, "obitos": 1, "data": "04_abr"},
    {"munic": "ITAPEVI", "casos": 7, "obitos": 1, "data": "04_abr"},
    {"munic": "ITAPIRA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "ITAQUAQUECETUBA", "casos": 10, "obitos": 0, "data": "04_abr"},
    {"munic": "ITARARÉ", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "ITU", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "ITUPEVA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "JABOTICABAL", "casos": 3, "obitos": 1, "data": "04_abr"},
    {"munic": "JAGUARIUNA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "JANDIRA", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "JAÚ", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "JOSÉ BONIFÁCIO", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "JUNDIAÍ", "casos": 6, "obitos": 0, "data": "04_abr"},
    {"munic": "LENCOIS PAULISTA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "LIMEIRA", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "LOUVEIRA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "MAIRIPORÃ", "casos": 4, "obitos": 1, "data": "04_abr"},
    {"munic": "MARÍLIA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "MATÃO", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "MAUÁ", "casos": 15, "obitos": 0, "data": "04_abr"},
    {"munic": "MOGI DAS CRUZES", "casos": 17, "obitos": 1, "data": "04_abr"},
    {"munic": "MOGI GUACU", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "NOVA ODESSA", "casos": 1, "obitos": 1, "data": "04_abr"},
    {"munic": "ORLÂNDIA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "OSASCO", "casos": 62, "obitos": 2, "data": "04_abr"},
    {"munic": "Outros estados", "casos": 34, "obitos": 0, "data": "04_abr"},
    {"munic": "Outros países", "casos": 35, "obitos": 0, "data": "04_abr"},
    {"munic": "PARIQUERA ACÚ", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "PAULÍNIA", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "PENÁPOLIS", "casos": 1, "obitos": 1, "data": "04_abr"},
    {"munic": "PIRACICABA", "casos": 6, "obitos": 0, "data": "04_abr"},
    {"munic": "PIRAJUÍ", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "POA", "casos": 3, "obitos": 0, "data": "04_abr"},
    {"munic": "PRAIA GRANDE", "casos": 4, "obitos": 0, "data": "04_abr"},
    {"munic": "PROMISSÃO", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "RIBEIRAO PIRES", "casos": 4, "obitos": 0, "data": "04_abr"},
    {"munic": "RIBEIRÃO PRETO", "casos": 24, "obitos": 1, "data": "04_abr"},
    {"munic": "RIO CLARO", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "SALTO DE PIRAPORA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "SANTA BRANCA", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "SANTA ISABEL", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "SANTANA DE PARNAIBA", "casos": 24, "obitos": 0, "data": "04_abr"},
    {"munic": "SANTO ANDRE", "casos": 76, "obitos": 3, "data": "04_abr"},
    {"munic": "SANTOS", "casos": 66, "obitos": 2, "data": "04_abr"},
    {"munic": "SAO BERNARDO DO CAMPO", "casos": 77, "obitos": 4, "data": "04_abr"},
    {"munic": "SAO CAETANO DO SUL", "casos": 38, "obitos": 1, "data": "04_abr"},
    {"munic": "SÃO JOSE DO RIO PARDO", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "SAO JOSE DO RIO PRETO", "casos": 9, "obitos": 0, "data": "04_abr"},
    {"munic": "SAO JOSE DOS CAMPOS", "casos": 24, "obitos": 0, "data": "04_abr"},
    {"munic": "SAO MANUEL", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "SAO PAULO", "casos": 3496, "obitos": 212, "data": "04_abr"},
    {"munic": "SAO SEBASTIAO", "casos": 3, "obitos": 1, "data": "04_abr"},
    {"munic": "SAO VICENTE", "casos": 5, "obitos": 0, "data": "04_abr"},
    {"munic": "SOROCABA", "casos": 8, "obitos": 2, "data": "04_abr"},
    {"munic": "SUZANO", "casos": 8, "obitos": 0, "data": "04_abr"},
    {"munic": "TABOAO DA SERRA", "casos": 39, "obitos": 2, "data": "04_abr"},
    {"munic": "TATUÍ", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "TAUBATÉ", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "VALINHOS", "casos": 3, "obitos": 0, "data": "04_abr"},
    {"munic": "VARGEM GRANDE PAULISTA", "casos": 4, "obitos": 1, "data": "04_abr"},
    {"munic": "VINHEDO", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "VOTORANTIM", "casos": 2, "obitos": 0, "data": "04_abr"},
    {"munic": "VOTUPORANGA", "casos": 1, "obitos": 0, "data": "04_abr"},
    {"munic": "AGUAS DE LINDOIA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "AGUDOS", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "AMERICANA", "casos": 3, "obitos": 2, "data": "05_abr"},
    {"munic": "ARACATUBA", "casos": 4, "obitos": 0, "data": "05_abr"},
    {"munic": "ARARAQUARA", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "ARUJA", "casos": 6, "obitos": 1, "data": "05_abr"},
    {"munic": "ASSIS", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Atibaia", "casos": 4, "obitos": 0, "data": "05_abr"},
    {"munic": "BARUERI", "casos": 30, "obitos": 1, "data": "05_abr"},
    {"munic": "BAURU", "casos": 3, "obitos": 1, "data": "05_abr"},
    {"munic": "BOTUCATU", "casos": 7, "obitos": 0, "data": "05_abr"},
    {"munic": "BRODOWSKI", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "CACHOEIRA PAULISTA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Caieiras", "casos": 20, "obitos": 1, "data": "05_abr"},
    {"munic": "CAJAMAR", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "CAMPINAS", "casos": 26, "obitos": 4, "data": "05_abr"},
    {"munic": "CARAPICUIBA", "casos": 14, "obitos": 1, "data": "05_abr"},
    {"munic": "Cedral", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Cotia", "casos": 29, "obitos": 3, "data": "05_abr"},
    {"munic": "CRAVINHOS", "casos": 2, "obitos": 1, "data": "05_abr"},
    {"munic": "Diadema", "casos": 24, "obitos": 1, "data": "05_abr"},
    {"munic": "DRACENA", "casos": 1, "obitos": 1, "data": "05_abr"},
    {"munic": "Embu das Artes", "casos": 20, "obitos": 1, "data": "05_abr"},
    {"munic": "Ferraz de Vasconcelos", "casos": 15, "obitos": 0, "data": "05_abr"},
    {"munic": "Franca", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "Francisco Morato", "casos": 8, "obitos": 1, "data": "05_abr"},
    {"munic": "FRANCO DA ROCHA", "casos": 8, "obitos": 1, "data": "05_abr"},
    {"munic": "GUARARAPES", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "GUARUJA", "casos": 3, "obitos": 0, "data": "05_abr"},
    {"munic": "Guarulhos", "casos": 62, "obitos": 5, "data": "05_abr"},
    {"munic": "HORTOLANDIA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Ignorado", "casos": 5, "obitos": 0, "data": "05_abr"},
    {"munic": "Indaiatuba", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "IRACEMAPOLIS", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "ITANHAEM", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "ITAPECERICA DA SERRA", "casos": 9, "obitos": 1, "data": "05_abr"},
    {"munic": "ITAPETININGA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Itapevi", "casos": 8, "obitos": 1, "data": "05_abr"},
    {"munic": "Itapira", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "ITAQUAQUECETUBA", "casos": 10, "obitos": 0, "data": "05_abr"},
    {"munic": "ITARARE", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "ITU", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "ITUPEVA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "JABOTICABAL", "casos": 3, "obitos": 1, "data": "05_abr"},
    {"munic": "JAGUARIUNA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "JANDIRA", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "JAU", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "JOSE BONIFACIO", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "JUNDIAI", "casos": 6, "obitos": 0, "data": "05_abr"},
    {"munic": "LENCOIS PAULISTA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "LIMEIRA", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "LOUVEIRA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "MAIRIPORA", "casos": 5, "obitos": 2, "data": "05_abr"},
    {"munic": "MARILIA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "MATAO", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "MAUA", "casos": 16, "obitos": 0, "data": "05_abr"},
    {"munic": "MOGI DAS CRUZES", "casos": 17, "obitos": 1, "data": "05_abr"},
    {"munic": "MOGI GUACU", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "NOVA ODESSA", "casos": 1, "obitos": 1, "data": "05_abr"},
    {"munic": "ORLANDIA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Osasco", "casos": 69, "obitos": 3, "data": "05_abr"},
    {"munic": "Outros estados", "casos": 34, "obitos": 0, "data": "05_abr"},
    {"munic": "Outros países", "casos": 34, "obitos": 0, "data": "05_abr"},
    {"munic": "PARIQUERA ACU", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "PAULINIA", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "PENAPOLIS", "casos": 1, "obitos": 1, "data": "05_abr"},
    {"munic": "PIRACICABA", "casos": 6, "obitos": 0, "data": "05_abr"},
    {"munic": "PIRAJUI", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "POA", "casos": 3, "obitos": 0, "data": "05_abr"},
    {"munic": "Praia Grande", "casos": 4, "obitos": 0, "data": "05_abr"},
    {"munic": "PROMISSAO", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "RIBEIRAO PIRES", "casos": 4, "obitos": 0, "data": "05_abr"},
    {"munic": "RIBEIRAO PRETO", "casos": 25, "obitos": 1, "data": "05_abr"},
    {"munic": "RIO CLARO", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "Salto de Pirapora", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Santa Branca", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "SANTA ISABEL", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "SANTANA DE PARNAIBA", "casos": 24, "obitos": 0, "data": "05_abr"},
    {"munic": "SANTO ANDRE", "casos": 72, "obitos": 3, "data": "05_abr"},
    {"munic": "Santos", "casos": 72, "obitos": 2, "data": "05_abr"},
    {"munic": "SAO BERNARDO DO CAMPO", "casos": 81, "obitos": 5, "data": "05_abr"},
    {"munic": "SAO CAETANO DO SUL", "casos": 38, "obitos": 1, "data": "05_abr"},
    {"munic": "SÃO JOSE DO RIO PARDO", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "SAO JOSE DO RIO PRETO", "casos": 10, "obitos": 0, "data": "05_abr"},
    {"munic": "SAO JOSE DOS CAMPOS", "casos": 30, "obitos": 0, "data": "05_abr"},
    {"munic": "SAO MANUEL", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "SAO PAULO", "casos": 3612, "obitos": 220, "data": "05_abr"},
    {"munic": "SAO SEBASTIAO", "casos": 3, "obitos": 1, "data": "05_abr"},
    {"munic": "SAO VICENTE", "casos": 5, "obitos": 0, "data": "05_abr"},
    {"munic": "SOROCABA", "casos": 9, "obitos": 2, "data": "05_abr"},
    {"munic": "Suzano", "casos": 9, "obitos": 0, "data": "05_abr"},
    {"munic": "TABOAO DA SERRA", "casos": 41, "obitos": 3, "data": "05_abr"},
    {"munic": "TATUI", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "TAUBATE", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "TERRA ROXA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "VALINHOS", "casos": 3, "obitos": 0, "data": "05_abr"},
    {"munic": "VARGEM GRANDE PAULISTA", "casos": 4, "obitos": 1, "data": "05_abr"},
    {"munic": "VINHEDO", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "Votorantim", "casos": 2, "obitos": 0, "data": "05_abr"},
    {"munic": "VOTUPORANGA", "casos": 1, "obitos": 0, "data": "05_abr"},
    {"munic": "ADAMANTINA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "AGUAS DE LINDOIA", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "AGUAS DE SAO PEDRO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "AGUDOS", "casos": 7, "obitos": 1, "data": "21_abr"},
    {"munic": "ALAMBARI", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "AMERICANA", "casos": 25, "obitos": 3, "data": "21_abr"},
    {"munic": "AMERICO BRASILIENSE", "casos": 5, "obitos": 0, "data": "21_abr"},
    {"munic": "AMPARO", "casos": 5, "obitos": 0, "data": "21_abr"},
    {"munic": "ANDRADINA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "ANGATUBA", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "APARECIDA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "APIAI", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ARACARIGUAMA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ARACATUBA", "casos": 38, "obitos": 0, "data": "21_abr"},
    {"munic": "ARACOIABA DA SERRA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ARANDU", "casos": 7, "obitos": 0, "data": "21_abr"},
    {"munic": "ARARAQUARA", "casos": 51, "obitos": 2, "data": "21_abr"},
    {"munic": "ARARAS", "casos": 6, "obitos": 0, "data": "21_abr"},
    {"munic": "ARTUR NOGUEIRA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ARUJA", "casos": 25, "obitos": 1, "data": "21_abr"},
    {"munic": "ASSIS", "casos": 6, "obitos": 1, "data": "21_abr"},
    {"munic": "ATIBAIA", "casos": 22, "obitos": 1, "data": "21_abr"},
    {"munic": "AVAI", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "AVARE", "casos": 8, "obitos": 1, "data": "21_abr"},
    {"munic": "BADY BASSITT", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "BARIRI", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "BARRA DO TURVO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "BARRETOS", "casos": 11, "obitos": 2, "data": "21_abr"},
    {"munic": "BARUERI", "casos": 144, "obitos": 5, "data": "21_abr"},
    {"munic": "BATATAIS", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "BAURU", "casos": 58, "obitos": 3, "data": "21_abr"},
    {"munic": "BEBEDOURO", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "BILAC", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "BIRIGUI", "casos": 8, "obitos": 0, "data": "21_abr"},
    {"munic": "BOITUVA", "casos": 7, "obitos": 0, "data": "21_abr"},
    {"munic": "BOTUCATU", "casos": 28, "obitos": 2, "data": "21_abr"},
    {"munic": "BRAGANCA PAULISTA", "casos": 36, "obitos": 7, "data": "21_abr"},
    {"munic": "BRODOWSKI", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "BURITAMA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "CACAPAVA", "casos": 8, "obitos": 0, "data": "21_abr"},
    {"munic": "CACHOEIRA PAULISTA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "CAIABU", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "CAIEIRAS", "casos": 49, "obitos": 7, "data": "21_abr"},
    {"munic": "CAJAMAR", "casos": 9, "obitos": 1, "data": "21_abr"},
    {"munic": "CAJURU", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "CAMPINAS", "casos": 199, "obitos": 7, "data": "21_abr"},
    {"munic": "CAMPO LIMPO PAULISTA", "casos": 7, "obitos": 1, "data": "21_abr"},
    {"munic": "CAMPOS DO JORDAO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "CANANEIA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "CAPAO BONITO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "CAPELA DO ALTO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "CARAGUATATUBA", "casos": 14, "obitos": 2, "data": "21_abr"},
    {"munic": "CARAPICUIBA", "casos": 101, "obitos": 3, "data": "21_abr"},
    {"munic": "CASTILHO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "CATANDUVA", "casos": 9, "obitos": 3, "data": "21_abr"},
    {"munic": "CEDRAL", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "CHAVANTES", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "CONCHAS", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "COTIA", "casos": 89, "obitos": 5, "data": "21_abr"},
    {"munic": "CRAVINHOS", "casos": 7, "obitos": 1, "data": "21_abr"},
    {"munic": "CRUZEIRO", "casos": 3, "obitos": 1, "data": "21_abr"},
    {"munic": "CUBATAO", "casos": 24, "obitos": 0, "data": "21_abr"},
    {"munic": "DIADEMA", "casos": 135, "obitos": 5, "data": "21_abr"},
    {"munic": "DRACENA", "casos": 3, "obitos": 2, "data": "21_abr"},
    {"munic": "DUARTINA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ELDORADO", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "ELIAS FAUSTO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "EMBU DAS ARTES", "casos": 60, "obitos": 5, "data": "21_abr"},
    {"munic": "EMBU-GUACU", "casos": 6, "obitos": 0, "data": "21_abr"},
    {"munic": "ESTIVA GERBI", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "FARTURA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "FERNANDOPOLIS", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "FERRAZ DE VASCONCELOS", "casos": 58, "obitos": 3, "data": "21_abr"},
    {"munic": "FRANCA", "casos": 6, "obitos": 0, "data": "21_abr"},
    {"munic": "FRANCISCO MORATO", "casos": 33, "obitos": 1, "data": "21_abr"},
    {"munic": "FRANCO DA ROCHA", "casos": 66, "obitos": 3, "data": "21_abr"},
    {"munic": "GARCA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "GUARARAPES", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "GUARAREMA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "GUARATINGUETA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "GUARUJA", "casos": 65, "obitos": 2, "data": "21_abr"},
    {"munic": "GUARULHOS", "casos": 330, "obitos": 28, "data": "21_abr"},
    {"munic": "GUZOLANDIA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "HORTOLANDIA", "casos": 10, "obitos": 0, "data": "21_abr"},
    {"munic": "IBIRA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "IBIUNA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "IEPE", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "IGARAPAVA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "IGARATA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "IGUAPE", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "ILHA COMPRIDA", "casos": 15, "obitos": 0, "data": "21_abr"},
    {"munic": "ILHA SOLTEIRA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ILHABELA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "INDAIATUBA", "casos": 9, "obitos": 0, "data": "21_abr"},
    {"munic": "IRACEMAPOLIS", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ITANHAEM", "casos": 6, "obitos": 1, "data": "21_abr"},
    {"munic": "ITAPECERICA DA SERRA", "casos": 51, "obitos": 1, "data": "21_abr"},
    {"munic": "ITAPETININGA", "casos": 7, "obitos": 1, "data": "21_abr"},
    {"munic": "ITAPEVA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ITAPEVI", "casos": 51, "obitos": 5, "data": "21_abr"},
    {"munic": "ITAPIRA", "casos": 15, "obitos": 3, "data": "21_abr"},
    {"munic": "ITAQUAQUECETUBA", "casos": 53, "obitos": 0, "data": "21_abr"},
    {"munic": "ITARARE", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ITATIBA", "casos": 4, "obitos": 1, "data": "21_abr"},
    {"munic": "ITATINGA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "ITU", "casos": 5, "obitos": 0, "data": "21_abr"},
    {"munic": "ITUPEVA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "JABOTICABAL", "casos": 9, "obitos": 2, "data": "21_abr"},
    {"munic": "JACAREI", "casos": 21, "obitos": 0, "data": "21_abr"},
    {"munic": "JACI", "casos": 6, "obitos": 0, "data": "21_abr"},
    {"munic": "JAGUARIUNA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "JALES", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "JANDIRA", "casos": 16, "obitos": 1, "data": "21_abr"},
    {"munic": "JARDINOPOLIS", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "JAU", "casos": 5, "obitos": 0, "data": "21_abr"},
    {"munic": "JOANOPOLIS", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "JOSE BONIFACIO", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "JUNDIAI", "casos": 53, "obitos": 6, "data": "21_abr"},
    {"munic": "JUNQUEIROPOLIS", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "JUQUITIBA", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "LARANJAL PAULISTA", "casos": 5, "obitos": 2, "data": "21_abr"},
    {"munic": "LEME", "casos": 4, "obitos": 2, "data": "21_abr"},
    {"munic": "LENCOIS PAULISTA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "LIMEIRA", "casos": 10, "obitos": 1, "data": "21_abr"},
    {"munic": "LINS", "casos": 6, "obitos": 2, "data": "21_abr"},
    {"munic": "LORENA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "LOUVEIRA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "MACATUBA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "MAIRINQUE", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "MAIRIPORA", "casos": 14, "obitos": 4, "data": "21_abr"},
    {"munic": "MARILIA", "casos": 8, "obitos": 1, "data": "21_abr"},
    {"munic": "MATAO", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "MAUA", "casos": 96, "obitos": 4, "data": "21_abr"},
    {"munic": "MIGUELOPOLIS", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "MINEIROS DO TIETE", "casos": 3, "obitos": 1, "data": "21_abr"},
    {"munic": "MIRANDOPOLIS", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "MIRASSOL", "casos": 6, "obitos": 0, "data": "21_abr"},
    {"munic": "MOCOCA", "casos": 2, "obitos": 1, "data": "21_abr"},
    {"munic": "MOGI DAS CRUZES", "casos": 124, "obitos": 8, "data": "21_abr"},
    {"munic": "MOGI GUACU", "casos": 9, "obitos": 1, "data": "21_abr"},
    {"munic": "MOGI MIRIM", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "MONGAGUA", "casos": 3, "obitos": 1, "data": "21_abr"},
    {"munic": "MONTE ALTO", "casos": 11, "obitos": 1, "data": "21_abr"},
    {"munic": "MONTE MOR", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "MORRO AGUDO", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "MORUNGABA", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "NAZARE PAULISTA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "NHANDEARA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "NOVA ODESSA", "casos": 2, "obitos": 1, "data": "21_abr"},
    {"munic": "OLIMPIA", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "ORLANDIA", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "OSASCO", "casos": 321, "obitos": 27, "data": "21_abr"},
    {"munic": "OURINHOS", "casos": 10, "obitos": 0, "data": "21_abr"},
    {"munic": "PARIQUERA-ACU", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "PAULINIA", "casos": 9, "obitos": 0, "data": "21_abr"},
    {"munic": "PAULISTANIA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "PEDERNEIRAS", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "PEDRA BELA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "PENAPOLIS", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "PERUIBE", "casos": 7, "obitos": 0, "data": "21_abr"},
    {"munic": "PIEDADE", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "PILAR DO SUL", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "PINDAMONHANGABA", "casos": 3, "obitos": 1, "data": "21_abr"},
    {"munic": "PINDORAMA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "PIRACAIA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "PIRACICABA", "casos": 25, "obitos": 2, "data": "21_abr"},
    {"munic": "PIRAJU", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "PIRAJUI", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "PIRATININGA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "POA", "casos": 28, "obitos": 3, "data": "21_abr"},
    {"munic": "PONTAL", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "POPULINA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "PORTO FELIZ", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "PORTO FERREIRA", "casos": 2, "obitos": 1, "data": "21_abr"},
    {"munic": "PRAIA GRANDE", "casos": 57, "obitos": 7, "data": "21_abr"},
    {"munic": "PRATANIA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "PRESIDENTE PRUDENTE", "casos": 8, "obitos": 2, "data": "21_abr"},
    {"munic": "PRESIDENTE VENCESLAU", "casos": 8, "obitos": 3, "data": "21_abr"},
    {"munic": "PROMISSAO", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "QUATA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "QUINTANA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "RANCHARIA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "REGISTRO", "casos": 4, "obitos": 1, "data": "21_abr"},
    {"munic": "RIBEIRAO PIRES", "casos": 35, "obitos": 1, "data": "21_abr"},
    {"munic": "RIBEIRAO PRETO", "casos": 84, "obitos": 5, "data": "21_abr"},
    {"munic": "RINCAO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "RINOPOLIS", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "RIO CLARO", "casos": 14, "obitos": 4, "data": "21_abr"},
    {"munic": "RIO GRANDE DA SERRA", "casos": 9, "obitos": 0, "data": "21_abr"},
    {"munic": "SALTO", "casos": 5, "obitos": 0, "data": "21_abr"},
    {"munic": "SALTO DE PIRAPORA", "casos": 6, "obitos": 0, "data": "21_abr"},
    {"munic": "SANTA BARBARA D'OESTE", "casos": 2, "obitos": 1, "data": "21_abr"},
    {"munic": "SANTA BRANCA", "casos": 2, "obitos": 1, "data": "21_abr"},
    {"munic": "SANTA CRUZ DO RIO PARDO", "casos": 6, "obitos": 0, "data": "21_abr"},
    {"munic": "SANTA GERTRUDES", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "SANTA ISABEL", "casos": 3, "obitos": 1, "data": "21_abr"},
    {"munic": "SANTA LUCIA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "SANTANA DE PARNAIBA", "casos": 63, "obitos": 1, "data": "21_abr"},
    {"munic": "SANTO ANDRE", "casos": 270, "obitos": 14, "data": "21_abr"},
    {"munic": "SANTO ANTONIO DA ALEGRIA", "casos": 1, "obitos": 1, "data": "21_abr"},
    {"munic": "SANTOS", "casos": 322, "obitos": 19, "data": "21_abr"},
    {"munic": "SAO BERNARDO DO CAMPO", "casos": 310, "obitos": 20, "data": "21_abr"},
    {"munic": "SAO CAETANO DO SUL", "casos": 110, "obitos": 4, "data": "21_abr"},
    {"munic": "SAO CARLOS", "casos": 9, "obitos": 2, "data": "21_abr"},
    {"munic": "SAO JOAO DA BOA VISTA", "casos": 5, "obitos": 0, "data": "21_abr"},
    {"munic": "SAO JOAQUIM DA BARRA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "SAO JOSE DO RIO PARDO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "SAO JOSE DO RIO PRETO", "casos": 72, "obitos": 8, "data": "21_abr"},
    {"munic": "SAO JOSE DOS CAMPOS", "casos": 138, "obitos": 3, "data": "21_abr"},
    {"munic": "SAO LOURENCO DA SERRA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "SAO MANUEL", "casos": 4, "obitos": 1, "data": "21_abr"},
    {"munic": "SAO MIGUEL ARCANJO", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "SAO PAULO", "casos": 10342, "obitos": 753, "data": "21_abr"},
    {"munic": "SAO PEDRO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "SAO ROQUE", "casos": 8, "obitos": 0, "data": "21_abr"},
    {"munic": "SAO SEBASTIAO", "casos": 6, "obitos": 2, "data": "21_abr"},
    {"munic": "SAO VICENTE", "casos": 59, "obitos": 1, "data": "21_abr"},
    {"munic": "SERRANA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "SERTAOZINHO", "casos": 9, "obitos": 1, "data": "21_abr"},
    {"munic": "SOROCABA", "casos": 56, "obitos": 12, "data": "21_abr"},
    {"munic": "SUMARE", "casos": 5, "obitos": 0, "data": "21_abr"},
    {"munic": "SUZANO", "casos": 82, "obitos": 7, "data": "21_abr"},
    {"munic": "TABOAO DA SERRA", "casos": 124, "obitos": 8, "data": "21_abr"},
    {"munic": "TANABI", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "TAQUARITINGA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "TAQUARITUBA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "TARABAI", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "TATUI", "casos": 7, "obitos": 0, "data": "21_abr"},
    {"munic": "TAUBATE", "casos": 7, "obitos": 0, "data": "21_abr"},
    {"munic": "TERRA ROXA", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "TUPA", "casos": 2, "obitos": 0, "data": "21_abr"},
    {"munic": "UBATUBA", "casos": 3, "obitos": 0, "data": "21_abr"},
    {"munic": "VALINHOS", "casos": 14, "obitos": 3, "data": "21_abr"},
    {"munic": "VARGEM GRANDE PAULISTA", "casos": 10, "obitos": 3, "data": "21_abr"},
    {"munic": "VARZEA PAULISTA", "casos": 4, "obitos": 0, "data": "21_abr"},
    {"munic": "VINHEDO", "casos": 14, "obitos": 0, "data": "21_abr"},
    {"munic": "VISTA ALEGRE DO ALTO", "casos": 1, "obitos": 0, "data": "21_abr"},
    {"munic": "VOTORANTIM", "casos": 6, "obitos": 1, "data": "21_abr"},
    {"munic": "VOTUPORANGA", "casos": 9, "obitos": 0, "data": "21_abr"},
    {"munic": "OUTRO ESTADO", "casos": 14, "obitos": 0, "data": "21_abr"},
    {"munic": "OUTRO PAIS", "casos": 42, "obitos": 0, "data": "21_abr"},
    {"munic": "IGNORADO", "casos": 7, "obitos": 0, "data": "21_abr"}
]


def create_dir():
    """
    Cria o diretório `data`, onde serão guardados os arquivos.
    Este diretório é sobrescrito cada vez que o script é rodado.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def strip_accents(text):
    """
    Retorna `string` sem acentuação, considerando que os nomes
    dos municípios são grafados com e sem acento
    """
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass
    text = unicodedata.normalize('NFKD', text)\
        .encode('ascii', 'ignore')\
        .decode('utf-8')
    return str(text)


def normalize_cities():
    """
    Pega a base de cidades no GitHub e aplica a `desacentuação`
    """
    base = 'https://raw.githubusercontent.com/rodolfo-viana/dailylog/master'
    path = '/misc/cod_ibge_municipios_sp.csv'
    url = base + path
    cities = pd.read_csv(url)
    cities['NM_NORMALIZ'] = cities['NM_MUNICIP']\
        .apply(lambda x: strip_accents(x)
               .upper().replace(" ", "")
               .replace("-", "")
               .replace("'", ""))
    return cities


def read_excel_sheets(xls_path):
    """
    Busca o `xlsx` no GitHub da Seade, ignora as datas com dados
    malformatados (relacionados na variável `missing_date` acima),
    faz o parsing dos demais, inclui os dados malformatados,
    formata o conjunto -- inclusive com a `desacentuação` --,
    vincula à base de municípios do IBGE e salva

    OUTPUT: `secretaria_sp_municipios_dia.csv`
    """
    cities = normalize_cities()
    missing_df = pd.DataFrame(missing_dates)
    xl = pd.ExcelFile(xls_path)
    for i in xl.sheet_names:
        if i not in ['04_abr', '05_abr', '21_abr']:
            sheet = pd.read_excel(xl, sheet_name=i).fillna(0)
            sheet.rename(columns={
                sheet.columns[0]: "munic",
                sheet.columns[1]: "casos",
                sheet.columns[2]: "obitos"
            }, inplace=True)
            sheet["data"] = i
            sheet = sheet[sheet["casos"].apply(lambda x: str(x).isdigit())]
            sheet["obitos"] = sheet["obitos"].apply(lambda x: str(x)
                                                    .replace("-", "0"))
            sheet["casos"] = sheet["casos"].apply(lambda x: str(x)
                                                  .replace("-", "0"))
            sheet["casos"] = sheet["casos"].astype(int)
            sheet["obitos"] = sheet["obitos"].astype(float).astype(int)
            to_drop = sheet[sheet["munic"].isin(IGN_LIST)].index
            sheet.drop(to_drop, inplace=True)
            sheet.to_csv(f'temp_{i}.csv', index=False)
    quase_final = pd.concat(
        [pd.read_csv(f) for f in glob.glob(f'temp_*.csv')]
    )
    final = pd.concat([quase_final, missing_df], sort=False)
    final['munic'] = final['munic'].apply(lambda x: strip_accents(x)
                                          .upper().replace(" ", "")
                                          .replace("-", "").replace("'", ""))
    final["munic"] = final["munic"].apply(lambda x: str(x)
                                          .replace("MOJIMIRIM", "MOGIMIRIM"))
    final["munic"] = final["munic"].apply(lambda x: str(x)
                                          .replace("MOGGUACU", "MOGIGUACU"))
    df = pd.merge(
        final, cities,
        left_on="munic",
        right_on="NM_NORMALIZ",
        how='left'
    )
    df.replace(regex=DICT_DATE, inplace=True)
    df['data'] = pd.to_datetime(df['data'])
    df = df[["CD_GEOCMU", "NM_MUNICIP", "data", "casos", "obitos"]]
    df['NM_MUNICIP'] = df['NM_MUNICIP'].fillna("OUTROS LOCAIS")
    df['CD_GEOCMU'] = df['CD_GEOCMU'].fillna(9999999).astype(int)
    df = df.groupby(['CD_GEOCMU', 'NM_MUNICIP', 'data'])\
        .agg({"casos": "sum", "obitos": "sum"})\
        .reset_index()
    df.rename(columns={
        "CD_GEOCMU": "cod_ibge",
        "NM_MUNICIP": 'municipio'
    }, inplace=True)
    df.to_csv('secretaria_sp_municipios_dia.csv', index=False)


if __name__ == '__main__':
    create_dir()
    os.chdir(DATA_DIR)
    read_excel_sheets(URL)
    os.system('rm temp_*')
