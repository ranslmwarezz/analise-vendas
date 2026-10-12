-- Quais categorias geraram mais faturamento em 2025?
SELECT c.nome, SUM((it.quantidade * it.preco_unitario) - it.desconto) AS faturamento_categoria
FROM produtos p
INNER JOIN itens_venda it
ON p.id = it.produto_id
INNER JOIN vendas v
ON it.venda_id = v.id
INNER JOIN categorias c
ON p.categoria_id = c.id
WHERE v.status = 'CONCLUIDA' AND EXTRACT(YEAR FROM v.data_hora) = 2025
GROUP BY c.nome
ORDER BY faturamento_categoria DESC;