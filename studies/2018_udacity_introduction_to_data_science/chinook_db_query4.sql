/* Query 4: músicas mais repetidas (10 repetições ou mais) em playlists */
SELECT
  t.Name,
  COUNT(pt.TrackId) repeticoes
FROM PlaylistTrack pt
JOIN Track t
  ON pt.TrackId = t.TrackId
GROUP BY 1
HAVING repeticoes >= 10
ORDER BY 2 DESC;