# %%

import pandas as pd
import sqlalchemy

# %%

# CRIA A CONEXÃO COM O BANCO DE DADOS
engine = sqlalchemy.create_engine('sqlite:///../data/olist.db')

# %%

# ACESSANDO UMA TABELA
clientes = pd.read_sql_table(table_name='tb_customers', con=engine)
clientes

# %%

# TAMBÉM PODEMOS USAR SQL PARA CONSULTAR
query = 'SELECT * FROM tb_customers LIMIT 100'
clientes_100 = pd.read_sql_query(query, con=engine)
clientes_100

# %%

# UMA QUERY MAIS COMPLEXA
query = '''
SELECT seller_id,
       sum(price) AS valor_total,
       count(distinct order_id) AS qtd_pedidos
  FROM tb_order_items
 GROUP BY seller_id'''
orders = pd.read_sql_query(query, con=engine)
orders

# %%

# PODEMOS SALVAR O DADO DO PYTHON NO BD TAMBÉM,
# NO CASO ABAIXO, ELE IRÁ CRIAR UMA TABELA
# CHAMADA orders_per_customer
orders.to_sql('orders_per_customer',
              con=engine,
              index=False,
              if_exists='replace')