/*
DASHBOARD DO BOLSA FAMÍLIA
--------------------------
Bases: view_bolsa_familia_pagamentos, view_bolsa_familia_saques
Objetivo: criar a base do painel interativo do Bolsa Família, feito no DataStudio
Autor: Rodolfo Viana
Data: 4.mar.2019
*/

WITH pagamentos_agreg as (
  SELECT
    uf,
    codigo_municipio_siafi,
    nome_municipio_siafi,
    ano_competencia,
    mes_competencia,
    CAST(SUM(valor_beneficio) as FLOAT64) as valor_pgto,
    COUNT(DISTINCT nis_beneficiario) as benef_pgto,
    CASE
      WHEN mes_competencia < 10
      THEN CONCAT(CAST(ano_competencia as STRING), CAST(0 as STRING), CAST(mes_competencia as STRING))
      ELSE CONCAT(CAST(ano_competencia as STRING), CAST(mes_competencia as STRING))
    END as periodo_pgto
  FROM `tvg-bd-governo.transparencia.view_bolsa_familia_pagamentos`
  GROUP BY
    uf,
    codigo_municipio_siafi,
    nome_municipio_siafi,
    ano_competencia,
    mes_competencia,
    periodo_pgto
), saques_agreg as (
  SELECT
    uf,
    codigo_municipio_siafi,
    nome_municipio_siafi,
    ano_competencia,
    mes_competencia,
    CAST(SUM(valor_beneficio) as FLOAT64) as valor_saque,
    COUNT(DISTINCT nis_beneficiario) as benef_saque,
    CASE
      WHEN mes_competencia < 10
      THEN CONCAT(CAST(ano_competencia as STRING), CAST(0 as STRING), CAST(mes_competencia as STRING))
      ELSE CONCAT(CAST(ano_competencia as STRING), CAST(mes_competencia as STRING))
    END as periodo_saque
  FROM `tvg-bd-governo.transparencia.view_bolsa_familia_saques`
  GROUP BY
    uf,
    codigo_municipio_siafi,
    nome_municipio_siafi,
    ano_competencia,
    mes_competencia,
    periodo_saque
)
SELECT
  pgto.uf,
  pgto.codigo_municipio_siafi,
  pgto.nome_municipio_siafi,
  pgto.periodo_pgto,
  pgto.benef_pgto,
  pgto.valor_pgto,
  saque.benef_saque,
  saque.valor_saque,
  pgto.benef_pgto - saque.benef_saque as benef_diferenca,
  pgto.valor_pgto - saque.valor_saque as valor_diferenca
FROM pagamentos_agreg as pgto
JOIN saques_agreg as saque
  ON pgto.codigo_municipio_siafi = saque.codigo_municipio_siafi
  AND pgto.periodo_pgto = saque.periodo_saque
GROUP BY
  pgto.uf,
  pgto.codigo_municipio_siafi,
  pgto.nome_municipio_siafi,
  pgto.ano_competencia,
  pgto.mes_competencia,
  pgto.periodo_pgto,
  pgto.valor_pgto,
  pgto.benef_pgto,
  saque.valor_saque,
  saque.benef_saque
