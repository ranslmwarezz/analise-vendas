-- Quais vendedores geraram mais faturamento e quantas vendas foram concluíram em 2025?
SELECT v.nome, COUNT(DISTINCT vd.id) vendas_feitas, SUM(it.quantidade * it.preco_unitario - it.desconto) AS faturamento_vendedor
FROM vendedores v
INNER JOIN vendas vd ON v.id = vd.vendedor_id
INNER JOIN itens_venda it ON vd.id = it.venda_id
WHERE vd.status = 'CONCLUIDA' AND EXTRACT(YEAR FROM vd.data_hora) = 2025
GROUP BY v.id, v.nome
ORDER BY faturamento_vendedor DESC;