from connection import connect_db
con = connect_db("master", autocommit=True)

cursor = con.cursor()

cursor.execute("""
IF DB_ID('E-Commerce_Customer_Behavior') IS NULL
CREATE DATABASE [E-Commerce_Customer_Behavior]
""")

con.commit()
con.close()
