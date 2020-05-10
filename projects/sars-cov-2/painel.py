from google.oauth2 import service_account
import pandas_gbq as gpd
import pandas as pd
import streamlit as st

# Pega credential (`json` gerado no modo `conta de serviço`) e ID do projeto no BQ
PROJECT_ID = "tvg-bd-governo"
CREDENTIALS = service_account.Credentials.from_service_account_file(
    'credentials/gcloud_bq_py.json',
)


@st.cache
def fetch_data(sql):
	"""
	Conecta com o BQ, roda uma query de SQL e retorna em `dataframe`
	"""
	df = gpd.read_gbq(sql, project_id=PROJECT_ID, credentials=CREDENTIALS)
	return df


# Salva query de SQL numa variável
obitos = """
WITH t1 as (
  SELECT CAST(data as date) data, 
    uf, 
    CASE
        WHEN uf = "AC" THEN "Acre"
        WHEN uf = "AL" THEN "Alagoas"
        WHEN uf = "AP" THEN "Amapá"
        WHEN uf = "AM" THEN "Amazonas"
        WHEN uf = "BA" THEN "Bahia"
        WHEN uf = "CE" THEN "Ceará"
        WHEN uf = "DF" THEN "Distrito Federal"
        WHEN uf = "ES" THEN "Espírito Santo"
        WHEN uf = "GO" THEN "Goiás"
        WHEN uf = "MA" THEN "Maranhão"
        WHEN uf = "MT" THEN "Mato Grosso"
        WHEN uf = "MS" THEN "Mato Grosso do Sul"
        WHEN uf = "MG" THEN "Minas Gerais"
        WHEN uf = "PA" THEN "Pará"
        WHEN uf = "PB" THEN "Paraíba"
        WHEN uf = "PR" THEN "Paraná"
        WHEN uf = "PE" THEN "Pernambuco"
        WHEN uf = "PI" THEN "Piauí"
        WHEN uf = "RJ" THEN "Rio de Janeiro"
        WHEN uf = "RN" THEN "Rio Grande do Norte"
        WHEN uf = "RS" THEN "Rio Grande do Sul"
        WHEN uf = "RO" THEN "Rondônia"
        WHEN uf = "RR" THEN "Roraima"
        WHEN uf = "SC" THEN "Santa Catarina"
        WHEN uf = "SP" THEN "São Paulo"
        WHEN uf = "SE" THEN "Sergipe"
        WHEN uf = "TO" THEN "Tocantins"
    END estado,
    casos, 
    obitos 
  FROM `tvg-bd-governo.covid19.ministerio_uf_diario`
), t2 as (
  SELECT 
    CAST(data as date) data, 
    uf, 
    obitos_cartorio 
  FROM `tvg-bd-governo.covid19.cartorios`
) SELECT
  t1.data,
  t1.uf,
  t1.estado,
  t1.casos,
  t1.obitos obitos_ministerio,
  IFNULL(t2.obitos_cartorio, 0) obitos_cartorio
FROM t1
LEFT JOIN t2 ON t1.data = t2.data AND t1.uf = t2.uf
ORDER BY 1,2
"""

# Salva tabela em variável
compara_obitos = fetch_data(obitos)

# Formata os dados
compara_obitos['data'] = pd.to_datetime(compara_obitos['data'])
periodo = compara_obitos['data'].dt.to_period("M")
grupo = compara_obitos.groupby([periodo, 'estado']).sum().reset_index()
grupo = grupo[['data', 'estado', 'obitos_ministerio', 'obitos_cartorio']]
brasil = grupo.groupby('data').sum().reset_index()
brasil['estado'] = 'Brasil'
df = pd.concat([brasil, grupo])

# Cria o widget de seleção de estado e filtra o `dataframe`
locais = df['estado'].unique().tolist()
selecao = st.selectbox(
    'Escolha o local',
    locais
)
df = df[df['estado'] == selecao]

# Formata o `dataframe` para gráfico
df = df[['data', 'obitos_ministerio', 'obitos_cartorio']]
df['data'] = df['data'].astype(str)
df = df.set_index('data')

# Cria gráfico
st.line_chart(df)

# Cria texto
st.markdown(f"Até o momento, **{selecao}** acumula **{df['obitos_ministerio'].sum()} óbitos** "
	+ f"segundo o Ministério da Saúde, e **{df['obitos_cartorio'].sum()} óbitos** de acordo com "
	+ "os registros em cartórios. Cabe ressaltar que o Ministério considera óbitos por covid-19 "
	+ "somente os casos confirmados, enquanto os cartórios consideram confirmados e suspeitos.")