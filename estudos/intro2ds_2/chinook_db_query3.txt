/* Query 3: bandas de rock que os brasileiros consomem */
SELECT
  aa.Name bandas,
  COUNT(aa.Name) vendas
FROM Customer c
JOIN Invoice i
  ON c.CustomerId = i.CustomerId
JOIN InvoiceLine il
  ON i.InvoiceId = il.InvoiceId
JOIN Track t
  ON il.TrackId = t.TrackId
JOIN Album a
  ON t.AlbumId = a.AlbumId
JOIN Artist aa
  ON a.ArtistId = aa.ArtistId
JOIN Genre g
  ON t.GenreId = g.GenreId
WHERE g.Name = 'Rock'
AND c.Country = 'Brazil'
GROUP BY 1
ORDER BY 2 DESC;