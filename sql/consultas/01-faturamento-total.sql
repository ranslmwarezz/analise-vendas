-- Quanto a empresa faturou em 2025?

SELECT SUM((iv.quantidade * iv.preco_unitario) - iv.desconto) AS faturamento_total
FROM itens_venda iv
INNER JOIN vendas v ON iv.venda_id = v.id
WHERE v.status = 'CONCLUIDA' AND EXTRACT(YEAR FROM v.data_hora) = 2025;