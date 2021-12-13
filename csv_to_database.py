# import psycopg2

# conn = psycopg2.connect(
#     host="arjuna.db.elephantsql.com",
#     database="xdzwpuop",
#     user="xdzwpuop",
#     password="uW8dSE7OdUye6fuCni7x4Gy5atztstog")



# cur = conn.cursor()

# cur.execute("DROP TABLE IF EXISTS shopee_product")

# cur.execute("""CREATE TABLE shopee_product (
#     product_title VARCHAR(1000),
#     lowest_price FLOAT,
#     montly_sales INTEGER,
#     original_price FLOAT,
#     discount_rate INTEGER,
#     star FLOAT,
#     ratings FLOAT,
#     total_sales INTEGER,
#     favorites INTEGER,
#     brand VARCHAR(50),
#     weight FLOAT,
#     warranty INTEGER,
#     capacity  FLOAT,
#     stock INTEGER,
#     power INTEGER

# );""")

# cur.execute

# conn.commit()

import pandas as pd
final = pd.read_csv('product_info_list.csv')
final.columns = [c.lower() for c in final.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://xdzwpuop:uW8dSE7OdUye6fuCni7x4Gy5atztstog@arjuna.db.elephantsql.com:5432/xdzwpuop')

final.to_sql("my_table_name", engine)