from connection import get_engine
import pandas as pd
engine = get_engine()
df_cus = pd.read_csv("data/processed/customers_cleaned.csv")
df_pro = pd.read_csv("data/processed/products_clean.csv")
df_sale = pd.read_csv("data/processed/sales_cleaned.csv")
df_ord = pd.read_csv("data/processed/orders_clean.csv")
print("Loading customers_dim!")
df_cus.to_sql(
    name = "customers_dim",
    con = engine,
    schema="dbo",
    if_exists="append",
    index = False,
    chunksize=1000
)
print("Loading products_dim!")
df_pro.to_sql(
    name = "products_dim",
    con = engine,
    schema="dbo",
    if_exists="append",
    index = False,
    chunksize=1000
)
print("Loading sales_fact!")
df_sale.to_sql(
    name = "sales_fact",
    con = engine,
    schema = "dbo",
    if_exists="append",
    index = False,
    chunksize=1000
)
print("Loading order_bridge!")
df_ord.to_sql(
    name = "order_bridge",
    con = engine,
    schema = "dbo",
    if_exists="append",
    index=False,
    chunksize=1000
)
