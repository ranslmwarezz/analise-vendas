
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    tipo_pessoa VARCHAR(2) NOT NULL,
    documento VARCHAR(18) NOT NULL UNIQUE,
    cidade VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(100),
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT clientes_tipo_pessoa_check
        CHECK (tipo_pessoa IN ('PF', 'PJ'))
);

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descricao TEXT,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    categoria_id INTEGER NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    estoque_atual INTEGER NOT NULL DEFAULT 0,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT produtos_categoria_id_fk
        FOREIGN KEY (categoria_id)
        REFERENCES categorias(id),

    CONSTRAINT produtos_preco_check
        CHECK (preco >= 0),

    CONSTRAINT produtos_estoque_atual_check
        CHECK (estoque_atual >= 0)
);

CREATE TABLE vendedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    documento VARCHAR(18) NOT NULL UNIQUE,
    telefone VARCHAR(15),
    email VARCHAR(100),
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    vendedor_id INTEGER NOT NULL,
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    forma_pagamento VARCHAR(30) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'PENDENTE',

    CONSTRAINT vendas_cliente_id_fk
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id),

    CONSTRAINT vendas_vendedor_id_fk
        FOREIGN KEY (vendedor_id)
        REFERENCES vendedores(id),

    CONSTRAINT vendas_status_check
        CHECK (status IN ('PENDENTE', 'CONCLUIDA', 'CANCELADA')),

    CONSTRAINT vendas_forma_pagamento_check
        CHECK (
            forma_pagamento IN (
                'DINHEIRO',
                'PIX',
                'BOLETO',
                'DEBITO',
                'CREDITO'
            )
        )
);

CREATE TABLE itens_venda (
    id SERIAL PRIMARY KEY,
    venda_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(10, 2) NOT NULL,
    desconto NUMERIC(10, 2) NOT NULL DEFAULT 0,

    CONSTRAINT itens_venda_venda_fk
        FOREIGN KEY (venda_id)
        REFERENCES vendas(id)
        ON DELETE CASCADE,

    CONSTRAINT itens_venda_produto_fk
        FOREIGN KEY (produto_id)
        REFERENCES produtos(id),

    CONSTRAINT itens_venda_quantidade_check
        CHECK (quantidade > 0),

    CONSTRAINT itens_venda_preco_check
        CHECK (preco_unitario >= 0),

    CONSTRAINT itens_venda_desconto_check
        CHECK (
            desconto >= 0
            AND desconto <= (quantidade * preco_unitario)
        )
);