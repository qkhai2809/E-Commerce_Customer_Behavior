from connection import connect_db
con = connect_db("E-Commerce_Customer_Behavior")
cursor = con.cursor()

#Create customers_dim
cursor.execute("""
CREATE TABLE dbo.customers_dim(
customer_id              VARCHAR(20) PRIMARY KEY              ,
customer_name             NVARCHAR(100)                         ,
customer_age              INT                     ,
gender                    VARCHAR(20)                        ,
customer_segment          VARCHAR(50)                        ,
customer_city              NVARCHAR(100),
customer_state              NVARCHAR(50),
customer_country             NVARCHAR(50),
region                      VARCHAR(20),
customer_postal_code         INT   ,
customer_acquisition_cost    DECIMAL(10,5)
)""")
# Create products_dim
cursor.execute("""
CREATE TABLE dbo.products_dim(
 product_id             VARCHAR(20)    PRIMARY KEY,
 product_name           NVARCHAR(100),
 product_category       VARCHAR(50),
 product_subcategory    VARCHAR(50),
 brand                  NVARCHAR(100),
 supplier               NVARCHAR(100),
 unit_price             DECIMAL(18,2),
 product_cost           DECIMAL(18, 2),
 product_rating         DECIMAL(3, 1)
)""")
#Create sales_fact
cursor.execute("""
CREATE TABLE dbo.sales_fact(
 order_id      VARCHAR(20)    PRIMARY KEY,
 order_date     DATE,
 order_time      TIME,
 order_status    VARCHAR(50),
 sales_channel   VARCHAR(50),
 customer_id      VARCHAR(20),
 payment_method   VARCHAR(20),
 payment_status   VARCHAR(50),
 currency         VARCHAR(10),
 shipping_method  VARCHAR(50),
 delivery_days    FLOAT,
 estimated_delivery_days  FLOAT,
 delivery_status      VARCHAR(20),
 return_status          VARCHAR(10),
 return_reason        NVARCHAR(50),
 customer_rating       DECIMAL(5, 1),
 review_sentiment      VARCHAR(20),
 customer_review       NVARCHAR(100),
 marketing_channel     VARCHAR(50),
 campaign_name         NVARCHAR(50),
 coupon_code           VARCHAR(10),
 loyalty_points_earned  INT,
 loyalty_points_redeemed   INT,
 quantity                INT,
 gross_sales          DECIMAL(18, 2),
 discount_amount      DECIMAL(18, 2),
 tax_amount            DECIMAL(18, 2),
 shipping_cost          DECIMAL(18, 2),
 net_sales                DECIMAL(18, 2),
 product_cost            DECIMAL(18, 2),
 profit                  DECIMAL(18, 2),
 profit_margin_percentage  DECIMAL(5, 2),
 customer_lifetime_value    DECIMAL(18, 2),
 is_repeat_customer         BIT,
 customer_order_count       INT,
 FOREIGN KEY (customer_id) REFERENCES dbo.customers_dim(customer_id)
 )""")
#Create order_bridge
cursor.execute("""
CREATE TABLE dbo.order_bridge(
 order_items_id       INT IDENTITY(1,1) PRIMARY KEY,
 order_id             VARCHAR(20),
 product_id           VARCHAR(20),
 quantity             INT,
 unit_price           DECIMAL(18, 2),
 discount_percentage  DECIMAL(11, 10),
 discount_amount      DECIMAL(18, 2),
 gross_sales          DECIMAL(18, 2),
 tax_amount           DECIMAL(18, 2),
 shipping_cost        DECIMAL(18, 2),
 net_sales            DECIMAL(18, 2),
 product_cost         DECIMAL(18, 2),
 profit               DECIMAL(18, 2),
 FOREIGN KEY (order_id) REFERENCES dbo.sales_fact(order_id),
 FOREIGN KEY (product_id) REFERENCES dbo.products_dim(product_id)

 )""")

con.commit()
con.close()




