/* Query 2: vendas por tipo de mídia */
SELECT
  m.Name tipo,
  q_m.quantidade
FROM (SELECT
      t.MediaTypeId,
      COUNT(t.MediaTypeId) quantidade
      FROM Invoice i
      JOIN InvoiceLine il
        ON i.InvoiceId = il.InvoiceId
      JOIN TRACK t
        ON il.TrackId = t.TrackId
      GROUP BY 1) q_m
JOIN MediaType m
  ON q_m.MediaTypeId = m.MediaTypeId
GROUP BY 1
ORDER BY 2 DESC;