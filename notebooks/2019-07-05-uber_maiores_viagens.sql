/*
VARIAÇÃO DE TEMPO MÉDIO DE VIAGEM
-------------------------------
Base: view_uber_horadodia
Objetivo: descobrir tempo médio e variação no tempo de viagem entre dois pontos
Detalhamento: de 2016 a 2018; recorte temporal por dia útil
Cliente: Gian Dias, produtor da Globo SP
Projeto: Anda SP
Autor: Rodolfo Viana
Data: 5.jul.2019
*/

WITH ano_2018 as (
  SELECT
    CONCAT(NomeZonaOrigem,"-",NomeZonaDestino) as trajeto_2018,
    AVG(TempoMedio) as media_2018
  FROM
    `tvg-bd-governo.mobilidade_sp_prd.view_uber_horadodia`
  WHERE
    Recorte = 'diasuteis'
    AND ano = 2018
  GROUP BY trajeto_2018
), ano_2017 as (
  SELECT
    CONCAT(NomeZonaOrigem,"-",NomeZonaDestino) as trajeto_2017,
  AVG(TempoMedio) as media_2017
  FROM
    `tvg-bd-governo.mobilidade_sp_prd.view_uber_horadodia`
  WHERE
    Recorte = 'diasuteis'
    AND ano = 2017
  GROUP BY trajeto_2017
), ano_2016 as (
  SELECT
    CONCAT(NomeZonaOrigem,"-",NomeZonaDestino) as trajeto_2016,
  AVG(TempoMedio) as media_2016
  FROM
    `tvg-bd-governo.mobilidade_sp_prd.view_uber_horadodia`
  WHERE
    Recorte = 'diasuteis'
    AND ano = 2016
  GROUP BY trajeto_2016
)
SELECT
  trajeto_2016 as trajeto,
  AVG(media_2016) as periodo_2016,
  AVG(ano_2017.media_2017) as periodo_2017,
  ((AVG(ano_2017.media_2017)/AVG(ano_2016.media_2016)-1)*100) as var_percentual_2016_2017,
  AVG(ano_2018.media_2018) as periodo_2018,
  ((AVG(ano_2018.media_2018)/AVG(ano_2017.media_2017)-1)*100) as var_percentual_2017_2018,
  ((AVG(ano_2018.media_2018)/AVG(ano_2016.media_2016)-1)*100) as var_percentual_2016_2018
FROM
  ano_2016
JOIN
  ano_2017
  ON ano_2017.trajeto_2017 = ano_2016.trajeto_2016
JOIN
  ano_2018
  on ano_2018.trajeto_2018 = ano_2017.trajeto_2017
GROUP BY trajeto_2016
ORDER BY periodo_2018 DESC
LIMIT 100
