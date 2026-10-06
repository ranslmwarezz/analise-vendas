-- Qual foi o faturamento de cada mês em 2025?
SELECT 
CASE EXTRACT(MONTH FROM v.data_hora)
WHEN 1 THEN 'Janeiro'
WHEN 2 THEN 'Fevereiro'
WHEN 3 THEN 'Março'
WHEN 4 THEN 'Abril'
WHEN 5 THEN 'Maio'
WHEN 6 THEN 'Junho'
WHEN 7 THEN 'Julho'
WHEN 8 THEN 'Agosto'
WHEN 9 THEN 'Setembro'
WHEN 10 THEN 'Outubro' 
WHEN 11 THEN 'Novembro'
WHEN 12 THEN 'Dezembro'
END AS mes, SUM((it.quantidade * it.preco_unitario) - it.desconto) AS faturamento_mes
FROM itens_venda it
INNER JOIN vendas v
ON it.venda_id = v.id
WHERE v.status = 'CONCLUIDA' AND EXTRACT(YEAR FROM v.data_hora) = 2025
GROUP BY mes
ORDER BY mes ASC;