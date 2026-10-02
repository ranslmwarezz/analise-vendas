import calendar
import random
from datetime import datetime

from faker import Faker


print("Gerador de dados - Análise de Vendas")

random.seed(42)
Faker.seed(42)
faker = Faker("pt_BR")

QUANTIDADE_CLIENTES = 1000
QUANTIDADE_VENDEDORES = 15
QUANTIDADE_VENDAS = 10000

categorias = [
    "Eletrônicos",
    "Informática",
    "Acessórios",
    "Periféricos",
    "Celulares",
    "Escritório",
    "Áudio e Vídeo",
    "Games"
]

produtos = {
    "Eletrônicos": [
        'LG OLED C4 55"',
        'LG OLED C4 65"',
        'LG OLED C4 77"',
        'LG QNED85T 55"',
        'LG QNED85T 65"',
        'Samsung QN90D 55"',
        'Samsung QN90D 65"',
        'Samsung DU8000 50"',
        'Samsung DU8000 55"',
        'TCL C655 55"'
    ],
    "Informática": [
        "Dell Inspiron 15 3530",
        "Lenovo IdeaPad 1i 15",
        "Lenovo IdeaPad Slim 3i",
        "ASUS Vivobook 15 X1504",
        "Acer Aspire 5 A515-57",
        "Acer Nitro V 15",
        "ASUS TUF Gaming F15",
        "AMD Ryzen 5 5600G",
        "AMD Ryzen 7 5700X",
        "Intel Core i5-12400F"
    ],
    "Acessórios": [
        "Apple Adaptador de Energia USB-C de 20W",
        "Samsung Carregador Super Fast Charging de 25W",
        "Baseus Metal Gleam Series 8-in-1",
        "UGREEN Revodok 105",
        "Anker 735 GaNPrime 65W",
        "UGREEN USB-C para USB-C 100W 2m",
        "Baseus Cafule USB-C 100W",
        "TP-Link UB500 Bluetooth 5.0",
        "TP-Link Archer T3U Plus",
        "Apple EarPods USB-C"
    ],
    "Periféricos": [
        "Logitech MX Master 3S",
        "Logitech G502 HERO",
        "Logitech G PRO X Superlight 2",
        "Logitech K380",
        "Logitech G915 TKL",
        "Logitech C920e",
        "Logitech G435",
        "Razer DeathAdder V3",
        "Razer BlackShark V2",
        "HyperX Alloy Origins Core"
    ],
    "Celulares": [
        "Apple iPhone 16 128GB",
        "Apple iPhone 16 Plus 128GB",
        "Apple iPhone 16 Pro 128GB",
        "Apple iPhone 16 Pro Max 256GB",
        "Samsung Galaxy S25 128GB",
        "Samsung Galaxy S25+ 256GB",
        "Samsung Galaxy S25 Ultra 256GB",
        "Samsung Galaxy A56 5G",
        "Samsung Galaxy A36 5G",
        "Motorola Edge 50 Fusion 256GB"
    ],
    "Escritório": [
        "Epson EcoTank L3250",
        "Epson EcoTank L4260",
        "Epson EcoTank L5590",
        "Epson EcoTank L6270",
        "Epson EcoTank L6490",
        "Canon MegaTank G3110",
        "Canon MegaTank G6010",
        "Canon PIXMA G3170",
        "HP OfficeJet Pro 9020e",
        "HP LaserJet Pro M404dn"
    ],
    "Áudio e Vídeo": [
        "JBL Flip 6",
        "JBL Charge 5",
        "JBL Tune 720BT",
        "JBL PartyBox Encore",
        "Sony WH-1000XM5",
        "Sony WF-1000XM5",
        "Sony SRS-XB100",
        "Samsung HW-Q600C",
        "Amazon Echo Dot 5ª Geração",
        "Amazon Fire TV Stick 4K Max"
    ],
    "Games": [
        "PlayStation 5 Slim",
        "PlayStation 5 Pro",
        "Xbox Series S 512GB",
        "Xbox Series S 1TB",
        "Nintendo Switch OLED",
        "Nintendo Switch Lite",
        "PlayStation Portal",
        "Controle sem fio DualSense",
        "Controle DualSense Edge",
        "Nintendo Switch Pro Controller"
    ]
}

LOCALIZACOES = [
    ("Aracaju", "SE", "79"),
    ("Salvador", "BA", "71"),
    ("Feira de Santana", "BA", "75"),
    ("Recife", "PE", "81"),
    ("Caruaru", "PE", "81"),
    ("Maceió", "AL", "82"),
    ("João Pessoa", "PB", "83"),
    ("Natal", "RN", "84"),
    ("Fortaleza", "CE", "85"),
    ("Teresina", "PI", "86"),
    ("São Luís", "MA", "98"),
    ("Belém", "PA", "91"),
    ("Manaus", "AM", "92"),
    ("Brasília", "DF", "61"),
    ("Goiânia", "GO", "62"),
    ("Belo Horizonte", "MG", "31"),
    ("Uberlândia", "MG", "34"),
    ("Vitória", "ES", "27"),
    ("Rio de Janeiro", "RJ", "21"),
    ("São Paulo", "SP", "11"),
    ("Campinas", "SP", "19"),
    ("Curitiba", "PR", "41"),
    ("Florianópolis", "SC", "48"),
    ("Porto Alegre", "RS", "51"),
    ("Campo Grande", "MS", "67"),
    ("Cuiabá", "MT", "65"),
    ("Palmas", "TO", "63"),
    ("Porto Velho", "RO", "69"),
    ("Rio Branco", "AC", "68"),
    ("Boa Vista", "RR", "95"),
    ("Macapá", "AP", "96")
]

FAIXAS_PRECO = {
    "Eletrônicos": (2500, 7000),
    "Informática": (800, 8000),
    "Acessórios": (40, 500),
    "Periféricos": (150, 1200),
    "Celulares": (1400, 10000),
    "Escritório": (500, 4500),
    "Áudio e Vídeo": (100, 4500),
    "Games": (500, 7000)
}

PESOS_CATEGORIAS = {
    "Eletrônicos": 1.0,
    "Informática": 1.2,
    "Acessórios": 2.2,
    "Periféricos": 2.0,
    "Celulares": 1.4,
    "Escritório": 1.0,
    "Áudio e Vídeo": 1.8,
    "Games": 1.3
}

MESES_PESOS = [5, 5, 6, 6, 7, 7, 7, 8, 9, 10, 12, 14]

FORMAS_PAGAMENTO = [
    "PIX",
    "CREDITO",
    "DEBITO",
    "DINHEIRO",
    "BOLETO"
]

PESOS_FORMAS_PAGAMENTO = [
    4,
    5,
    2,
    1,
    2
]

STATUS_VENDA = [
    "CONCLUIDA",
    "CANCELADA",
    "PENDENTE"
]

PESOS_STATUS_VENDA = [
    94,
    4,
    2
]


def escapar_sql(texto):
    return str(texto).replace("'", "''")


def gerar_preco(nome_produto, categoria):
    nome = nome_produto.lower()
    minimo, maximo = FAIXAS_PRECO[categoria]

    if "oled c4" in nome:
        if '55"' in nome:
            minimo, maximo = 5000, 6000
        elif '65"' in nome:
            minimo, maximo = 6500, 7500
        elif '77"' in nome:
            minimo, maximo = 8000, 9500
    elif "qned85t" in nome:
        if '55"' in nome:
            minimo, maximo = 3500, 5000
        elif '65"' in nome:
            minimo, maximo = 5000, 6500
    elif "qn90d" in nome:
        if '55"' in nome:
            minimo, maximo = 4500, 6000
        elif '65"' in nome:
            minimo, maximo = 6000, 7500
    elif "du8000" in nome:
        if '50"' in nome:
            minimo, maximo = 2500, 3500
        elif '55"' in nome:
            minimo, maximo = 3000, 4000
    elif "tcl c655" in nome:
        minimo, maximo = 2500, 3500
    elif "inspiron" in nome:
        minimo, maximo = 3000, 5500
    elif "ideapad" in nome:
        minimo, maximo = 2500, 5000
    elif "vivobook" in nome:
        minimo, maximo = 3000, 5500
    elif "aspire" in nome:
        minimo, maximo = 3000, 5500
    elif "nitro" in nome:
        minimo, maximo = 5000, 8500
    elif "tuf gaming" in nome:
        minimo, maximo = 5500, 9000
    elif "ryzen 5 5600g" in nome:
        minimo, maximo = 700, 1100
    elif "ryzen 7 5700x" in nome:
        minimo, maximo = 1100, 1800
    elif "core i5-12400f" in nome:
        minimo, maximo = 800, 1400
    elif "iphone 16 pro max" in nome:
        minimo, maximo = 8000, 10000
    elif "iphone 16 pro" in nome:
        minimo, maximo = 6500, 8500
    elif "iphone 16 plus" in nome:
        minimo, maximo = 5500, 7000
    elif "iphone 16" in nome:
        minimo, maximo = 4500, 6000
    elif "galaxy s25 ultra" in nome:
        minimo, maximo = 6500, 8500
    elif "galaxy s25+" in nome:
        minimo, maximo = 5000, 6500
    elif "galaxy s25" in nome:
        minimo, maximo = 4000, 5500
    elif "galaxy a56" in nome:
        minimo, maximo = 1800, 2500
    elif "galaxy a36" in nome:
        minimo, maximo = 1400, 2000
    elif "edge 50 fusion" in nome:
        minimo, maximo = 1800, 2600
    elif "l3250" in nome:
        minimo, maximo = 800, 1200
    elif "l4260" in nome:
        minimo, maximo = 1200, 1800
    elif "l5590" in nome:
        minimo, maximo = 1500, 2200
    elif "l6270" in nome:
        minimo, maximo = 1800, 2600
    elif "l6490" in nome:
        minimo, maximo = 2200, 3200
    elif "g3110" in nome or "g3170" in nome:
        minimo, maximo = 700, 1200
    elif "g6010" in nome:
        minimo, maximo = 1200, 1800
    elif "officejet" in nome:
        minimo, maximo = 1500, 3000
    elif "laserjet" in nome:
        minimo, maximo = 1500, 3500
    elif "flip 6" in nome:
        minimo, maximo = 400, 700
    elif "charge 5" in nome:
        minimo, maximo = 700, 1000
    elif "tune 720bt" in nome:
        minimo, maximo = 300, 600
    elif "partybox encore" in nome:
        minimo, maximo = 1200, 2000
    elif "wh-1000xm5" in nome:
        minimo, maximo = 1800, 2800
    elif "wf-1000xm5" in nome:
        minimo, maximo = 1200, 2000
    elif "srs-xb100" in nome:
        minimo, maximo = 250, 450
    elif "hw-q600c" in nome:
        minimo, maximo = 1800, 3000
    elif "echo dot" in nome:
        minimo, maximo = 300, 600
    elif "fire tv stick" in nome:
        minimo, maximo = 300, 600
    elif "playstation 5 pro" in nome:
        minimo, maximo = 5500, 7000
    elif "playstation 5 slim" in nome:
        minimo, maximo = 3500, 4500
    elif "xbox series s 1tb" in nome:
        minimo, maximo = 3000, 4000
    elif "xbox series s 512gb" in nome:
        minimo, maximo = 2200, 3200
    elif "switch oled" in nome:
        minimo, maximo = 2500, 3500
    elif "switch lite" in nome:
        minimo, maximo = 1400, 2200
    elif "playstation portal" in nome:
        minimo, maximo = 1500, 2200
    elif "dualsense edge" in nome:
        minimo, maximo = 1000, 1500
    elif "dualsense" in nome:
        minimo, maximo = 400, 600
    elif "switch pro controller" in nome:
        minimo, maximo = 500, 800
    elif "mx master 3s" in nome:
        minimo, maximo = 350, 600
    elif "g502" in nome:
        minimo, maximo = 250, 450
    elif "pro x superlight 2" in nome:
        minimo, maximo = 700, 1100
    elif "k380" in nome:
        minimo, maximo = 180, 300
    elif "g915 tkl" in nome:
        minimo, maximo = 700, 1200
    elif "c920e" in nome:
        minimo, maximo = 300, 500
    elif "g435" in nome:
        minimo, maximo = 300, 500
    elif "deathadder v3" in nome:
        minimo, maximo = 300, 600
    elif "blackshark v2" in nome:
        minimo, maximo = 400, 700
    elif "alloy origins core" in nome:
        minimo, maximo = 400, 700

    return round(random.uniform(minimo, maximo), 2)


def gerar_estoque(preco):
    if preco >= 5000:
        return random.randint(3, 15)
    if preco >= 2000:
        return random.randint(5, 30)
    if preco >= 500:
        return random.randint(10, 50)
    return random.randint(20, 100)


def gerar_data_cadastro():
    return faker.date_time_between(
        start_date=datetime(2024, 1, 1),
        end_date=datetime(2024, 12, 31, 23, 59, 59)
    )


def gerar_cliente():
    tipo_pessoa = random.choices(
        ["PF", "PJ"],
        weights=[90, 10],
        k=1
    )[0]

    if tipo_pessoa == "PF":
        nome = faker.name()
        documento = faker.unique.cpf()
    else:
        nome = faker.company()
        documento = faker.unique.cnpj()

    cidade, estado, ddd = random.choice(LOCALIZACOES)

    telefone = (
        f"({ddd}) "
        f"{random.randint(90000, 99999)}-"
        f"{random.randint(0, 9999):04d}"
    )

    email = faker.email()
    criado_em = gerar_data_cadastro()

    return {
        "nome": nome,
        "tipo_pessoa": tipo_pessoa,
        "documento": documento,
        "cidade": cidade,
        "estado": estado,
        "telefone": telefone,
        "email": email,
        "criado_em": criado_em
    }


def gerar_vendedor():
    nome = faker.name()
    documento = faker.unique.cpf()
    ddd = random.choice(LOCALIZACOES)[2]
    telefone = (
        f"({ddd}) "
        f"{random.randint(90000, 99999)}-"
        f"{random.randint(0, 9999):04d}"
    )
    email = faker.email()
    criado_em = gerar_data_cadastro()

    return {
        "nome": nome,
        "documento": documento,
        "telefone": telefone,
        "email": email,
        "criado_em": criado_em
    }


def gerar_data_venda():
    mes = random.choices(
        range(1, 13),
        weights=MESES_PESOS,
        k=1
    )[0]

    ultimo_dia = calendar.monthrange(2025, mes)[1]
    dia = random.randint(1, ultimo_dia)
    hora = random.randint(8, 21)
    minuto = random.randint(0, 59)
    segundo = random.randint(0, 59)

    return datetime(2025, mes, dia, hora, minuto, segundo)


def escolher_produtos(produtos_gerados, pesos, quantidade):
    escolhidos = []
    ids_escolhidos = set()

    while len(escolhidos) < quantidade:
        produto = random.choices(
            produtos_gerados,
            weights=pesos,
            k=1
        )[0]

        if produto["id"] not in ids_escolhidos:
            escolhidos.append(produto)
            ids_escolhidos.add(produto["id"])

    return escolhidos


quantidade_produtos = sum(
    len(lista) for lista in produtos.values()
)

if quantidade_produtos != 80:
    raise ValueError(
        f"Esperados 80 produtos, mas foram encontrados {quantidade_produtos}."
    )

categorias_ids = {
    categoria: id_categoria
    for id_categoria, categoria in enumerate(categorias, start=1)
}

produtos_gerados = []
produto_id = 1

for categoria, lista_produtos in produtos.items():
    categoria_id = categorias_ids[categoria]

    for nome_produto in lista_produtos:
        preco = gerar_preco(nome_produto, categoria)
        estoque = gerar_estoque(preco)

        produtos_gerados.append({
            "id": produto_id,
            "nome": nome_produto,
            "categoria_id": categoria_id,
            "categoria": categoria,
            "preco": preco,
            "estoque_atual": estoque
        })

        produto_id += 1

clientes = []
clientes_pesos = []

for cliente_id in range(1, QUANTIDADE_CLIENTES + 1):
    cliente = gerar_cliente()
    cliente["id"] = cliente_id
    clientes.append(cliente)

    if cliente_id <= 50:
        clientes_pesos.append(8)
    else:
        clientes_pesos.append(random.randint(1, 4))

vendedores = []

for vendedor_id in range(1, QUANTIDADE_VENDEDORES + 1):
    vendedor = gerar_vendedor()
    vendedor["id"] = vendedor_id
    vendedores.append(vendedor)

produtos_pesos = []
for produto in produtos_gerados:
    peso_categoria = PESOS_CATEGORIAS[produto["categoria"]]
    variacao = random.uniform(0.8, 1.2)
    produtos_pesos.append(peso_categoria * variacao)

vendedores_pesos = [
    3 if vendedor["id"] <= 3 else random.randint(1, 2)
    for vendedor in vendedores
]

with open("./dados/dados_iniciais.sql", "w", encoding="utf-8") as arquivo:
    for categoria in categorias:
        categoria_sql = escapar_sql(categoria)
        criado_em = gerar_data_cadastro()

        sql = (
            "INSERT INTO categorias (nome, criado_em) "
            f"VALUES ('{categoria_sql}', '{criado_em}');"
        )

        arquivo.write(sql + "\n")

    for produto in produtos_gerados:
        nome_sql = escapar_sql(produto["nome"])
        criado_em = gerar_data_cadastro()

        sql = (
            "INSERT INTO produtos "
            "(nome, categoria_id, preco, estoque_atual, criado_em) "
            "VALUES "
            f"('{nome_sql}', {produto['categoria_id']}, "
            f"{produto['preco']:.2f}, {produto['estoque_atual']}, "
            f"'{criado_em}');"
        )

        arquivo.write(sql + "\n")

    for cliente in clientes:
        nome_sql = escapar_sql(cliente["nome"])
        documento_sql = escapar_sql(cliente["documento"])
        cidade_sql = escapar_sql(cliente["cidade"])
        estado_sql = escapar_sql(cliente["estado"])
        telefone_sql = escapar_sql(cliente["telefone"])
        email_sql = escapar_sql(cliente["email"])

        sql = (
            "INSERT INTO clientes "
            "(nome, tipo_pessoa, documento, cidade, estado, "
            "telefone, email, criado_em) "
            "VALUES "
            f"('{nome_sql}', '{cliente['tipo_pessoa']}', "
            f"'{documento_sql}', '{cidade_sql}', '{estado_sql}', "
            f"'{telefone_sql}', '{email_sql}', '{cliente['criado_em']}');"
        )

        arquivo.write(sql + "\n")

    for vendedor in vendedores:
        nome_sql = escapar_sql(vendedor["nome"])
        documento_sql = escapar_sql(vendedor["documento"])
        telefone_sql = escapar_sql(vendedor["telefone"])
        email_sql = escapar_sql(vendedor["email"])

        sql = (
            "INSERT INTO vendedores "
            "(nome, documento, telefone, email, criado_em) "
            "VALUES "
            f"('{nome_sql}', '{documento_sql}', '{telefone_sql}', "
            f"'{email_sql}', '{vendedor['criado_em']}');"
        )

        arquivo.write(sql + "\n")

    quantidade_itens_gerados = 0

    for venda_id in range(1, QUANTIDADE_VENDAS + 1):
        cliente = random.choices(
            clientes,
            weights=clientes_pesos,
            k=1
        )[0]

        vendedor = random.choices(
            vendedores,
            weights=vendedores_pesos,
            k=1
        )[0]

        data_hora = gerar_data_venda()

        forma_pagamento = random.choices(
            FORMAS_PAGAMENTO,
            weights=PESOS_FORMAS_PAGAMENTO,
            k=1
        )[0]

        status = random.choices(
            STATUS_VENDA,
            weights=PESOS_STATUS_VENDA,
            k=1
        )[0]

        sql_venda = (
            "INSERT INTO vendas "
            "(cliente_id, vendedor_id, data_hora, forma_pagamento, status) "
            "VALUES "
            f"({cliente['id']}, {vendedor['id']}, '{data_hora}', "
            f"'{forma_pagamento}', '{status}');"
        )

        arquivo.write(sql_venda + "\n")

        quantidade_itens = random.choices(
            [1, 2, 3, 4, 5],
            weights=[25, 30, 25, 15, 5],
            k=1
        )[0]

        itens = escolher_produtos(
            produtos_gerados,
            produtos_pesos,
            quantidade_itens
        )

        for produto in itens:
            quantidade = random.choices(
                [1, 2, 3, 4],
                weights=[65, 25, 8, 2],
                k=1
            )[0]

            variacao_preco = random.uniform(0.95, 1.05)
            preco_unitario = round(
                produto["preco"] * variacao_preco,
                2
            )

            valor_bruto = quantidade * preco_unitario

            if random.random() < 0.30:
                percentual_desconto = random.uniform(0.03, 0.10)
                desconto = round(
                    valor_bruto * percentual_desconto,
                    2
                )
            else:
                desconto = 0

            sql_item = (
                "INSERT INTO itens_venda "
                "(venda_id, produto_id, quantidade, preco_unitario, desconto) "
                "VALUES "
                f"({venda_id}, {produto['id']}, {quantidade}, "
                f"{preco_unitario:.2f}, {desconto:.2f});"
            )

            arquivo.write(sql_item + "\n")
            quantidade_itens_gerados += 1


print(f"Categorias geradas: {len(categorias)}")
print(f"Produtos gerados: {len(produtos_gerados)}")
print(f"Clientes gerados: {len(clientes)}")
print(f"Vendedores gerados: {len(vendedores)}")
print(f"Vendas geradas: {QUANTIDADE_VENDAS}")
print(f"Itens de venda gerados: {quantidade_itens_gerados}")
print("O arquivo dados/dados_iniciais.sql foi criado com sucesso!")
