-- Quais são os 10 produtos que geraram mais faturamento em 2025?
SELECT p.nome, SUM((it.quantidade * it.preco_unitario) - it.desconto) AS faturamento_produto
FROM produtos p
INNER JOIN itens_venda it
ON p.id = it.produto_id
INNER JOIN vendas v
ON it.venda_id = v.id
WHERE v.status = 'CONCLUIDA' AND EXTRACT(YEAR FROM v.data_hora) = 2025
GROUP BY p.id, p.nome
ORDER BY faturamento_produto DESC
LIMIT 10;