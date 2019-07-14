/*
MINUTOS DE OPERAÇÃO
-------------------------------
Base: view_metro
Objetivo: descobrir o tempo, na soma de minutos, de cada status de operação de cada linha
Cliente: Gian Dias, produtor da Globo SP
Projeto: Anda SP
Autor: Rodolfo Viana
Data: 3.jul.2019
*/

WITH t as (
  SELECT
    linha_nome,
    EXTRACT(date from atualizacao) as data,
    EXTRACT(hour from atualizacao) as hora,
    CASE
    WHEN situacao in ("Operação Encerrada", "Operações Encerradas") THEN "Operação encerrada"
      WHEN situacao = "Operação Normal" THEN "Operação normal"
      WHEN situacao = "Velocidade Reduzida" THEN "Operação com velocidade reduzida"
      WHEN situacao = "Operação Parcial" THEN "Operação parcial"
      WHEN situacao in ("Operação Paralisada", "Paralisada") THEN "Operação paralisada"
      ELSE "Sem dados"
    END as status,
    TIME_DIFF(MAX(CAST(atualizacao as time)), MIN(CAST(atualizacao as time)), minute) as minutos,
  FROM
    `tvg-bd-governo.mobilidade_sp_prd.view_metro`
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
