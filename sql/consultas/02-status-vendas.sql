-- Quantas vendas existem em cada status?
SELECT v.status, COUNT(*) AS vendas_por_status
FROM vendas v
GROUP BY v.status;
