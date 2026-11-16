import pyodbc
from sqlalchemy import create_engine
from urllib.parse import quote_plus

server = r"localhost\SQLEXPRESS02"
def connect_db(database = "master", autocommit = False):
    con = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;",
    autocommit=autocommit
    )
    return con



def get_engine(database="E-Commerce_Customer_Behavior"):
    connect_string = quote_plus(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return create_engine(
        f"mssql+pyodbc:///?odbc_connect={connect_string}",
        fast_executemany=True,
    )
