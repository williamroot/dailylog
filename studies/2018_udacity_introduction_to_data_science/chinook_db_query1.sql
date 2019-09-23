/* QUERY 1: quanto cada gênero faturou por ano */
SELECT
  g.Name genero,
  strftime('%Y', i.InvoiceDate) ano,
  SUM(il.UnitPrice * il.Quantity) faturamento
FROM Invoice i
JOIN InvoiceLine il
  ON i.InvoiceId = il.InvoiceId
JOIN Track t
  ON il.TrackId = t.TrackId
JOIN Genre g
  ON t.GenreId = g.GenreId
GROUP BY 1,
         2
ORDER BY 1, 2 DESC;