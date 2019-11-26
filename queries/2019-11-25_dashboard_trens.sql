WITH t as (
  SELECT
    EXTRACT(date from hora_geracao) as data,
    EXTRACT(hour from hora_geracao) as hora,
    linha_nome,
    status,
    CASE
      WHEN lower(descricao) LIKE "%obra%de modernização%" or lower(descricao) LIKE "%obras%" THEN "Obras"
      WHEN lower(descricao) LIKE "%falha de trem%" THEN "Falhas no trem"
      WHEN lower(descricao) LIKE "%normalização%" THEN "Tempo de normalização"
      WHEN lower(descricao) LIKE "%sistema de energia%" THEN "Problemas no sistema de energia"
      WHEN lower(descricao) LIKE "%alagamento%" THEN "Alagamentos"
      WHEN lower(descricao) LIKE "%vandalismo%" THEN "Vandalismo"
      WHEN lower(descricao) LIKE "%serviço%programado%" THEN "Serviços programados"
      WHEN lower(descricao) LIKE "%manutenção%" THEN "Manutenção"
      WHEN lower(descricao) LIKE "%problema%técnico%" THEN "Problemas técnicos"
      WHEN lower(descricao) LIKE "%equipamento%de via%" THEN "Problemas em equipamentos de via"
      WHEN lower(descricao) LIKE "%pessoa%na via%" THEN "Pessoas na via"
      WHEN lower(descricao) LIKE "%atendimento de usuário%" THEN "Atendimento de usuário"
      WHEN lower(descricao) LIKE "%interferência na%via%" THEN "Interferência na via"
      WHEN lower(descricao) = "" THEN "Sem informações"
      ELSE "Outros"
    END as descritivo,
    EXTRACT(dayofweek from hora_geracao) as dia_semana,
    TIME_DIFF(MAX(CAST(hora_geracao as time)), MIN(CAST(hora_geracao as time)), minute) as minutos
  FROM
    `tvg-bd-governo.mobilidade_sp_prd.view_cptm`
  WHERE
    status not in ("Operações Encerradas", "Operacão Encerrada")
    AND linha_nome is not null
  GROUP BY 1, 2, 3, 4, 5, 6
)
SELECT
  linha_nome,
  data,
  CASE
    WHEN dia_semana = 1 THEN "Domingo"
    WHEN dia_semana = 2 THEN "Segunda"
    WHEN dia_semana = 3 THEN "Terça"
    WHEN dia_semana = 4 THEN "Quarta"
    WHEN dia_semana = 5 THEN "Quinta"
    WHEN dia_semana = 6 THEN "Sexta"
    ELSE "Sábado"
  END as dia_da_semana,
  CASE
    WHEN hora BETWEEN 0 AND 1 THEN "00:00 - 01:59"
    WHEN hora BETWEEN 2 AND 3 THEN "02:00 - 03:59"
    WHEN hora BETWEEN 4 AND 5 THEN "04:00 - 05:59"
    WHEN hora BETWEEN 6 AND 7 THEN "06:00 - 07:59"
    WHEN hora BETWEEN 8 AND 9 THEN "08:00 - 09:59"
    WHEN hora BETWEEN 10 AND 11 THEN "10:00 - 11:59"
    WHEN hora BETWEEN 12 AND 13 THEN "12:00 - 13:59"
    WHEN hora BETWEEN 14 AND 15 THEN "14:00 - 15:59"
    WHEN hora BETWEEN 16 AND 17 THEN "16:00 - 17:59"
    WHEN hora BETWEEN 18 AND 19 THEN "18:00 - 19:59"
    WHEN hora BETWEEN 20 AND 21 THEN "20:00 - 21:59"
    ELSE "22:00 - 23:59"
  END as hora_do_dia,
  CASE
    WHEN status = "Operação Normal" THEN "Operação normal"
    WHEN status = "Velocidade Reduzida" THEN "Velocidade reduzida"
    WHEN status = "Operação Parcial" THEN "Operação parcial"
    ELSE "Dados indisponíveis"
  END as status,
  descritivo,
  SUM(minutos) as quantidade
FROM
  t
GROUP BY
  2, 4, 1, 3, 5, 6
