 <p align="center">
  <strong>Análise de Vendas</strong>
</p>

<p align="center">
  Projeto pessoal utilizando SQL, PostgreSQL, Docker e Python para explorar dados comerciais fictícios.
</p>

<p align="center">
  <a href="https://www.postgresql.org/">
    <img src="https://img.shields.io/badge/PostgreSQL-18-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL 18">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.12.3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12.3">
  </a>
  <a href="https://www.postgresql.org/docs/">
    <img src="https://img.shields.io/badge/SQL-Queries-4479A1?style=for-the-badge" alt="SQL">
  </a>
  <a href="https://faker.readthedocs.io/">
    <img src="https://img.shields.io/badge/Faker-Dados%20Sint%C3%A9ticos-45A049?style=for-the-badge" alt="Faker">
  </a>
  <a href="https://docs.docker.com/compose/">
    <img src="https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Compose">
  </a>
  <a href="https://github.com/ranslmwarezz/analise-vendas">
    <img src="https://img.shields.io/github/last-commit/ranslmwarezz/analise-vendas?style=for-the-badge" alt="Último commit">
  </a>
</p>

---

## Modelo de dados

O banco de dados é composto por seis tabelas:

- `clientes`: informações de identificação, localização e contato dos clientes.
- `categorias`: categorias dos produtos comercializados.
- `produtos`: produtos, preços, estoque e categorias relacionadas.
- `vendedores`: informações de identificação e contato dos vendedores.
- `vendas`: registros das vendas, incluindo cliente, vendedor, data, forma de pagamento e status.
- `itens_venda`: produtos incluídos em cada venda, com quantidade, preço unitário e desconto.

As tabelas são relacionadas por chaves primárias e estrangeiras, com restrições para garantir a integridade dos dados. Uma venda pode conter vários itens, e cada item está associado a um produto.

A estrutura do banco está definida em [`sql/schema.sql`](sql/schema.sql).

## Pré-requisitos

Para executar o projeto, você precisará de:

- Git
- Docker Engine e Docker Compose
- Python 3.12.3 e pip, caso deseje gerar novamente os dados sintéticos.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/ranslmwarezz/analise-vendas.git
cd analise-vendas
```

### 2. Configurar as variáveis de ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e configure as variáveis utilizadas pelo Docker Compose:

```dotenv
POSTGRES_DB=analise_vendas
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_local
POSTGRES_PORT=5432
```

Substitua `sua_senha_local` por uma senha definida no seu ambiente.

### 3. Iniciar o PostgreSQL

Com o arquivo `.env` configurado, execute:

```bash
sudo docker compose up -d
```

Confira o estado do serviço:

```bash
sudo docker compose ps
```

O PostgreSQL é executado em um contêiner Docker, e os dados são armazenados em um volume persistente.

Se o Docker estiver configurado para funcionar sem privilégios de administrador no seu sistema, você poderá executar os comandos sem `sudo`.

### 4. Criar as tabelas

Com o PostgreSQL em execução, execute o schema:

```bash
sudo docker compose exec -T postgres \
  psql -U postgres -d analise_vendas < sql/schema.sql
```

Esse comando cria as tabelas, os relacionamentos e as restrições definidas no schema.

### 5. Carregar os dados iniciais

O projeto já inclui um conjunto de dados sintéticos em `dados/dados_iniciais.sql`.

Para carregar os registros no banco:

```bash
sudo docker compose exec -T postgres \
  psql -U postgres -d analise_vendas < dados/dados_iniciais.sql
```

**Importante:** execute o schema e a carga inicial apenas uma vez em um banco vazio. Reexecutar o schema pode causar erros porque as tabelas já existirão, e recarregar os mesmos dados pode gerar duplicações ou conflitos.

Os comandos acima utilizam os valores padrão de usuário e banco. Caso você altere esses valores no `.env`, ajuste também os parâmetros `-U` e `-d` dos comandos.

### 6. Executar as consultas SQL

As consultas estão armazenadas individualmente na pasta `sql/consultas/`.

Para executar uma consulta, utilize:

```bash
sudo docker compose exec -T postgres \
  psql -U postgres -d analise_vendas < sql/consultas/01-faturamento-total.sql
```

Para executar outra consulta, substitua o caminho pelo arquivo SQL desejado.

Os resultados são apresentados diretamente no terminal.

### 7. Gerar novos dados (opcional)

O arquivo `dados/dados_iniciais.sql` já está disponível no repositório. A geração de uma nova massa de dados é opcional.

Crie um ambiente virtual Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute o gerador a partir da raiz do projeto:

```bash
python3 scripts/gerar_dados.py
```

O script utiliza Faker para gerar novos dados sintéticos e sobrescreve o arquivo `dados/dados_iniciais.sql`.

A geração dos dados não os carrega automaticamente no PostgreSQL. Para utilizar a nova massa, carregue o arquivo em um banco vazio, seguindo as etapas anteriores.

## Status do projeto

Projeto em desenvolvimento, com consultas SQL e análises sendo adicionadas conforme a evolução dos estudos.
