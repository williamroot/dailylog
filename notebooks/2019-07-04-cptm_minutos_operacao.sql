/*
MINUTOS DE OPERAÇÃO
-------------------------------
Base: view_cptm
Objetivo: descobrir o tempo, na soma de minutos, de cada status de operação de cada linha
Cliente: Gian Dias, produtor da Globo SP
Projeto: Anda SP
Autor: Rodolfo Viana
Data: 4.jul.2019
*/

WITH t as (
  SELECT
    linha_nome,
    EXTRACT(date from hora_geracao) as data,
    EXTRACT(hour from hora_geracao) as hora,
    status,
    TIME_DIFF(MAX(CAST(hora_geracao as time)), MIN(CAST(hora_geracao as time)), minute) as minutos
  FROM
    `tvg-bd-governo.mobilidade_sp_prd.view_cptm`
  GROUP BY 1, 2, 3, 4
)
SELECT
  t.linha_nome,
  EXTRACT(month from t.data) as mes,
  t.status,
  SUM(t.minutos) as minutos
FROM
  t
GROUP BY 1, 2, 3
