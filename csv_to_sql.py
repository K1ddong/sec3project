import pandas as pd
import sqlite3

conn = sqlite3.connect('product_info_list.db')
cur = conn.cursor()

data = pd.read_csv('product_info_list.csv')

data.to_sql('products', conn, if_exists='append', index=False)