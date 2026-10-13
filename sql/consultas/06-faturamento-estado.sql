-- Quais estados geraram mais faturamento em 2025?
-- Qual o faturamento geral?
SELECT 
    CASE 
    WHEN GROUPING(c.estado) = 1 THEN 'Total Geral'
    ELSE c.estado
    END AS estado,
    SUM(it.quantidade * it.preco_unitario - it.desconto) AS faturamento_estado
FROM clientes c
INNER JOIN vendas v ON c.id = v.cliente_id
INNER JOIN itens_venda it ON v.id = it.venda_id
WHERE EXTRACT(YEAR FROM v.data_hora) = 2025 AND v.status = 'CONCLUIDA'
GROUP BY ROLLUP(c.estado)
ORDER BY GROUPING(c.estado), faturamento_estado DESC;
